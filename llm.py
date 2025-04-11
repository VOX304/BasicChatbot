import os
import google.generativeai as genai
from src.prompt import system_instruction
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

# Ensure API Key is loaded
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Missing Gemini API Key. Set GEMINI_API_KEY in .env")

# Configure Gemini API
genai.configure(api_key=api_key)

messages = [{"role": "system", "content": system_instruction}]

async def ask_order(messages, model="gemini-2.0-flash-thinking-exp-01-21", temperature=0.7):
    """ Sends user messages to Google Gemini API and returns response """
    try:
        model = genai.GenerativeModel(model)

        # Combine system instruction with user messages
        conversation = [{"role": "system", "content": system_instruction}] + messages

        response = model.generate_content([msg["content"] for msg in conversation])
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"