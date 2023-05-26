# Mandarin Chinese Language Tutor w/ Telegram + ChatGPT

## Background
This is a proof of concept demonstrating how you can build a **conversation-based language tutor** using Telegram, ChatGPT, and a few free text-to-speech libraries. I've seen a few demos highlighting text-based conversations with a LLM language tutor but felt like the experience could be greatly improved if you could actually practice _speaking_ with the bot.  I've been studying Mandarin for a bit and decided I'd try this out as a potential learning tool.

The general concept is quite simple:
* Setup a Telegram bot which natively supports sending/receiving audio files
* Connect the Telegram bot to an LLM agent (in this case ChatGPT) who is instructed to act as a language tutor
* Use open source TTS libraries to convert the user's voice into text for ChatGPT to parse and on the reverse path convert ChatGPT's text response to an audio (voice) output

## Demo

Here's a quick demo where I'm having a basic conversation with the tutor bot in Mandarin.

### (Unmute Audio - apologies for my poor Mandarin skills!)

https://github.com/mikewhiteman/telegram-mandarin-tutor/assets/46505379/e180f8ff-061b-4f93-8570-ccd98e4df75f

I find the dynamic nature of the LLM conversations fascinating - the topics tend to vary significantly and often feel very similar to real speaking practice, where you can choose to switch into English if you don't understand a topic (see the 1:05 mark where I requested the tutor repeat the question in English).

## How do I set this up?
* `pip install -r requirements.txt`
* Create a [Telegram bot](https://core.telegram.org/bots/api) and generate an API key
* Create an [OpenAI Platform account](https://platform.openai.com) and generate an API key
* Populate an `.env` file (or configure environment variables) with your API keys for Telegram and ChatGPT
* If you wish to speak with the bot in Mandarin, you're done! Just run `python3 app.py` and start chatting with the bot using the Telegram web or mobile app. 

## Can I use this for other languages besides Mandarin?
Yes absolutely, there are just a few things you'll need to change:
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

3. Update the `lang` setting in the Google Text to Speech (gTTS) library used by `response_text_to_audio()`:

```
    # Use Google Text-to-Speech to convert the text to speech
    tts = gTTS(text, lang="zh")
    tts.save("voice_message.mp3")
```

Note: The easiest way to get a list of available languages is to print them with `gtts-cli --all`
