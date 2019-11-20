FROM python:3.7
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt

# fastText の学習済みモデルをダウンロード
COPY convertmodel.py /code
RUN wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=0ByFQ96A4DgSPUm9wVWRLdm5qbmc' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=0ByFQ96A4DgSPUm9wVWRLdm5qbmc" -O tmp.zip && rm -rf /tmp/cookies.txt \
    && unzip tmp.zip \
    && rm -rf tmp.zip \
    # 読み込みを高速化するためバイナリフォーマットに変換
    && python convertmodel.py \
    && rm -rf model.vec

COPY app.py /code
COPY client/dist/ /code/client/dist/
CMD python app.py
