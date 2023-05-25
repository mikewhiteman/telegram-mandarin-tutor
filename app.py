import os
import openai
from dotenv import load_dotenv
import telebot
import requests
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from chatgpt_settings import ChatgptAgent

load_dotenv()

# API keys defined in .env file
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
openai.api_key = os.getenv('OPENAPI_KEY')

#Initialize Telegram/OpenAI agents
telegram_bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
openai_agent = ChatgptAgent()


# This will store previous messages - hacky but works for 1:1 convos w/o long-term memory
global previous_messages
previous_messages = []

def send_message() -> str:
    base_prompt = openai_agent.base_prompt
    message_to_send = base_prompt + previous_messages 

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_to_send,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    print(send_message())
