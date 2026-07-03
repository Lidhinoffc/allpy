from huggingface_hub import InferenceClient

from ..config import (
    api_key,
    model,
)


class HuggingFaceProvider:

    def __init__(self):

        self.client = InferenceClient(
            api_key=api_key()
        )

    def chat(
        self,
        prompt,
        **kwargs,
    ):

        response = self.client.chat_completion(

            model=model(),

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content