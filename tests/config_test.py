from openai import OpenAI
from config.model_config import Model
import pytest
from unittest.mock import patch, MagicMock
import os

@pytest.fixture
def mock_env():
    with patch.dict(os.environ, {"MODEL_NAME":"test_model"}):
        yield

@pytest.fixture
def mock_openai():
    with patch("openai.OpenAI") as mock_client:
        mock_instance=MagicMock()
        mock_client.return_value=mock_instance
        mock_instance.chat.completions.create.return_value={"response":"test"}
        yield mock_instance

@pytest.fixture
def test_openai(mock_env,mock_openai):
    
    model_name= os.environ.get("MODEL_NAME")

    client = OpenAI()
    completion= client.chat.completions.create(
        model=Model(model_name)
)
    
    mock_openai.chat.completions.create.assert_called_once_with(model=Model("test_model"))
    
    assert completion == {"response":"test"}