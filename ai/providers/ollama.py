from ollama import Client

from ..config import (
    base_url,
    model,
)


class OllamaProvider:

    def __init__(self):

        self.client = Client(
            host=base_url() or "http://localhost:11434"
        )

    def chat(
        self,
        prompt,
        **kwargs,
    ):

        response = self.client.chat(

            model=model() or "llama3",

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]