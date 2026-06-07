FROM python:3.10

WORKDIR /app

ENV PYTHONPATH="${PYTHONPATH}:/app"

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Chrome

RUN apt-get update && apt-get install -y wget curl unzip gnupg2

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg

RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && apt-get install -y google-chrome-stable

COPY . .

CMD ["pytest", "test_cases/", "--browser", "chrome", "--headless"]
