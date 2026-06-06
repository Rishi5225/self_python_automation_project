FROM python:3.10

WORKDIR /app

COPY . .

ENV PYTHONPATH=/app

RUN pip install -r requirements.txt

CMD ["pytest"]FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest"]
