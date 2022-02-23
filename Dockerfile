FROM python:3.9

RUN mkdir ./app
RUN chmod 777 /app
WORKDIR /app

RUN apt -qq update && apt -qq install -y git python3 ffmpeg libsndfile1-dev python3-pip

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash","start.sh"]
