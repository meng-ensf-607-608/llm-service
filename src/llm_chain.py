from langchain_core.output_parsers import JsonOutputParser
from src.data_models import HealthRecommendations, PatientInput
from src.prompt_template import template
from src.model_factory import GoogleGenerativeAIFactory
from src.config import MODEL_TYPE_GEMINI
from langchain_core.prompts import PromptTemplate


def create_chain(model_type):
    model = get_model(model_type)
    output_parser = JsonOutputParser(pydantic_object=HealthRecommendations)
    prompt = PromptTemplate(template=template,
                            input_variables=["complaints", "age", "gender","occupation", "chronic_conditions"],
                            partial_variables={"format_instructions": output_parser.get_format_instructions()}
                            )
    return prompt | model | output_parser

def get_model(type: str):
    match type:
        case MODEL_TYPE_GEMINI:
            return GoogleGenerativeAIFactory().create_model()
