import requests
from Send_email import Send_mail

topic = "stocks"

API_key = "6a90fa48a3bb4c85a1adddb15a089db6"
url = "https://newsapi.org/v2/everything?q={topic}&from=2023-10-12&sortBy" \
      "=publishedAt&apiKey=6a90fa48a3bb4c85a1adddb15a089db6&language=en"

# Make Request
response = requests.get(url)

# Get a Dictionary with data
contents = response.json()

# Access the title, decription
Body = ""
for article in contents["articles"]:
    Titles = article["title"]
    Articles = article["description"]
    links = article["url"]
    Body = f"{Body}\n{Articles}\n{links}"
Body = f"""\
Subject: News of the day 
   
{Body}
"""

Body = Body.encode("utf-8")
Send_mail(Body)
