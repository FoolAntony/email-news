import requests
from send_email import send_email

TOPIC = "tesla"

api_key = "YOUR_API_KEY"
url = "https://newsapi.org/v2/everything?" \
      f"q={TOPIC}" \
      "&from=2026-03-16" \
      "&sortBy=publishedAt" \
      f"&apiKey={api_key}" \
      "&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with page content
content =  request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"][:10]:
    if article["title"] and article["description"] is not None:
        body =  "Subject: Today's News" + "\n" \
                + body + article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] \
                + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)