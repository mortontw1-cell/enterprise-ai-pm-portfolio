"""
PCC Checkpoint: Dictionaries, Functions, and JSON Data Structures.
Simulates parsing structured output from an AI model.
"""

import json

# 1. Define a function that processes an AI project scope payload
def parse_project_estimate(raw_data: dict) -> dict:
    project_name = raw_data.get("project_name", "Untitled Project")
    estimated_hours = raw_data.get("hours", 0)
    hourly_rate = raw_data.get("rate", 0.0)
    
    total_cost = estimated_hours * hourly_rate
    
    return {
        "project_name": project_name,
        "estimated_hours": estimated_hours,
        "hourly_rate": hourly_rate,
        "total_cost": total_cost,
        "status": "Scope Validated" if total_cost > 0 else "Pending Review"
    }

# 2. Mock JSON response from Gemini / AI Studio
gemini_mock_response = '''
{
    "project_name": "Commercial Turf Weed Control & Overseeding",
    "hours": 18,
    "rate": 125.00,
    "materials": ["Triad QC Herbicide", "Kentucky Bluegrass Blend"]
}
'''

# 3. Convert JSON string to Python dictionary
parsed_json_dict = json.loads(gemini_mock_response)

# 4. Process and print results
summary = parse_project_estimate(parsed_json_dict)

print("--- Extracted Project Summary ---")
for key, value in summary.items():
    print(f"{key.replace('_', ' ').title()}: {value}")