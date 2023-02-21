import requests

api_key = "ef5bbf04ca734e0bb53ce7745912f6f1"
url="https://newsapi.org/v2/everything?q=tesla&" \
    "from=2023-01-21&sortBy=publishedAt&" \
    "apiKey=ef5bbf04ca734e0bb53ce7745912f6f1"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print (article["title"])
    print(article["description"])

