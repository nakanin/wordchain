FROM python:3.7
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://drive.google.com/uc?export=download&id=0ByFQ96A4DgSPNFdleG1GaHcxQzA' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=0ByFQ96A4DgSPNFdleG1GaHcxQzA" -O tmp.zip && rm -rf /tmp/cookies.txt \
    && unzip tmp.zip \
    && rm -rf tmp.zip
ADD . /code
CMD python app.py
