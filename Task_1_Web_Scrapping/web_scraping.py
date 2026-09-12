import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article", class_="product_pod")
Data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.replace("£", "").strip()
    rating = book.find("p", class_="star-rating")["class"][1]
    availability = book.find("p", class_="instock availability").text.strip()
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print(f"Availability: {availability}")

    Data.append({
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability
    })

    df = pd.DataFrame(Data)
    pd.to_numeric(df["price"], errors="coerce")
    
    print(df["price"].dtype)
    print(df["price"].describe())


    print("\nDataset information:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Values:")
    print(df.duplicated().sum())

    print("\nSummary Statistics:")
    print(df.describe())

    print("\nPrice Summary Statistics:")
    print(df["price"].describe())
