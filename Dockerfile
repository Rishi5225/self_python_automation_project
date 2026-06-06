FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Chrome

RUN apt-get update && apt-get install -y wget unzip curl gnupg && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && apt-get update && apt-get install -y google-chrome-stable

COPY . .

CMD ["pytest", "test_cases/", "--browser", "chrome", "--headless"]
