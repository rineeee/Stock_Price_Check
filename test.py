from flask import Flask, render_template
from bs4 import BeautifulSoup
import urllib.request as req


def getStock(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = req.urlopen(url).read().decode('cp949')
    soup = BeautifulSoup(res, "html.parser")

    stock = soup.select("p.no_today span.blind")[0].text
    status = soup.select(
        'div.rate_info > div > p.no_exday > em:nth-child(2)')[0].text.split("\n")

    info = {"stock": stock, "status": status[1], "delta": status[2]}

    return info


def getStockData(data):
    info = getStock(data["code"])

    result = data
    result["info"] = info

    return result


app = Flask(__name__)


@app.route('/')
def home():

    datas = [{"name": "LG화학", "code": "051910"},
             {"name": "삼성전자", "code": "051910"},
             {"name": "LG전자", "code": "066570"}]

    result = []
    for data in datas:
        r = getStockData(data)
        result.append(r)

    return render_template('stock.html',  datas=result)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
