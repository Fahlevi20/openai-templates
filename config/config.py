from openai import OpenAI
from model_config import Model
import os
from chat.chat import chat_message

model_name= os.environ.get("MODEL_NAME")
api_key = os.environ.get("API_KEY")
organization_id=os.environ.get("ORGANIZATION_ID")

def model_configuration():
    client = OpenAI(api_key=api_key)
    completion= client.chat.completions.create(
        model=Model(model_name),
        messages=chat_message
    )
    
    return client.choices[0].messages