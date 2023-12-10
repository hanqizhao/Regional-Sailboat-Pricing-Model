import requests
from bs4 import BeautifulSoup
import pandas as pd

# 发送GET请求，获取网站内容
url = "https://www.boat-specs.com/"
response = requests.get(url)

# 使用BeautifulSoup解析网站内容
soup = BeautifulSoup(response.content, "html.parser")

# 提取需要的数据，存储到Python数据结构中
data = []
boats = soup.find_all("div", class_="boatblock")
for boat in boats:
    name = boat.find("h3").text.strip()
    specs = boat.find("ul", class_="specs")
    parameters = {}
    for li in specs.find_all("li"):
        key = li.find("span", class_="spec-title").text.strip()
        value = li.find("span", class_="spec-data").text.strip()
        parameters[key] = value
    data.append({"name": name, "parameters": parameters})

# 将数据转换成DataFrame对象，并导出到Excel文件中
df = pd.DataFrame(data)
df.to_excel("boats.xlsx", index=False)