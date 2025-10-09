from gensim.models import Word2Vec

# Load your trained model
model = Word2Vec.load("kannada_word2vec.model")

word = 'ಸಮಸ್ಯೆ'
similar_words = model.wv.most_similar(word, topn=10)

print(f"Most similar words to '{word}':\n")
for w, score in similar_words:
    print(f"{w:15} : {score:.4f}")


