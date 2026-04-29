from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["XIDAO_API_KEY"],
    base_url="https://api.xidao.online/v1"
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="XiDao API provides lower-cost OpenAI-compatible access for developers."
)

print(len(response.data[0].embedding))
