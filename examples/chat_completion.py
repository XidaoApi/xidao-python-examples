from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["XIDAO_API_KEY"],
    base_url="https://api.xidao.online/v1"
)

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short product update announcement for an AI app."}
    ]
)

print(response.choices[0].message.content)
