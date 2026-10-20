import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  base_url="https://api.groq.com/openai/v1",
  api_key=os.environ.get("GROQ_API_KEY"),
)

completion = client.chat.completions.create(
  messages=[
    {
        "role": "user",
        "content": "You are a professional travel guide."
    },
    {
      "role": "user",
      "content": "What are the best places to visit in Bangalore?"
    }
  ],
  model="qwen/qwen3.8-27b",
)

print(completion.choices[0].message)