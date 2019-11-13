import gensim


model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)
model.save_word2vec_format('model.bin', binary=True)
