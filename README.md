# Mandarin Chinese Language Tutor w/ Telegram + ChatGPT

## Background
This is a proof of concept demonstrating how you can build a **voice-based language tutor** using Telegram, ChatGPT, and Google's free speech recognition and text-to-speech libraries. I've seen a few demos highlighting text-based conversations with a LLM language tutor but felt like the experience could be greatly improved if you could actually practice _speaking_ with your LLM tutor.  I've been studying Mandarin for a bit and decided I'd try this out as a potential learning tool.

## Demo

Here's a quick demo where I'm having a basic conversation with the ChatGPT-powered tutor in Mandarin.

### (Unmute Audio - apologies for my poor Mandarin skills!)

https://github.com/mikewhiteman/telegram-mandarin-tutor/assets/46505379/c1025346-6968-4867-a02c-e433803c2fc1

While it's not a substitute for real speaking practice, I find the dynamic nature of the LLM conversations fascinating. The topics tend to vary significantly (particularly if you play with ChatGPT's temperature setting) and often feel very similar to real speaking practice, particularly since you can switch into English if you don't understand a topic (see the 0:25 mark where I requested the tutor repeat the question in English).

## How do I set this up?
* `pip install -r requirements.txt` (Python 3.6+)
* Create a [Telegram bot](https://core.telegram.org/bots/api) and generate an API key
* Create an [OpenAI Platform account](https://platform.openai.com) and generate an API key
* Populate an `.env` file (or configure environment variables) with your API keys for Telegram and ChatGPT
* If you wish to speak with the bot in Mandarin, you're done! Just run `python3 app.py` and start chatting with the bot using the Telegram app. 

## Can I use this for other languages besides Mandarin?
Yes absolutely, there are just a few things you'll need to change:
1. Update the `base_prompt` in [chatgpt_agent.py](chatgpt_agent.py)
2. Update the language parameter in `convert_voice_to_text()` to a supported language:

```
    r = sr.Recognizer()
    with sr.AudioFile("voice_message.wav") as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="zh-CN")
        print(f"Converted audio to the following text: {text}")
```
You can find a full list of supported languages for Google's Speech Recognition APIs [here](https://codelabs.developers.google.com/codelabs/cloud-speech-text-python3#5)

3. Update the `lang` parameter in the Google Text to Speech (gTTS) library used by `response_text_to_audio()`:

```
    # Use Google Text-to-Speech to convert the text to speech
    tts = gTTS(text, lang="zh")
    tts.save("voice_message.mp3")
```

Note: The easiest way to get a list of available gTTS languages is to print them with `gtts-cli --all`


## To Do:
- [ ] Add support for multiple languages (ultimately a rather simple mapping exercise across the supported languages in the Speech Recognition & TTS libraries)
- [ ] Replace gTTS library with more realistic sounding alternatives. gTTS is a fantastic free service but I think I can find fairly inexpensive alternatives that would provide a much more realistic sounding voice for the Mandarin tutor. 
- [ ] Build conversation caching so the bot can recall recent conversations and hold conversations with multiple users at once 
