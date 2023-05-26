# Mandarin Chinese Language Tutor w/ Telegram + ChatGPT

## Background
This is a small proof of concept app that I built demonstrating how Telegram, ChatGPT, and a few free text <> speech libraries can be combined into an AI language tutor. I've seen a few demos highlighting text-based convos with a LLM bot but felt like the experience could be greatly improved if you could speak practice _speaking_ directly with the bot.  I've been studying Mandarin for a few years now and figured I'd share this idea with others as a potential learning tool. 

The general concept is quite simple:
* Setup a Telegram bot which natively supports sending/receiving audio files
* Connect the Telegram bot to an LLM agent (in this case ChatGPT) who is instructed to act as a language tutor
* Use open source TTS libraries to convert the user's voice into text for ChatGPT and on the reverse path convert ChatGPT's text response a  voice output

## Installation
* pip install -r requirements.txt
* Populate the the .env file with your API keys for Telegram and ChatGPT
* If you wish to speak with the bot in Mandarin, you're done!

## Can I use this for other languages besides Mandarin?
