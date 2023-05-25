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

# Static keys defined in .env file
OPENAPI_KEY = os.getenv('OPENAPI_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

#Initialize Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

#Initial chat request

previous_messages = []

def chat_request(previous_messages: list) -> str:






    return 'test'