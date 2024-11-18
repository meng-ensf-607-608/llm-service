from langchain_core.output_parsers import JsonOutputParser
from src.data_models import HealthRecommendation, PatientInput
from src.prompt_template import template
from src.model_factory import GoogleGenerativeAIFactory
from src.config import MODEL_TYPE_GEMINI
from langchain_core.prompts import PromptTemplate
from src.logger import get_logger

logger = get_logger(__name__)

def create_chain(model_type):
    model = get_model(model_type)
    output_parser = JsonOutputParser(pydantic_object=HealthRecommendation)
    prompt = PromptTemplate(template=template,
                            input_variables=["complaints", "age", "gender","occupation", "chronic_conditions"],
                            partial_variables={"format_instructions": output_parser.get_format_instructions()}
                            )
    logger.debug("------- prompt -----")
    logger.debug(prompt)
    logger.debug("----------------------")
    return prompt | model | output_parser

def get_model(type: str):
    logger.debug("Model type: {type}")
    match type:
        case MODEL_TYPE_GEMINI:
            return GoogleGenerativeAIFactory().create_model()
