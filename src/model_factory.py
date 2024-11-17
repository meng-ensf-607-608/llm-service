from abc import ABC, abstractmethod
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from src.logger import get_logger

logger = get_logger(__name__)

from src.config import GEMINI_ENV_KEY, MODEL_TEMPERATURE_ENV_KEY


class LLMModelFactory(ABC):
    """Abstract factory class for creating LLM model instances."""

    @abstractmethod
    def create_model(self):
        """Creates and returns an LLM model instance."""
        pass

class GoogleGenerativeAIFactory(LLMModelFactory):
    """Concrete factory for creating Google Generative AI models."""

    def __init__(self):
        self.model_name = os.getenv(GEMINI_ENV_KEY)
        self.temperature = float(os.getenv(MODEL_TEMPERATURE_ENV_KEY, 0))

    def create_model(self):
        logger.debug("Model: {self.model_name}")
        logger.debug("Model Temperature: {self.temperature}")
        return ChatGoogleGenerativeAI(model=self.model_name, temperature=self.temperature)
    