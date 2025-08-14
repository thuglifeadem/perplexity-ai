from openai import OpenAI

# Replace with your Perplexity API key
api_key = "YOUR_PERPLEXITY_API_KEY"

client = OpenAI(
    api_key=api_key,
    base_url="https://api.perplexity.ai"
)

# Example query to generate LinkedIn post content
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant that generates engaging LinkedIn posts."
    },
    {
        "role": "user",
        "content": "Generate a LinkedIn post about the benefits of AI in professional networking, including real-time insights and citations."
    }
]

response = client.chat.completions.create(
    model="sonar-pro",  # Use 'sonar-small' for simpler queries
    messages=messages,
    max_tokens=300  # Adjust for post length
)

generated_post = response.choices[0].message.content
print(generated_post)
