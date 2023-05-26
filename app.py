import os
import openai
import telebot
import requests
import speech_recognition as sr
from dotenv import load_dotenv
from gtts import gTTS
from pydub import AudioSegment
from chatgpt_agent import ChatgptAgent

load_dotenv()

# API keys defined in .env file
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
openai.api_key = os.getenv('OPENAPI_KEY')

#Initialize Telegram/OpenAI agents
telegram_bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
chatgpt_agent = ChatgptAgent()

# This will store previous messages - hacky but works for 1:1 convos w/o long-term memory
global previous_messages
previous_messages = []


# Telegram speech recognition logic
@telegram_bot.message_handler(content_types=["voice"])
def telegram_handler(message: telebot.types.Message):
    # Grab user_id from the request
    user_id = message.chat.id
    
    # Fetch remote location for the user's voice file
    voice_file_info = telegram_bot.get_file(message.voice.file_id)
    voice_file_path = voice_file_info.file_path

    # Convert voice file to text
    user_request_text= convert_voice_to_text(voice_file_path)

    # Send text to ChatGPT API
    chatgpt_response = request_chatgpt(user_request_text, user_id)

    # Send ChatGPT's response to telegram
    telegram_bot.send_message(user_id, chatgpt_response)

    # Convert ChatGPT's response to Telegram voice file and send via telegram bot
    voice_file_name = convert_text_to_voice(chatgpt_response)
    voice = open(voice_file_name, "rb")
    telegram_bot.send_voice(message.chat.id, voice)
    voice.close()

    # Remove ChatGPT's voice file once sent
    os.remove("voice_message_reply.ogg")


def convert_voice_to_text(voice_file_path: str) -> str:
    audio_file = requests.get(f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{voice_file_path}")

    # Save file locally
    with open("voice_message.ogg", "wb") as f:
        f.write(audio_file.content)

    # Convert to WAV so we can transcribe the audio using 
    sound = AudioSegment.from_file("voice_message.ogg", format="ogg")
    sound.export("voice_message.wav", format="wav")

    # Use SpeechRecognition w/ Google Speech Recognition APIs to transcribe the voice message
    r = sr.Recognizer()
    with sr.AudioFile("voice_message.wav") as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="zh-CN")
        print(f"Converted audio to the following text: {text}")

    # Clean-up text files
    os.remove("voice_message.ogg")
    os.remove("voice_message.wav")

    return text

def convert_text_to_voice(text: str) -> str:
    # Use Google Text-to-Speech to convert the text to speech
    tts = gTTS(text, lang="zh")
    tts.save("voice_message.mp3")

    # Use pydub to convert to OGG format
    ogg_file_name = "voice_message_reply.ogg"
    sound = AudioSegment.from_mp3("voice_message.mp3")
    sound.export(ogg_file_name, format="mp3")

    os.remove("voice_message.mp3")

    return ogg_file_name

def request_chatgpt(text: str, user_id: str) -> str:
    previous_messages.append({"role": "user", "content": text})
    base_prompt = chatgpt_agent.base_prompt
    message_to_send = base_prompt + previous_messages 

    print(f"Sending the following message to ChatGPT: {message_to_send}")

    raw_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_to_send,
        temperature=chatgpt_agent.temperature,
        max_tokens=chatgpt_agent.max_tokens
    )

    response = raw_response['choices'][0]['message']['content']
    previous_messages.append({"role":"assistant", "content": response})
    print(f"ChatGPT responded with: {response}")

    return response

if __name__ == "__main__":
    telegram_bot.polling()
