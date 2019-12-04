import time
import random
import os
import gensim
import MeCab
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__, static_folder='client/dist', static_url_path='')
app.config['JSON_AS_ASCII'] = False
CORS(app)
model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)


@app.route('/word-from/<input>')
def wordchain(input):
    if request.args.get('type', 'renso') == 'renso':
        results = associate(input)
    else:
        results = shiritori(input)

    return jsonify(words=results)


def associate(input):
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
    return results


def makeDictionary():
    dic = {}
    for line in open('Noun.csv', 'r', encoding='euc_jp'):
        values = line.strip().split(',')
        word = values[0]
        kana = values[-2]
        word = word + '（' + kana + '）'
        if not kana[-1] in ['ン', 'ィ', 'ャ', 'ュ', 'ョ', 'ー']:
            words = dic.setdefault(kana[0], [])
            words.append((word, kana[-1]))
    return dic


def shiritori(input):
    dic = makeDictionary()
    mecab = MeCab.Tagger('-Oyomi')
    last = mecab.parse(input)[-2]

    results = [input]
    for i in range(10):
        words = dic.get(last)
        (word, last) = random.choice(words)
        results.append(word)
    return results


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=int(os.environ.get('PORT', 5000)))