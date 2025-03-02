from openai import OpenAI
from .model_config import Model
import os
from chat.chat import chat_message
from dotenv import load_dotenv
load_dotenv()

model_name= os.environ.get("MODEL_NAME")
organization_id=os.environ.get("ORGANIZATION_ID")
api_key = os.getenv("OPENAI_API_KEY")  # Correct environment variable name
print(api_key)
if not api_key:
    raise ValueError("API Key is missing! Set the OPENAI_API_KEY environment variable.")

def model_configuration(prompt):
    client = OpenAI(api_key=api_key)
    completion= client.chat.completions.create(
        model=Model(model_name).model,
        messages=chat_message(prompt)
    )
    print(completion)
    return completion.choices[0].message.content