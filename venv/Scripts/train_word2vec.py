from gensim.models import Word2Vec

# Replace this with your tokenized Kannada sentences
sentences = [
    ['ನಾನು', 'ಶಾಲೆಗೆ', 'ಹೋಗುತ್ತಿದ್ದೇನೆ'],
    ['ಅವಳು', 'ಪಾಠಶಾಲೆಯಲ್ಲಿ', 'ಕಲಿಯುತ್ತಾಳೆ'],
    ['ಅವನಿಗೆ', 'ಪುಸ್ತಕ', 'ಇಷ್ಟವಾಗಿದೆ']
]

# Train Word2Vec model
model = Word2Vec(
    sentences=sentences,
    vector_size=100,  # Dimension of word vectors
    window=5,         # Context window
    min_count=1,      # Ignores words with frequency < 1
    sg=1,             # 1=skip-gram, 0=CBOW
    workers=4         # Number of CPU threads
)

# Save model for later use
model.save("kannada_word2vec.model")
model.wv.save_word2vec_format("kannada_word_vectors.txt")

# Example: get vector for a word
print("Vector for 'ಶಾಲೆ':", model.wv['ಶಾಲೆ'])

# Example: most similar words
print("Most similar to 'ಶಾಲೆ':", model.wv.most_similar('ಶಾಲೆ', topn=5))
