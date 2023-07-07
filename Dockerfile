FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git python3-pip ffmpeg

RUN mkdir /safone
WORKDIR /safone

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
