import requests
from bs4 import BeautifulSoup
from note import extract_info
import csv

file = open("naver_books.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["title", "img_src", "detail_link", "author", "publisher"])

final_result = []

for i in range(8):
    book_html = requests.get(f'https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+2}')
    book_soup = BeautifulSoup(book_html.text, 'html.parser')
    book_list_box = book_soup.find("ol", {"class" : "basic"})
    book_list = book_list_box.find_all("li")

    final_result = final_result + extract_info(book_list)

print(book_list)

for result in final_result:
    row=[]
    row.append(result['title'])
    row.append(result['img_src'])
    row.append(result['detail_link'])
    row.append(result['author'])
    row.append(result['publisher'])

    writer.writerow(row)

# print(final_result)

# 'title' : title,
#             'img_src': img_src,
#             'detail_link': detail_link,
#             'author': author,
#             'publisher': publisher