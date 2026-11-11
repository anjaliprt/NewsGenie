import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# The client automatically picks up the GEMINI_API_KEY environment variable.
client = genai.Client()

def ask_llm(question: str) -> str:
    try:
        # Call generation directly via the client
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        # Check for valid text response
        if response.text:
            return response.text.strip()

        return ""

    except Exception:
        # Returns an empty string if the API call fails or times out
        return ""
