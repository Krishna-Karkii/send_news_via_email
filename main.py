import requests
import send_email

topic = "earth"
# Api key and url
api_key = "7ba2aaf2a0864e04a249eab3ea6ef225"
url = (f"https://newsapi.org/v2/everything?q={topic}"
       "&from=2024-04-04&sortBy=publishedAt"
       "&apiKey=7ba2aaf2a0864e04a249eab3ea6ef225"
       "&language=en")

# request api and store it in df as dictionary
request = requests.get(url)
df = request.json()

content = "Subject: Today's news\n"
for article in df["articles"][0:10]:
    if article["title"] and article["description"] is not None:
        content = (content + article['title']
                   + '\n' + article["description"]
                   + "\n" + article["url"] + 2*"\n")

content = content.encode("utf-8")

send_email.send_mail(message=content,
                     user_email="krishnakarki1996@gmail.com")

