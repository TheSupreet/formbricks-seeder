import json
from utils.llm import generate_json

def generate():
    print("🤖 Generating realistic data with LLM...")

    surveys = generate_json("""
    Generate 5 realistic product feedback surveys.
    Each survey must have:
    - title
    - description
    - questions (array with type, text, options if needed)
    Return ONLY valid JSON.
    """)

    users = generate_json("""
    Generate 10 unique users.
    Each user:
    - name
    - email
    - role (Manager or Owner)
    Return ONLY valid JSON.
    """)

    responses = generate_json("""
    Generate 1 realistic response per survey.
    Responses should match survey questions.
    Return ONLY valid JSON.
    """)

    with open("data/surveys.json", "w") as f:
        json.dump(surveys, f, indent=2)

    with open("data/users.json", "w") as f:
        json.dump(users, f, indent=2)

    with open("data/responses.json", "w") as f:
        json.dump(responses, f, indent=2)

    print("✅ Data generated in /data")
