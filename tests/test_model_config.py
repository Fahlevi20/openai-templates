import pytest
from config.model_config import Model
def test_model_initialization():
    test_model_name="gpt-4o-mini"
    model_instance=Model(test_model_name)
    
    assert model_instance.model == test_model_name
