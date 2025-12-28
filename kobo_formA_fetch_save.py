import os
import json
import urllib.request
import urllib.error

# =========================
# CONFIGURATION 
# =========================
API_TOKEN = "7cfed601a647c0b72f46045922c1f71a1430d7d2"
FORM_ID = "a2eKp7YQ4GXDF88d8fekhh"

# =========================
# PATH SETUP
# =========================
DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(DATA_DIR, "formA_submissions.json")

# =========================
# KOBO API REQUEST
# =========================
url = f"https://kf.kobotoolbox.org/api/v2/assets/{FORM_ID}/data/"

request = urllib.request.Request(url)
request.add_header("Authorization", f"Token {API_TOKEN}")

try:
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))

    # =========================
    # SAVE DATA
    # =========================
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("✅ Form A data fetched successfully")
    print(f"📁 Saved to: {OUTPUT_FILE}")
    print(f"📊 Total submissions: {len(data.get('results', []))}")

except urllib.error.HTTPError as e:
    print("❌ HTTP Error:", e.code)
    print(e.read().decode())

except Exception as e:
    print("❌ Unexpected error:")
    print(e)
