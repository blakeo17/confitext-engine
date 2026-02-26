import json
import openai
import os

with open("data/metrics.json", "r") as f:
    data = json.load(f)

if not data:
    print("No data found.")
    exit()

# Pick top video by Views
top_video = max(data, key=lambda x: int(x["Views"]))

print("\nTop Performing Video:\n")
print(f"Angle: {top_video['Angle']}")
print(f"Hook: {top_video['Hook']}")
print(f"Views: {top_video['Views']}")
print(f"Avg Watch: {top_video['Avg_Watch']}%")
print(f"Saves: {top_video['Saves']}")
print(f"Follows: {top_video['Follows']}")

print("\nGenerating next week content...\n")

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = f"""
The top performing short-form video had:

Angle: {top_video['Angle']}
Hook: {top_video['Hook']}
Views: {top_video['Views']}
Avg Watch: {top_video['Avg_Watch']}%
Saves: {top_video['Saves']}
Follows: {top_video['Follows']}

Based on this, create a simple Next Week Content Plan.
Give 3 new video ideas.
Each should include:
- Angle
- Hook
- Short concept description
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
