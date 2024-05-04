import requests

# Api key and url
api_key = "7ba2aaf2a0864e04a249eab3ea6ef225"
url = ("https://newsapi.org/v2/everything?q=tesla"
       "&from=2024-04-04&sortBy=publishedA"
       "t&apiKey=7ba2aaf2a0864e04a249eab3ea6ef225")

# request api and store it in df as dictionary
request = requests.get(url)
df = request.json()

print(df)