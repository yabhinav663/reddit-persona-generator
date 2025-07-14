# reddit-persona-generator/src/main.py
import os
import sys
sys.path.append(os.path.dirname(__file__))
from reddit_scraper import fetch_user_data
from persona_builder import generate_persona
from utils import save_to_file, extract_username


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <reddit_user_profile_url>")
        return

    profile_url = sys.argv[1]
    username = extract_username(profile_url)

    print(f"Fetching data for user: {username}")
    user_data = fetch_user_data(username)

    print("Generating user persona...")
    persona_text = generate_persona(user_data)

    print("Generated Persona Text Preview:")
    print(persona_text[:500])

    save_to_file(f"../data/{username}_persona.txt", persona_text)
    print(f"Persona saved to data/{username}_persona.txt")

if __name__ == "__main__":
    main()


