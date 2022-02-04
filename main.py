from bs4 import BeautifulSoup
import requests
import pandas as pd


URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
response = requests.get(URL)
payscale_webpage = response.text
soup = BeautifulSoup(payscale_webpage, "html.parser")
pay_tag = soup.find_all(name="td", class_="data-table__cell")

pay_major = []
pay_early = []
pay_mid = []
for tag in pay_tag:
    if tag.getText()[:6] == "Major:":
        pay_major.append(tag.getText()[6:])
    elif tag.getText()[:5] == "Early":
        early_pay = tag.getText()[18:].replace(',','')
        pay_early.append(float(early_pay))
    elif tag.getText()[:3] == "Mid":
        mid_pay = tag.getText()[16:].replace(',','')
        pay_mid.append(float(mid_pay))

pay_data = []
for i in range(len(pay_mid)):
    pay_data.append([pay_major[i], pay_early[i], pay_mid[i]])

df = pd.DataFrame(pay_data, columns=["Major", "Early Career Pay", "Mid-Career Pay"])

print(df.sort_values("Mid-Career Pay"))