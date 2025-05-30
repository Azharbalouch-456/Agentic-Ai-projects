from openai import AsyncOpenAI               # Import the AsyncOpenAI client to interact with Gemini AI asynchronously
from dotenv import load_dotenv               # Import to load environment variables from a .env file
import os                                   # Import os module to access environment variables
import asyncio                              # Import asyncio to run async functions

load_dotenv()                              # Load environment variables from a .env file into the program's environment

gemini_api_key = os.getenv("GEMINI_API_KEY")  # Get the API key stored under GEMINI_API_KEY from environment variables
print(f"API Key Loaded: {gemini_api_key}")    # Print the API key to confirm it's loaded (for debugging)

if not gemini_api_key:                     # Check if the API key is missing or empty
    raise ValueError("GEMINI_API_KEY is not set. Please set it in your .env file.")  # Raise error if API key not found

# Create an asynchronous client to communicate with Gemini AI
client = AsyncOpenAI(
    api_key=gemini_api_key,                # Provide the API key for authorization
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Set the Gemini API base URL
    timeout=30                             # Set timeout to 30 seconds to wait for responses before giving up
)

# Define an asynchronous function to send prompt to Gemini AI and get response
async def generate_text(prompt: str) -> str:
    try:
        # Send a chat completion request to the Gemini AI with the given prompt
        response = await client.chat.completions.create(
            model="gemini-2.0-flash",      # Specify the AI model to use
            messages=[{"role": "user", "content": prompt}],  # Pass the prompt as a user message
        )
        # Extract and return the generated text from the response
        return response.choices[0].message.content
    except Exception as e:                  # Catch any exceptions during the request
        print(f"Error during API call: {e}")  # Print the error message for debugging
        return ""                          # Return empty string if there was an error

# Define the main async function to run the example
async def main():
    # This is the prompt sent to Gemini AI to translate English to Sindhi
    prompt = "Translate this English text to Sindhi: Hello, how are you?"
    
    # Call generate_text() to get AI response for the prompt
    result = await generate_text(prompt)
    
    # Print the translated text from Gemini AI
    print("Response from API:\n", result)

# Run the main function if this script is executed directly (not imported)
if __name__ == "__main__":
    asyncio.run(main())     

    # Use asyncio to run the async main() function
