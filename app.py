import chainlit as cl
from src.llm import ask_order, messages  # Now using Gemini API
from dotenv import load_dotenv

load_dotenv()

@cl.on_chat_start
async def main():
    await cl.Message(content="Hello, Welcome to our online store.").send()


@cl.on_message
async def handle_message(message: cl.Message):
    messages.append({"role": "user", "content": message.content})

    response = await ask_order(messages)  # ✅ Calls Gemini
    messages.append({"role": "assistant", "content": response})

    await send_response(response)

async def send_response(response):
    await cl.Message(content=response).send()