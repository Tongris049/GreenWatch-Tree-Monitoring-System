import urllib.request
import json
import os

# =========================
# CONFIGURATION
# =========================
API_TOKEN = "7cfed601a647c0b72f46045922c1f71a1430d7d2"
FORM_B_ID = "abYn8qRZBQCJhsN7Abtugn"

FORM_B_URL = f"https://kf.kobotoolbox.org/api/v2/assets/{FORM_B_ID}/data/"

VALID_IDS_FILE = "data/valid_tree_ids.json"

OUTPUT_VALID = "data/processed/formB_valid.json"
OUTPUT_INVALID = "data/processed/formB_invalid.json"

# =========================
# ENSURE OUTPUT FOLDERS EXIST
# =========================
os.makedirs("data/processed", exist_ok=True)

# =========================
# FETCH FORM B DATA
# =========================
headers = {
    "Authorization": f"Token {API_TOKEN}"
}

req = urllib.request.Request(FORM_B_URL, headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        formB_data = json.loads(response.read())
except Exception as e:
    print("❌ Failed to fetch Form B data")
    print(e)
    exit()

# =========================
# LOAD VALID TREE IDS (FROM FORM A)
# =========================
try:
    with open(VALID_IDS_FILE, "r", encoding="utf-8") as f:
        valid_tree_ids = json.load(f)
except Exception as e:
    print("❌ Failed to load valid Tree IDs")
    print(e)
    exit()

# =========================
# VALIDATION LOGIC
# =========================
valid_records = []
invalid_records = []

for record in formB_data.get("results", []):

    # ---- GPS PRESENCE CHECK ----
    gps = record.get("GPS_Coordinates") or record.get("_geolocation")
    if not gps:
        record["_validation_reason"] = "Missing GPS coordinates"
        invalid_records.append(record)
        continue

    # ---- TREE ID CHECK ----
    tree_id = record.get("Tree_ID")
    if not tree_id:
        record["_validation_reason"] = "Missing Tree_ID"
        invalid_records.append(record)
        continue

    if tree_id in valid_tree_ids:
        valid_records.append(record)
    else:
        record["_validation_reason"] = "Tree_ID not found in Form A"
        invalid_records.append(record)

# =========================
# SAVE RESULTS
# =========================
with open(OUTPUT_VALID, "w", encoding="utf-8") as f:
    json.dump(valid_records, f, indent=2)

with open(OUTPUT_INVALID, "w", encoding="utf-8") as f:
    json.dump(invalid_records, f, indent=2)

# =========================
# SUMMARY OUTPUT
# =========================
print("🔎 FORM B VALIDATION COMPLETE")
print(f"📊 Total Form B submissions: {len(formB_data.get('results', []))}")
print(f"✅ Valid records: {len(valid_records)}")
print(f"❌ Invalid records: {len(invalid_records)}")

if invalid_records:
    print("⚠️ Invalid record reasons:")
    for rec in invalid_records:
        print(
            "-",
            rec.get("Tree_ID", "UNKNOWN"),
            "|",
            rec.get("_validation_reason")
        )

print("📁 Outputs saved:")
print(" -", OUTPUT_VALID)
print(" -", OUTPUT_INVALID)
