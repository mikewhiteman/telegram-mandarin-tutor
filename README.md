# Mandarin Chinese Language Tutor w/ Telegram + ChatGPT

## Background
This is a small proof of concept app demonstrating how Telegram, ChatGPT, and a few free text to speech libraries can be combined into an AI language tutor. I've seen a few demos highlighting text-based convos with a LLM bot but felt like the experience could be greatly improved if you could speak practice _speaking_ directly with the bot.  I've been studying Mandarin for a few years now and figured I'd share this idea with others as a potential learning tool. 

The general concept is quite simple:
* Setup a Telegram bot which natively supports sending/receiving audio files
* Connect the Telegram bot to an LLM agent (in this case ChatGPT) who is instructed to act as a language tutor
* Use open source TTS libraries to convert the user's voice into text for ChatGPT and on the reverse path convert ChatGPT's text response a  voice output

## Demo


## Installation
* `pip install -r requirements.txt`
* Populate the the .env file with your API keys for Telegram and ChatGPT
* If you wish to speak with the bot in Mandarin, you're done!

## Can I use this for other languages besides Mandarin?
Yes absolutely, there's just a few things you'll need to change
1. Update the `base_prompt` in [chatgpt_settings.py](chatgpt_settings.py)
2. Update the language variable in `convert_voice_to_text()`:

```
    r = sr.Recognizer()
    with sr.AudioFile("voice_message.wav") as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="zh-CN")
        print(f"Converted audio to the following text: {text}")
```
You can find a full list of supported languages for Google's Speech Recognition APIs [here](https://codelabs.developers.google.com/codelabs/cloud-speech-text-python3#5)

3. Update the Google Text to Speech language (gTTS) library setting in `response_text_to_audio()`:

```
    # Use Google Text-to-Speech to convert the text to speech
    tts = gTTS(text, lang="zh")
    tts.save("voice_message.mp3")
```

Note: The easiest way to get a list of available languages is to print them with `gtts-cli --all`
