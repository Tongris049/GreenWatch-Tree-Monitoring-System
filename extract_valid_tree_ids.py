import json

# Input: Form A raw data
INPUT_FILE = "data/raw/formA_submissions.json"

# Output: Valid Tree IDs reference
OUTPUT_FILE = "data/valid_tree_ids.json"

# Load Form A data
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract Tree_IDs
tree_ids = []

for record in data.get("results", []):
    tree_id = record.get("Tree_ID")
    if tree_id:
        tree_ids.append(tree_id)

# Save Tree IDs
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(tree_ids, f, indent=2)

print("✅ Tree ID extraction complete")
print(f"🌳 Total valid Tree IDs: {len(tree_ids)}")
print(f"📁 Saved to: {OUTPUT_FILE}")
