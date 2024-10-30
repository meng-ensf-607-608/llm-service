from abc import ABC, abstractmethod
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from src.config import GEMINI_ENV_KEY


class LLMModelFactory(ABC):
    """Abstract factory class for creating LLM model instances."""

    @abstractmethod
    def create_model(self):
        """Creates and returns an LLM model instance."""
        pass

class GoogleGenerativeAIFactory(LLMModelFactory):
    """Concrete factory for creating Google Generative AI models."""

    def __init__(self, temperature: float = 0.9):
        self.model_name = os.getenv(GEMINI_ENV_KEY)
        self.temperature = temperature

    def create_model(self):
        return ChatGoogleGenerativeAI(model=self.model_name, temperature=self.temperature)
    