input_file = "kn.txt"
output_file = "kn_sample_fake.txt"
num_lines = 5000 # you can adjust this (10k, 100k, etc.)

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for i, line in enumerate(infile):
        if i >= num_lines:
            break
        outfile.write(line)
print(f"✅ Sample of {num_lines} lines saved to {output_file}")
