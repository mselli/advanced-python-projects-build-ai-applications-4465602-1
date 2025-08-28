from textblob import TextBlob

class Chatbot:

    def __init__(self):
    # Define intents and their corresponding responses based on keywords
        self.intents = {
            "hours":{
                "keywords": ["hours", "open", "close"],
                "response": "We are open from 9AM to 5PM, Monday to Friday."
            },
            "return":{
                "keywords":["refund", "money back", "return"],
                "response": "I'd be happy to help you with the return process. Let me transfer you to a live agent."
            }
        }
    

    def get_response(self, message):

        # Convert the message to lowercase for consistent keyword matching
        message = message.lower()

        # Check if the message contains any keywords associated with defined intents
        for intent in self.intents.values():
            if any(word in message for word in intent["keywords"]):
                return intent["response"]
        
        # Analyze the sentiment of the message using TextBlob
        sentiment = TextBlob(message).sentiment.polarity
        
        # Return a response based on the sentiment score
        return ("That's great to hear!" if sentiment > 0 else
            "I'm sorry to hear that. How can I help?" if sentiment < 0 else
            "I see. Can you tell me more about that?")

# Greet the user and prompt for input
    def chat(self):    
        print("Chatbot: Hi, how can I help you today?")
        # Continuously prompt the user for input until they choose to exit
        while(user_message := input("You: ").strip().lower()) not in ["exit", "quit", "bye"]:
            print(f"\n Chatbot: {self.get_response(user_message)}")
        # Thank the user for chatting when they exit

        print("Chatbot: Thank you for chatting, have a great day")
        

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()  # Start the chat when the script is executed
