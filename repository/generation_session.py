from bson import ObjectId

from model.session import Session
from repository.mongodb import MongoDB


class SessionRepository:
    def __init__(self):
        self.collection = MongoDB().get_db()["generation_sessions"]

    def create_session(self, session):
        return self.collection.insert_one(session.model_dump()).inserted_id

    def update_session(self, session_id: ObjectId, session_data):
        self.collection.update_one({"_id": session_id}, {
            "$set": session_data,
        })

    def update_conversations(self, session_id: ObjectId, conversations):
        self.collection.update_one({"_id": session_id}, {
            "$set": {
                "conversations": conversations,
            },
        })

    def get_session(self, session_id: ObjectId):
        return self.collection.find_one({"_id": session_id})

    def update_session_generated_response(self, session_id, extracted_json_response):
        self.collection.update_one({"_id": session_id}, {
            "$set": {
                "generated_response": extracted_json_response,
            },
        })

    def update_status(self, session_id, status):
        self.collection.update_one({"_id": session_id}, {
            "$set": {
                "status": status,
            },
        })
