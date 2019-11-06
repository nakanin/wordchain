import time
import random
import gensim
from flask import Flask


app = Flask(__name__)


def loadModel():
    start = time.time()
    print('モデルの読み込み開始...')
    loaded = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)
    print('モデルの読み込み終了')
    print(time.time() - start)
    return loaded


model = loadModel()


@app.route('/word-from/<input>')
def wordchain(input):
    results = [input]
    for i in range(10):
        similars = model.most_similar(positive=[input])
        print([s[0] for s in similars])
        random.shuffle(similars)
        for (word, value) in similars:
            if not word in results:
                results.append(word)
                input = word
                break
    return "<br>↓<br>".join(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)