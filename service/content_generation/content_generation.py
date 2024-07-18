import asyncio
import time

from openai import OpenAI
from config import config
from model.session import Conversation, OpenAIMessageRole, Session
from repository.generation_session import SessionRepository
from bson import ObjectId
from schema.schema import serialize_session
from service.content_generation.prompts import INIT_PROMPT, RESPOND_PROMPT, ENHANCE_IMAGE_PROMPT


class ContentGenerationService:
    def __init__(self):
        self.session_repository = SessionRepository()
        self.openai_client = OpenAI(api_key=config.OPENAI_API_KEY)

    def create_session(self):
        init_conversation = Conversation(role=OpenAIMessageRole.USER.value, content=INIT_PROMPT)
        new_session = Session(conversations=[init_conversation])
        inserted_id = self.session_repository.create_session(new_session)
        session_data = SessionRepository().get_session(inserted_id)
        return serialize_session(session_data)

    def get_session(self, session_id):
        session_id = ObjectId(session_id)
        session_data = self.session_repository.get_session(session_id)
        return serialize_session(session_data)

    def append_conversation(self, session_id: ObjectId, conversation):
        session_data = self.session_repository.get_session(session_id)
        if not session_data:
            raise Exception("Session not found")

        conversations = session_data["conversations"]
        conversations.append(conversation.model_dump())
        self.session_repository.update_conversations(session_id, conversations)

    def send_message(self, session_id, message):
        session_id = ObjectId(session_id)
        new_conversation = Conversation(role=OpenAIMessageRole.USER.value, content=message)
        self.append_conversation(session_id, new_conversation)
        updated_session_data = self.session_repository.get_session(session_id)
        return serialize_session(updated_session_data)

    def respond(self, session_id):
        start_time = time.time()
        session_id = ObjectId(session_id)
        respond_conversation = Conversation(role=OpenAIMessageRole.USER.value, content=RESPOND_PROMPT)
        self.append_conversation(session_id, respond_conversation)
        updated_session_data = self.session_repository.get_session(session_id)

        conversations = updated_session_data["conversations"]
        response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversations
        )

        response_text = response.choices[0].message.content
        extracted_json_response = extract_json_from_text(response_text)
        extracted_json_response = self.generate_images(extracted_json_response)
        self.session_repository.update_session_generated_response(session_id, extracted_json_response)
        print(f"Responded in {time.time() - start_time} seconds")
        return extracted_json_response

    def generate_images(self, generated_response):
        for tag in generated_response["tags"]:
            if tag["type"] == "image":
                image_url = self.text_to_image(tag["prompt"])
                tag["value"] = image_url
        return generated_response

    def text_to_image(self, prompt):
        prompt = f"{prompt}. {ENHANCE_IMAGE_PROMPT}"
        print(f"Generating image for prompt: {prompt}")
        response = self.openai_client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        print(f"Generated image for prompt: {prompt} with url: {image_url}")
        return image_url


def extract_json_from_text(text: str):
    json_start = text.index('{')
    json_end = text.rindex('}')
    return eval(text[json_start:json_end + 1])
