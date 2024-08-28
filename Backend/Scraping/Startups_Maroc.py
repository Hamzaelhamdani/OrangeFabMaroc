import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=['Name', 'Description', 'Logo'])
res = 150
url = "https://www.start-up.ma/liste-startups-au-maroc/"
response = requests.get(url).text
doc = BeautifulSoup(response, "html.parser")
pages = int(str(doc.find(class_ = "wp-pagenavi").find("span")).split("</span>")[0].split(">")[-1].split()[-1])
for page in range(pages):
    print(page+1)
    url = "https://www.start-up.ma/liste-startups-au-maroc/page/"+str(page+1)
    response = requests.get(url).text
    doc = BeautifulSoup(response, "html.parser")
    table = doc.find_all(class_ = "card_ecole card_ecole_clicked startup_height")
    for el in table:
        name = str(el.find("h3")).split("</a>")[0].split(">")[-1]
        desc = str(el.find("p")).split("</p>")[0].split(">")[-1]
        try:
            img = el.find("img")["src"]
        except:
            img = "No Image"
        df = pd.concat([df, pd.DataFrame([{"Name":name, "Description":desc, "Logo":img}])], ignore_index=True)
df.to_csv('output.csv', index=False)