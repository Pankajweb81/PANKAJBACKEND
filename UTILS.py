import json

# Load internship dataset from JSON file
def load_dataset(filepath="backend/data.json"):
    with open(filepath, "r") as file:
        return json.load(file)

# Filter internships by location
def filter_by_location(data, location):
    return [
        item for item in data
        if location.lower() in item["location"].lower()
    ]

# Filter internships by skill
def filter_by_skill(data, skill):
    return [
        item for item in data
        if any(skill.lower() in s.lower() for s in item["skills_required"])
    ]

# Format final recommendations for output
def format_recommendations(data, limit=5):
    return [
        {
            "title": item["title"],
            "description": item["description"],
            "location": item["location"],
            "skills_required": item["skills_required"]
        }
        for item in data[:limit]
    ]
