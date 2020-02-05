import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = input("Enter the url: ")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    for article_text in soup.find_all(class_="article__body"):
        print(article_text.text)
