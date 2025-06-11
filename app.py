import os
import google.generativeai as genai
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Define the booking assistant function
def flight_booking(location):
    if not location:
        return "Please enter a valid destination."
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"You are a helpful flight booking assistant. A user wants to fly to {location}. Respond appropriately."
    response = model.generate_content(prompt)
    return response.text.strip()

# Get user input
user_input = input("Where would you like to fly? ")


# Call the function and print the response
print(flight_booking(user_input))
