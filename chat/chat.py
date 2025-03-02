def chat_message(prompt):
    messages = [
        {'role': "system",
         "content": "You are a helpful assistant."
         },
        
        {'role':"user",
         "content":prompt,
         }
        
    ]

    return messages    
    