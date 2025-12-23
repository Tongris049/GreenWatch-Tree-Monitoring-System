import urllib.request
import json

# 🔐 Your KoBo API Token
API_TOKEN = "7cfed601a647c0b72f46045922c1f71a1430d7d2"

# 🆔 Your Form (Asset) ID
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
  

