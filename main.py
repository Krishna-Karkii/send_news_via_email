import requests
import send_email
# Api key and url
api_key = "7ba2aaf2a0864e04a249eab3ea6ef225"
url = ("https://newsapi.org/v2/everything?q=earth"
       "&from=2024-04-04&sortBy=publishedAt"
       "&apiKey=7ba2aaf2a0864e04a249eab3ea6ef225")

# request api and store it in df as dictionary
request = requests.get(url)
df = request.json()

content = ""
for article in df["articles"]:
    if article["title"] and article["description"] is not None:
        content = (content + article['title'] + '\n' + article["description"]
                   + 2*"\n")

content = content.encode("utf-8")

send_email.send_mail(message=content,
                     user_email="krishnakarki1996@gmail.com")

