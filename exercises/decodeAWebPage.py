import requests
from bs4 import BeautifulSoup

url = input("Enter the url: ")
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

for article_heading in soup.find_all("h2"):
    print(article_heading.text)
