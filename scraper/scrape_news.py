import requests
from bs4 import BeautifulSoup

def scrape_google_news(keyword="supply chain disruption"):
    url = f"https://news.google.com/search?q={keyword.replace(' ', '%20')}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve news.")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    
    for item in soup.find_all("a", class_="DY5T1d", limit=5):  # Get top 5
        title = item.text
        link = "https://news.google.com" + item["href"][1:]
        headlines.append({"title": title, "link": link})
    
    return headlines

if __name__ == "__main__":
    print("🔍 Fetching latest news...")
    news = scrape_google_news("logistics disruption")
    for i, n in enumerate(news, 1):
        print(f"{i}. {n['title']} → {n['link']}")
