import requests
from sendemail import send_email

topic = "tesla"

api_key = "ef5bbf04ca734e0bb53ce7745912f6f1"
url="https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2023-01-21&sortBy=publishedAt&" \
    "apiKey=ef5bbf04ca734e0bb53ce7745912f6f1&" \
    "language=en"

request = requests.get(url)
content = request.json()

body = " "

for article in content["articles"][:20]:
    body = "Subject: Today's news." + "\n" \
           + body + article["title"] + "\n" \
           + article["description"] + "\n" \
           + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

