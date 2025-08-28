# first install " pip install requirements.txt"

import logging
import os
from dotenv import load_dotenv
import google.generativeai as genai                             #first install "pip install google-generativeai"

# setup logging for the web app to capture errors and info
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

# Load environment variables from .env file
try:
    load_dotenv()
    logging.info("Loaded environment variables from .env file.")
except Exception as e:
    logging.error(f"Error loading .env file: {e}")


# Congigure google generative AI API
try:
    api_key=os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logging.error(" GOOGLE_API_KEY not found in environment variables.")
    else:
        genai.configure(api_key=api_key)
        logging.info("Google Generative AI API Configured.")
except Exception as e:
    logging.error(f"Error configuring Google Generative AI API: {e}")

def get_gemini_response(user_message):
    try:
        # Make the prompt force Gemini to be short and simple
        prompt = f"Reply in one or two short, simple sentences: {user_message}"

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            reply = response.text.strip()
        else:
            reply = "Sorry, I couldn't process that."

        logging.info(f"Gemini response: {reply}")
        return reply

    except Exception as e:
        logging.error(f"Error in get_gemini_response(): {e}")
        return "Sorry, I couldn't process that."

    
    