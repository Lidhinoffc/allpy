from google import genai

from ..config import (
    api_key,
    model,
)

from ..exceptions import APIKeyMissing


class GeminiProvider:

    def __init__(self):

        key = api_key()

        if not key:
            raise APIKeyMissing()

        self.client = genai.Client(
            api_key=key
        )

    def chat(
        self,
        prompt,
        **kwargs,
    ):

        response = self.client.models.generate_content(
            model=model() or "gemini-2.5-flash",
            contents=prompt,
        )

        return response.text