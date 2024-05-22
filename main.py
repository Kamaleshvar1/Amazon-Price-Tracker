import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
ACCEPTED_LANGUAGE = "en-US"
PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPTED_LANGUAGE
}

response = requests.get(url=PRODUCT_URL, headers=header)
data = response.text
soup = BeautifulSoup(data, "lxml")
price_whole = soup.find(class_="a-offscreen").get_text()
price_wo_currency = price_whole.split("$")[1]
price = float(price_wo_currency)
print(price)

product_name = soup.find(id="productTitle").get_text()
print(product_name)

if price <= 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kamaleshvar2004@gmail.com",
            msg=f"subject:Price Drop!!\n\n{product_name} is now: ${price}\n{PRODUCT_URL}".encode("utf-8")
        )
