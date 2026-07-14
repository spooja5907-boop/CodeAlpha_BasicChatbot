def chatbot():
    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("Bot: Hi, how can I help you?")
        elif message == "how are you":
            print("Bot: I'm fine, thanks!")
        elif message == "bye":
            print("Bot: Goodbye!")
            break
        elif message == "hi":
            print("Bot: Good morning! Keep smiling.")
        elif message == "thank you":
            print("Bot: You're welcome!")
        elif message == "what can you do":
            print("Bot: I can help you with simple predefined questions.")
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
