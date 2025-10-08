# train_word2vec.py

# Step 1: Load and tokenize
with open("kn_final.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
tokenized_sentences = [line.strip().split() for line in lines]

print("Number of sentences:", len(tokenized_sentences))
print("Example tokenized sentence:", tokenized_sentences[0])

# Step 2: Train Word2Vec
from gensim.models import Word2Vec

model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,
    window=5,
    min_count=2,
    sg=1,
    workers=4
)

# Step 3: Save model and vectors
model.save("kannada_word2vec.model")
model.wv.save_word2vec_format("kannada_word_vectors.txt")

# Step 4: Inspect vocabulary and test
print("Vocabulary size:", len(model.wv))
print("Sample words:", list(model.wv.index_to_key)[:20])

word = "ಶಾಲೆ"  # replace with a word from your corpus
if word in model.wv:
    print("Vector for 'ಶಾಲೆ':", model.wv[word])
    print("Most similar words:", model.wv.most_similar(word, topn=5))
else:
    print(f"'{word}' not found in vocabulary")
