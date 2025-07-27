import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = [h3.get_text() for h3 in soup.find_all("h3")[:10]]  # top 10 headlines
        return headlines
    else:
        return ["Failed to retrieve news"]

if __name__ == "__main__":
    news = scrape_bbc_news()
    print("Top BBC News Headlines:")
    for idx, headline in enumerate(news, 1):
        print(f"{idx}. {headline}")
