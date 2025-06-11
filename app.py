import os
import google.generativeai as genai
from dotenv import load_dotenv


# Step 1: Configure Gemini API key (make sure it's stored as an environment variable)

load_dotenv()   # This must be called before using os.getenv

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



# Step 2: Get user input
user_input = input("Where would you like to fly? ")



# Step 3: Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")



# Step 4: Generate a response using Gemini
prompt = f"You are a helpful flight booking assistant. A user wants to fly to {user_input}. Respond appropriately."
response = model.generate_content(prompt)



# Step 5: Display the response
print(response.text.strip())
