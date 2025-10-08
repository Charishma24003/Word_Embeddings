import unicodedata

def normalize(text):
    return unicodedata.normalize("NFC", text)

unique_lines = set()
with open("kn_cleaned_fake.txt", "r", encoding="utf-8") as f:
    for line in f:
        unique_lines.add(normalize(line.strip()))

with open("kn_final_fake.txt", "w", encoding="utf-8") as f:
    for line in unique_lines:
        f.write(line + "\n")

print("✅ Normalized and deduplicated — saved to kn_final.txt")
