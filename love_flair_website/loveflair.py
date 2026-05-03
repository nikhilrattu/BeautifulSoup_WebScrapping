import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# scrape name, price, stock, color, size
product_links= set()
all_data=[]
for x in range(1,11):
    base_url = "https://loveandflair.com/"
    url_next_page=(f"https://loveandflair.com/collections/activewear-1?page={x}")
    headers= {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
        }
    response=requests.get(url_next_page,headers=headers)
    
    soup=BeautifulSoup(response.text,"html.parser")
    # print(soup)
    products= soup.find_all("li", class_="collection-product-card quickview")
    for p in products:
        get_link = p.find("div", class_="card__title").find("a").get('href')
        stored_link = urljoin(base_url, get_link)
        product_links.add(stored_link)
        
for link in product_links:
    response=requests.get(link, headers=headers)

    soup = BeautifulSoup(response.text,'html.parser')

    name_of_product_tag = soup.find("h4", class_="product__title")
    price_of_product_tag = soup.find("span",class_="money")
    is_in_stock_tag=soup.find("span", class_="advantage__title")
    color_tag=soup.find("label", class_="color-swatch")
    available_size = []

    for inp in soup.find_all("input", {"name": "Size"}):
        classes = inp.get("class", [])
        
        if "disabled" not in classes:
            available_size.append(inp["value"])

    if available_size:
        size = available_size
    else:
        size = ["N/A"]
    name = name_of_product_tag.get_text(strip=True) if name_of_product_tag else None
    price = price_of_product_tag.get_text(strip=True) if price_of_product_tag else None
    stock = is_in_stock_tag.get_text(strip=True) if is_in_stock_tag else None
    color = color_tag.get_text(strip=True) if color_tag else None
    
    all_products={
            "Name": name,
            "Price": price,
            "Stock": stock,
            "Color": color,
            "Size": size
        }  
    all_data.append(all_products)

df=pd.DataFrame(all_data)
df.to_csv("products.csv", index=False)
