import openai
import time
from config import Config
cfg = Config()

openai.api_key = cfg.openai_api_key

# Overly simple abstraction until we create something better
def create_chat_completion(messages, model=None, temperature=None, max_tokens=None)->str:
    # Make the request to the OpenAI API and handle potential errors
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
    except openai.error.APIError as e:
        print(f"Encountered API error: {e}")
        print("Retrying in 10 seconds...")
        time.sleep(10)  # Wait for 10 seconds
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

    return response.choices[0].message["content"]

