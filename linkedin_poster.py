from openai import OpenAI
import json  # For saving output to a file

# Replace with your Perplexity API key
api_key = "PERPLEXITY_API"

client = OpenAI(
    api_key=api_key,
    base_url="https://api.perplexity.ai"
)

# Step 1: Let Perplexity decide a topic (e.g., trending in AI or business)
topic_messages = [
    {
        "role": "system",
        "content": "You are an AI that suggests timely, engaging topics for LinkedIn posts. Focus on professional themes like AI, business growth, or networking trends."
    },
    {
        "role": "user",
        "content": "Suggest one current, trending topic for a LinkedIn post. Keep it concise and relevant to today's date: August 14, 2025."
    }
]

topic_response = client.chat.completions.create(
    model="sonar-small-chat",  # Lightweight model for quick suggestions
    messages=topic_messages,
    max_tokens=50
)

suggested_topic = topic_response.choices[0].message.content.strip()
print(f"Suggested Topic: {suggested_topic}")

# Step 2: Generate LinkedIn post content based on the suggested topic
post_messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant that generates engaging, professional LinkedIn posts with real-time insights and citations."
    },
    {
        "role": "user",
        "content": f"Generate a LinkedIn post about '{suggested_topic}'. Make it authentic, 200-300 words, include key insights, and end with a call to action."
    }
]

post_response = client.chat.completions.create(
    model="sonar-pro",  # For detailed, high-quality content
    messages=post_messages,
    max_tokens=400
)

generated_post = post_response.choices[0].message.content
print("\nGenerated LinkedIn Post:\n")
print(generated_post)

# Optional: Save to a file for easy sharing or automation
with open("linkedin_post.json", "w") as file:
    json.dump({"topic": suggested_topic, "post": generated_post}, file)
