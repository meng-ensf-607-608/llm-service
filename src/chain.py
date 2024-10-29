from langchain_core.output_parsers import JsonOutputParser
from src.data_models import HealthRecommendations
from src.prompt import create_prompt
from src.prompt_template import template
from src.model_factory import LLMModelFactory
import os
from src.model_factory import GoogleGenerativeAIFactory


def create_chain(model_name):
    model_factory: LLMModelFactory = GoogleGenerativeAIFactory(model_name)
    output_parser = JsonOutputParser(pydantic_object=HealthRecommendations)
    model = model_factory.create_model()
    prompt = create_prompt(template)
    return prompt | model | output_parser

