from openai import OpenAI
from model_config import Model
import os

model_name= os.environ.get("MODEL_NAME")

client = OpenAI()
completion= client.chat.completions.create(
    model=Model(model_name)
)