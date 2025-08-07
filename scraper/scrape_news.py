import requests
from bs4 import BeautifulSoup
import pandas as pd

print("🔍 Fetching latest news...")

# Sample scrape from Hacker News
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

news_data = []
for item in soup.select(".athing"):
    title_tag = item.select_one(".titleline a")
    if title_tag:
        title = title_tag.text
        link = title_tag['href']
        news_data.append({"title": title, "link": link})

# Check if we got any data
if not news_data:
    print("⚠️ No news items found!")
else:
    # Save to CSV
    df = pd.DataFrame(news_data)
    df.to_csv("scraper/latest_news.csv", index=False)

    print("✅ News saved to latest_news.csv")