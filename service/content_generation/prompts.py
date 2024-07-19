INIT_PROMPT = """You are a helpful assistant. You are here to help user to write a SEO friendly article."""
RESPOND_PROMPT = """Follows these steps to generate the content:
STEP 1: Write me an article with length of {{NUM_WORDS}} words, which is about the topic: {{TOPIC}}. {{EXTRA_INFO}}. 
{{DESCRIPTION}}
STEP 2: You have to fill fill article content into a RFC8259 json object. The format is as follows: 
{
  "title": "fill the title of the article",
  "introduction": "briefly introduction about the content, the goal of article",
  "tags": [
    {
      "type": "must fill with h2 or h3",
      "value": "must fill with heading text",
    },
    {
      "type": "image",
      "prompt": "must fill with a prompt which can be used to generate image by AI",
    },
    {
      "type": "paragraph",
      "prompt": "must fill with short description of the paragraph",
      "value": "must fill with paragraph content"
    }
  ]
}
There have to be {{NUM_IMAGES}} image tags in the json object. The image tags should be placed after the heading tags.
STEP 3: If number of image tags is greater than {{NUM_IMAGES}}, you have to remove the image tags from the end 
of the json object un til the number of image tags is equal to {{NUM_IMAGES}}.
STEP 4: After you finish the json object, send it back to me. Do not include any explanations, 
only provide a  RFC8259 compliant JSON response.
"""
ENHANCE_IMAGE_PROMPT = """The image should be realistic, natural looks"""
