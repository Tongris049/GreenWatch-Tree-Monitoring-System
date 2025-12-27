import urllib.request
import json

# 🔐 My KoBo API Token
API_TOKEN = "7cfed601a647c0b72f46045922c1f71a1430d7d2"

# 🆔 My Form (Asset) ID
FORM_ID = "a2eKp7YQ4GXDF88d8fekhh"

# 🌍 KoBo API URL
url = f"https://kf.kobotoolbox.org/api/v2/assets/{FORM_ID}/data/"

# 📡 Prepare request
request = urllib.request.Request(url)
request.add_header("Authorization", f"Token {API_TOKEN}")

try:
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode())
        print("✅ Connection successful!")
        print("Total submissions:", len(data.get("results", [])))

except Exception as e:
    print("❌ Error connecting to KoBo:")
    print(e)
  

print(f"Total submissions: {len(data['results'])}")



print("\n🔍 INSPECTING FIRST SUBMISSION:\n")

if data["results"]:
    first = data["results"][0]
    for key, value in first.items():
        print(f"{key}: {value}")
else:
    print("No submissions found.")


print("\n📊 FIELD PRESENCE CHECK (first submission):\n")

required_fields = [
    "Tree_ID",
    "Planting_Entity_Type",
    "Local_Government_Area_LGA",
    "Community_Village",
    "Tree_Species",
    "GPS_Coordinates",
    "_geolocation",
    "Tree_Condition_at_time_of_capture"
]

for field in required_fields:
    print(f"{field}: {'✅' if field in first else '❌'}")



print("\n🧪 VALUE QUALITY CHECK:\n")

print("Tree ID:", first["Tree_ID"])
print("Entity Type:", first["Planting_Entity_Type"])
print("NGO Name:", first.get("Please_specify_the_NGO_name"))
print("LGA:", first["Local_Government_Area_LGA"])
print("Village:", first["Community_Village"])
print("Tree Species:", first.get("Please_specify_the_Tree_species"))
print("Tree Condition:", first["Tree_Condition_at_time_of_capture"])
print("Latitude:", first["_geolocation"][0])
print("Longitude:", first["_geolocation"][1])
