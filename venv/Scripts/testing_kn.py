from gensim.models import Word2Vec

# Load your trained model
model = Word2Vec.load("kannada_word2vec.model")

# Find most similar words
similar_words = model.wv.most_similar('ಶಾಲೆ', topn=10)
print("Most similar words to 'ಶಾಲೆ':")
for word, similarity in similar_words:
    print(word, similarity)
