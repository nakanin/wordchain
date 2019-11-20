import time
import random
import os
import gensim
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)


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
    return jsonify(words=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=int(os.environ.get('PORT', 5000)))