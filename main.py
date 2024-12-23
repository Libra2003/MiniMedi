import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the .env.local file
load_dotenv('.env')
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

print("Gemini Chatbot: Hello! How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Gemini Chatbot: Goodbye!")
        break

    response = chat_session.send_message(user_input)
    print(f"Gemini Chatbot: {response.text}")