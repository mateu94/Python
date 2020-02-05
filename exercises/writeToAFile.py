import requests
from bs4 import BeautifulSoup

url = input("Enter the url: ")
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

with open("out.txt", "w") as outputFile:
    for article_heading in soup.find_all("h2"):
         outputFile.write(article_heading.text + "\n")
