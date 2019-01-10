from gensim.models import Word2Vec
model = Word2Vec.load("sample.model")
print(model['computer'])
