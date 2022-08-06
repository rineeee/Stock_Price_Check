from bs4 import BeautifulSoup
import urllib.request as req


def getStock(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = req.urlopen(url).read().decode('cp949')
    soup = BeautifulSoup(res, "html.parser")

    stock = soup.select("p.no_today span.blind")[0].text
    status = soup.select(
        "div.rate_info > div > p.no_exday > em:nth-child(2)")[0].text.split("\n")

    ret = {"stock": stock, "status": status[1], "delta": status[2]}
    return ret


# print(getStock("090360")["delta"])
