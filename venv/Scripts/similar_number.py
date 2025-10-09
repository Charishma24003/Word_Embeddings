from gensim.models import Word2Vec

model = Word2Vec.load("kannada_word2vec.model")
from scipy.spatial.distance import cosine

word1 = 'ಶಾಲೆ'
word2 = 'ಕಾಲೇಜು'

similarity = 1 - cosine(model.wv[word1], model.wv[word2])
print(f"Similarity between '{word1}' and '{word2}': {similarity:.4f}")

