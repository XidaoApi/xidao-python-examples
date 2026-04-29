from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["XIDAO_API_KEY"],
    base_url="https://api.xidao.online/v1"
)

messages = [
    {"role": "system", "content": "Summarize support tickets in 3 concise bullet points."},
    {"role": "user", "content": "Customer reports slower than expected AI response times during peak hours and wants a workaround until a permanent fix is deployed."}
]

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=messages,
    temperature=0.2,
)

print("Estimated optimization notes:")
print("- Use a smaller model for first-pass summaries")
print("- Keep prompts short and structured")
print("- Route only difficult cases to stronger models")
print("\nModel output:\n")
print(response.choices[0].message.content)
