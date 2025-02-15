from openai import OpenAI
from model_config import Model
import pytest
import unittest.mock import patch, MagicMock
import os

@pytest.fixture
def mock_env():
    with patch.dict(os.environ, {"MODEL_NAME":"test_model"}):
        yield
    
model_name= os.environ.get("MODEL_NAME")

client = OpenAI()
completion= client.chat.completions.create(
    model=Model(model_name)
)