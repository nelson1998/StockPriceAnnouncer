import pyttsx3
import bs4
import requests

engine = pyttsx3.init()

ticker = str(input("Enter a stock ticker."))
final_price = ""

stock = requests.get("https://robinhood.com/stocks/" + ticker)
soup = bs4.BeautifulSoup(stock.text, "xml")
price = soup.find("div", class_="_2YApulnV3lazBStOvoKx6m").find_all("span")
name = soup.find("header", class_="Jo5RGrWjFiX_iyW3gMLsy").h1.text

for spans in price:
    final_price = final_price + spans.string

engine.say(name + " is now at: " + final_price)
engine.runAndWait()
