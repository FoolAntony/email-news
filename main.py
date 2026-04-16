import requests
from send_email import send_email

api_key = "YOUR_API_KEY"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
       "2026-03-16&sortBy=publishedAt" \
       f"&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with page content
content =  request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)