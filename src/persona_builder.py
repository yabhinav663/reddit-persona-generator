import os
from openai import Client
from dotenv import load_dotenv

# Load .env file for API key
load_dotenv()
print("OpenAI Key Prefix:", os.getenv("OPENAI_API_KEY")[:8])

# Create OpenAI client using correct class
client = Client(api_key="sk-5aJkV7B9m2o1G5y0Y7E91UJPQsJMdjU23xwNED8KlUhzBt0E")
client = Client(api_key="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 ")

def generate_persona(user_data):
    prompt = f"""
You are an AI assistant that creates detailed user personas.
Use the following Reddit posts and comments to generate a persona for the user '{user_data['username']}'.

Include:
- Personality traits
- Interests
- Communication style
- Possible profession

For each trait, cite the specific post or comment that supports your conclusion.

Posts:
{user_data['posts']}

Comments:
{user_data['comments']}

Persona:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content
