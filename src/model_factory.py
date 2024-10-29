from abc import ABC, abstractmethod
from langchain_google_genai import ChatGoogleGenerativeAI

class LLMModelFactory(ABC):
    """Abstract factory class for creating LLM model instances."""

    @abstractmethod
    def create_model(self):
        """Creates and returns an LLM model instance."""
        pass

class GoogleGenerativeAIFactory(LLMModelFactory):
    """Concrete factory for creating Google Generative AI models."""

    def __init__(self, model_name: str, temperature: float = 0.9):
        self.model_name = model_name
        self.temperature = temperature

    def create_model(self):
        return ChatGoogleGenerativeAI(model=self.model_name, temperature=self.temperature)
    