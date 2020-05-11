import requests
from bs4 import BeautifulSoup
from note import extract_info
import csv

file = open("hospital.csv", mode="w", encoding='euc-kr',newline='')
writer = csv.writer(file)
writer.writerow(["city", "district", "title","number"])

hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'
hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")

# 이제부터 시도, 시군구, 선별진료소(이름), 전화번호 크롤링 후 csv 파일에 저장하시면 됩니다!

hospital_list_box = hospital_soup.find("tbody",{"class":"tb_center"})
hospital_list = hospital_list_box.find_all('tr')

print(hospital_list)


final_result = extract_info(hospital_list)

for hospital_row in final_result:
    row = []
    row.append(hospital_row['시도'])
    row.append(hospital_row['시군구'])
    row.append(hospital_row['선별진료소'])
    row.append(hospital_row['전화번호'])
    writer.writerow(row)

print("크롤링 끝!")