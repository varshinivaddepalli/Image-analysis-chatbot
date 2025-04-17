import requests
import json

class LLMClient:
    def __init__(self):
        self.API_URL = "https://api.groq.com/openai/v1/chat/completions"
        self.API_KEY = "Your Groq API key here"
        self.MODEL_NAME = "llama-3.3-70b-versatile"
        
    def generate_response(self, prompt, context=None):
        headers = {
            "Authorization": f"Bearer {self.API_KEY}",
            "Content-Type": "application/json"
        }
        
        messages = []
        
        # Add context if provided
        if context:
            messages.append({
                "role": "system",
                "content": (
                    "You are an AI assistant that helps analyze images. "
                    "Below is the extracted content from the image including text and tables. "
                    f"Context from image:\n{context}"
                )
            })
        
        messages.append({"role": "user", "content": prompt})
        
        data = {
            "model": self.MODEL_NAME,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 2048
        }
        
        try:
            response = requests.post(self.API_URL, headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error generating response: {str(e)}"
