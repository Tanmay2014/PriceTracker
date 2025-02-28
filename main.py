import requests as r
import bs4

# todo
# Make changes for amazon flipkart and Pricehistory

base_url = 'https://www.amazon.in'
# url = "https://www.amazon.in/dp/B0C8WP6B8R"
# The Above comment was an attempt to search product using product id

url = "https://amzn.in/d/5w9fQZk"
purl = "https://pricehistory.app/p/western-digital-wd-blue-sn580-pcie-gen-VWESmhw8"

headers = {
    'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'
}

base_response = r.get(url, headers=headers)
cookies = base_response.cookies

def to_text(product_response):
    soup = bs4.BeautifulSoup(product_response.text, features='lxml')
    return soup

def remove_extra_from_price(final_price):
    final_price = final_price.replace('<span class="a-price-whole">', '')
    final_price = final_price.replace('<span class="a-price-decimal">.</span></span>', '')
    final_price = final_price.replace(',','')
    return int(final_price)

def remove_extra_from_prod_name(prod_name):
    prod_name = str(prod_name)
    prod_name = prod_name.replace('[<span class="a-size-large product-title-word-break" id="productTitle">        ','')
    prod_name = prod_name.replace('       </span>]','')
    return prod_name

def ph_remove_extra_from_price(final_price):
    final_price = final_price.replace('[<div class="col bg-info text-light"> <span class="label">Lowest:</span> <span class="amount">₹', '')
    final_price = final_price.replace(' </span> </div>]', '')
    a_final_price = int(final_price.replace(',',''))
    return int(a_final_price)


product_response = r.get(url, headers=headers, cookies=cookies)
price_lines = to_text(product_response).find_all(class_= "a-price-whole")
prod_name = to_text(product_response).find_all(class_="a-size-large product-title-word-break")
# print(type(prod_name), type(price_lines))
final_price = str(price_lines[0])
print(f"{remove_extra_from_prod_name(prod_name)[:30]} : {remove_extra_from_price(final_price)}")

ph_response = r.get(purl, headers=headers, cookies=cookies)
ph_price_lines = str(to_text(ph_response).find_all(class_="col bg-info text-light"))
print(f"Lowest price for {remove_extra_from_prod_name(prod_name)[:30]} is {ph_remove_extra_from_price(ph_price_lines)}")