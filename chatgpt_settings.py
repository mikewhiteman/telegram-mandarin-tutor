class ChatgptAgent:
    def __init__(self, model='gpt-3.5-turbo', temperature=.7, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penality = presence_penalty
        self.base_prompt = [{"role": "system", "content": "Hi ChatGPT!"}]

