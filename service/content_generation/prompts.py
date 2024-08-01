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
STEP 3: Check the json object to make sure it is RFC8259 compliant. Make sure all the keys and values are in double 
quotes. If there is any error, you have to fix it.
STEP 4: After you finish the json object, send it back to me. Do not include any explanations, 
only provide a  RFC8259 compliant JSON response.
"""
ENHANCE_IMAGE_PROMPT = """The image should be realistic, natural looks"""

GEN_PARAGRAPH_PROMPT = """Rewrite the following paragraph in your own words. 
The paragraph should be about {{NUM_WORDS}} words long and contains the following keywords: {{KEYWORDS}}.
Here is the previous paragraph: {{PREVIOUS_PARAGRAPH}}.
Here is the extra description to write new paragraph: {{DESCRIPTION}}. 
"""

GEN_BLOG_PROMPT = """You are a helpful assistant. You are here to help user to write a SEO friendly article.
Follows these steps to generate the content:
STEP 1: Write me an article following description: {{DESCRIPTION}}.
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
      "type": "paragraph",
      "prompt": "must fill with short description of the paragraph",
      "value": "must fill with paragraph content"
    }
  ]
}
STEP 3: Check the json object to make sure it is RFC8259 compliant. Make sure all the keys and values are in double 
quotes. If there is any error, you have to fix it.
STEP 4: After you finish the json object, send it back to me. Do not include any explanations, 
only provide a  RFC8259 compliant JSON response.
"""
