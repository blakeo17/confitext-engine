import json

with open("data/metrics.json", "r") as f:
    data = json.load(f)

if not data:
    print("No data found.")
    exit()

top_video = max(data, key=lambda x: x["Views"])

print("\nTop Performing Video:\n")
print(f"Angle: {top_video['Angle']}")
print(f"Hook: {top_video['Hook']}")
print(f"Views: {top_video['Views']}")
print(f"Retention: {top_video['3s_Retention']}%")
print(f"Avg Watch: {top_video['Avg_Watch']}%")
print(f"Saves: {top_video['Saves']}")
print(f"Shares: {top_video['Shares']}")
print(f"Comments: {top_video['Comments']}")
print(f"Follows: {top_video['Follows']}")

