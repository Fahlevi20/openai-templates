from chat.chat import chat_message

from config.config import model_configuration


def main():
    user_input=input("Your Message:")
    
    response=model_configuration(user_input)
    
    print(response)
    

if __name__ == "__main__":
    main()