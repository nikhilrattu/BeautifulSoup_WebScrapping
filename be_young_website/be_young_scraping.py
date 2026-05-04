import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

new_arrivals = []

for page in range(1, 53):
    url = (f"https://www.beyoung.in/mens-new-arrival?page={page}")
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    # Extract JSON
    script = soup.find("script", id="__NEXT_DATA__")
    data = json.loads(script.string)

    # Navigate to products
    products = data["props"]["pageProps"]["details"]["products"]

    for item in products:
        product_name = item.get("name", "N/A")
        regular_price = item.get("price", "N/A")
        sale_price = item.get("special", "N/A")

        discount = "N/A"
        if isinstance(regular_price, (int, float)) and isinstance(sale_price, (int, float)) and regular_price != 0:
            discount = f"{round((1 - sale_price/regular_price)*100)}% off"

        all_products = {
            "Product": product_name,
            "Regular Price": regular_price,
            "Discounted Price": sale_price,
            "Discount": discount
        }

        new_arrivals.append(all_products)

#SAVE CSV HERE
df = pd.DataFrame(new_arrivals)
df.to_csv("BeYoung_Products.csv", index=False)

print("Total products:", len(df))
