def chat_message(prompt):
    prompt=input()
    messages = [
        {'role': "system",
         "content": "You are a helpful assistant."
         },
        
        {'role':"user",
         "content":prompt,
         }
        
    ]
    
    