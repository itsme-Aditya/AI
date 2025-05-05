import datetime

def simple_restaurant_chatbot():
    print("Welcome to my Restaurant Chatbot!")
    print("Ask me about: menu, price, contact, reservation, hours, or type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Thanks for visiting! Have a great day!")
            break

        elif "menu" in user_input:
            print("Chatbot: We serve pasta, pizza, salads, and desserts.")

        elif "price" in user_input or "cost" in user_input:
            print("Chatbot: The average cost per person is about Rs. 1500.")

        elif "contact" in user_input or "phone" in user_input:
            print("Chatbot: You can reach us at +91 1234567890.")

        elif "reservation" in user_input or "book" in user_input:
            print("Chatbot: To reserve a table, call us or book online at https://myresturant.com")

        elif "hours" in user_input or "open" in user_input:
            print("Chatbot: We're open daily from 11 AM to 10 PM.")

        elif "time" in user_input or "date" in user_input:
            now = datetime.datetime.now()
            print(f"Chatbot: Current date and time is {now.strftime('%y-%m-%d %I:%M %p')}.")

        else:
            print("Chatbot: Sorry, I didn't get that. Please ask about menu, price, contact, reservation, or hours.")


simple_restaurant_chatbot()
