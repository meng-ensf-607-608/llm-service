import pytest
from unittest.mock import patch, MagicMock
from src.llm_chain import create_chain, get_model
from src.config import MODEL_TYPE_GEMINI
from src.data_models import HealthRecommendations
from src.prompt_template import template

# Test for get_model function
@patch('src.llm_chain.GoogleGenerativeAIFactory')
def test_get_model_gemini(mock_factory):
    # Mock the returned model from GoogleGenerativeAIFactory
    mock_model = MagicMock()
    mock_factory.return_value.create_model.return_value = mock_model

    # Call the function with MODEL_TYPE_GEMINI
    result = get_model(MODEL_TYPE_GEMINI)

    # Assertions to check if the correct model is returned
    mock_factory.return_value.create_model.assert_called_once()
    assert result == mock_model

# Test for create_chain function
@patch('src.llm_chain.get_model')
@patch('src.llm_chain.JsonOutputParser')
@patch('src.llm_chain.PromptTemplate')
def test_create_chain(mock_prompt_template, mock_output_parser, mock_get_model):
    # Mocking objects and their methods
    mock_model = MagicMock()
    mock_get_model.return_value = mock_model
    
    mock_parser_instance = MagicMock()
    mock_output_parser.return_value = mock_parser_instance
    mock_parser_instance.get_format_instructions.return_value = "format instructions"
    
    mock_prompt_instance = MagicMock()
    mock_prompt_template.return_value = template

    # Call the function with a valid model type
    result = create_chain(MODEL_TYPE_GEMINI)

    # Assertions to check if the chain is created correctly
    mock_get_model.assert_called_once_with(MODEL_TYPE_GEMINI)
    mock_output_parser.assert_called_once_with(pydantic_object=HealthRecommendations)
    mock_prompt_template.assert_called_once_with(
        template=mock_prompt_template.return_value,
        input_variables=["complaints", "age", "gender", "occupation", "chronic_conditions"],
        partial_variables={"format_instructions": "format instructions"}
    )
    