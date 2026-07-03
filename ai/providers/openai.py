from openai import OpenAI

from ..config import (
    api_key,
    base_url,
    model,
)

from ..exceptions import APIKeyMissing


class OpenAIProvider:

    def __init__(self):

        key = api_key()

        if not key:
            raise APIKeyMissing(
                "API key not configured."
            )

        kwargs = {
            "api_key": key
        }

        if base_url():
            kwargs["base_url"] = base_url()

        self.client = OpenAI(**kwargs)

    def chat(
        self,
        prompt,
        **kwargs,
    ):

        response = self.client.chat.completions.create(

            model=model() or "gpt-4.1-mini",

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            **kwargs
        )

        return response.choices[0].message.content