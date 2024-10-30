import os
import pytest
from unittest.mock import patch
from src.model_factory import GoogleGenerativeAIFactory
from pydantic import ValidationError

# Test case 1: Test create_model with mocked environment variables
def test_create_model_with_env_vars(mocker):
    # Mock environment variables
    mocker.patch.dict(os.environ, {
        'GOOGLE_LLM_MODEL': 'test-model',
        'MODEL_TEMPERATURE': '0.7'
    })
    
    # Mock ChatGoogleGenerativeAI class
    mock_chat_model = mocker.patch('src.model_factory.ChatGoogleGenerativeAI')
    
    factory = GoogleGenerativeAIFactory()
    model = factory.create_model()
    
    mock_chat_model.assert_called_once_with(model='test-model', temperature=0.7)
    assert model == mock_chat_model.return_value

# Test case 2: Test create_model with default temperature when MODEL_TEMPERATURE is not set
def test_create_model_with_default_temperature(mocker):
    mocker.patch.dict(os.environ, {
        'GOOGLE_LLM_MODEL': 'test-model'
    }, clear=True)
    
    # Mock ChatGoogleGenerativeAI class
    mock_chat_model = mocker.patch('src.model_factory.ChatGoogleGenerativeAI')

    factory = GoogleGenerativeAIFactory()
    model = factory.create_model()
    
    mock_chat_model.assert_called_once_with(model='test-model', temperature=0.0)
    assert model == mock_chat_model.return_value

# Test case 3: Test create_model when GOOGLE_LLM_MODEL is missing (should raise a pydantic Validation error)
def test_create_model_missing_gemini_key(mocker):
   
    mocker.patch.dict(os.environ, {}, clear=True)
    
    with pytest.raises(ValidationError):  # Assuming TypeError would be raised if key is missing.
        factory = GoogleGenerativeAIFactory()
        factory.create_model()
