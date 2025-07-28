import requests
import pandas as pd
from datetime import datetime

# 1. Define the keyword you want to search for
KEYWORD = "supply chain"
API_URL = f"https://gnews.io/api/v4/search?q={KEYWORD}&token=1f83d2b76c1e0676a431f5c8&lang=en"

def fetch_news():
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        data = response.json().get("articles", [])
        news_list = []

        for article in data:
            news_list.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "publishedAt": article.get("publishedAt")
            })

        # Save as CSV in /data folder
        df = pd.DataFrame(news_list)
        file_name = f"data/news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(file_name, index=False)
        print(f"✅ News saved to {file_name}")
    else:
        print(f"❌ Failed to fetch news. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_news()
