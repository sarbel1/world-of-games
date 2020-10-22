FROM python:3

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install selenium

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "MainScores.py"]
