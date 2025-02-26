import requests as r
import bs4


# todo
# Make changes for amazon flipkart and Pricehistory



base_url = 'https://www.amazon.in'
# url = "https://www.amazon.in/dp/B0C8WP6B8R"

url = "https://www.amazon.in/BlueTM-SN580-NVMeTM-Internal-Storage/dp/B0C8WP6B8R?crid=3IXLKWAGWGTST&dib=eyJ2IjoiMSJ9.4bNezvwYcZmzlujVgvhQKX1s-LUf-_1uLtOhF7f5gMxStl7F5j_LkQJFD1Nud5HcAphmb9gOCeiuirjj369HWyWS6A2Nzl9LIcI0BfUIfZ46papM_qo4E2Md5PthLC6oqSdQGV0ftUuHft1Ldf_vpZ_RCpJdYS9KZ2alscpRD7YgEDtWVCgkm_yV0mU-yLpUEdqxKqwTcbW5geqyVjlnaMCPd7tC1NzfAIU6iGj35OA.B2amf1DX_oN1GUh9vqAncKp6VtnksV1sGY_rtyiRzJs&dib_tag=se&keywords=sn580&qid=1740550304&sprefix=sn580%2Caps%2C235&sr=8-1&th=1"

headers = {
    'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'
}

base_response = r.get(url, headers=headers)
cookies = base_response.cookies

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

product_response = r.get(url, headers=headers, cookies=cookies)
soup = bs4.BeautifulSoup(product_response.text, features='lxml')
price_lines = soup.findAll(class_= "a-price-whole")
prod_name = soup.findAll(class_="a-size-large product-title-word-break")
# print(type(prod_name), type(price_lines))
final_price = str(price_lines[0])
print(f"{remove_extra_from_prod_name(prod_name)} : {remove_extra_from_price(final_price)}")
