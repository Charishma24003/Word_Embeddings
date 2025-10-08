import re

def clean_kannada_text(text):
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    # Remove English letters and digits
    text = re.sub(r'[A-Za-z0-9]', '', text)
    # Keep only Kannada characters and common punctuation
    text = re.sub(r'[^\u0C80-\u0CFF\s.,!?]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()
    return text

input_file = "kn_sample_fake.txt"
output_file = "kn_cleaned_fake.txt"

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        cleaned = clean_kannada_text(line)
        if cleaned:
            outfile.write(cleaned + '\n')

print("✅ Cleaning complete — saved to kannada_cleaned.txt")
