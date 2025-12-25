from openai import OpenAI
from utils.config import OPENAI_API_KEY
import json

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_json(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return json.loads(response.choices[0].message.content)
