

from ..registry import register

from .openai import OpenAIProvider
from .openrouter import OpenRouterProvider
from .groq import GroqProvider
from .deepseek import DeepSeekProvider
from .together import TogetherProvider
from .mistral import MistralProvider
from .ollama import OllamaProvider
from .gemini import GeminiProvider
from .huggingface import HuggingFaceProvider

register("openai", OpenAIProvider)
register("openrouter", OpenRouterProvider)
register("groq", GroqProvider)
register("deepseek", DeepSeekProvider)
register("together", TogetherProvider)
register("mistral", MistralProvider)
register("ollama", OllamaProvider)
register("gemini", GeminiProvider)
register("huggingface", HuggingFaceProvider)