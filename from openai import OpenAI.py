from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise SystemExit("Set OPENAI_API_KEY environment variable before running.")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5-nano",
    input="write a haiku about ai",
    store=True,
)

print(response.output_text)
