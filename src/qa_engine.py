import os
import requests

class QAEngine:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "meta-llama/llama-4-maverick-17b-128e-instruct"

    def ask_about_celebrity(self, name, question):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        prompt = f"""
        You are an AI Assistant that knows a lot about celebrities.
        Answer concisely and accurately about {name}.
        
        Question: {question}
        """

        payload = {
            "model": self.model,
            "messages": [   # ✅ fixed
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 512  # ✅ fixed
        }

        response = requests.post(url=self.api_url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]  # ✅ fixed

        return "Sorry, I couldn't find the answer"
