# LLM Assisted Keyword extraction:
import google.generativeai as palm
import prompts as pr
from dotenv import load_dotenv
import os

load_dotenv()
palm_api_key = os.getenv("GOOGLE_PALM_API")

def extract(text):
    text = text.replace("*", "")
    lines = [line.strip() for line in text.splitlines()]

    keywords = [lines[i] for i in range(len(lines)) if i > 1]
    return keywords

def furtherSearch(text:str):
    palm.configure(api_key=palm_api_key)
    model = palm.get_model('models/chat-bison-001')

    response = palm.chat(messages=f"return keywords for the following text: {text}. return only the keywords and no other text. just the keywords in form of a python list.", temperature=1, context=pr.context)
    keywords = extract(response.last)

    return keywords