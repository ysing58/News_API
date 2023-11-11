import requests

API_key = "6a90fa48a3bb4c85a1adddb15a089db6"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-11&sortBy=publishedAt&apiKey=6a90fa48a3bb4c85a1adddb15a089db6"


#Make Request
request = requests.get(url)

#Get a Dictionary with data
contents = request.json()

#Access the title, decription
for article in contents["articles"]:
    print(article["title"])
    print(article["Description"])