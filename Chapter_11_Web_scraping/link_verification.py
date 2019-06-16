'''
Write a program that, given the URL of a web page, will attempt to download
every linked page on the page. The program should flag any pages
that have a 404 “Not Found” status code and print them out as broken links.
'''

import requests, bs4

url = "https://www.archmotorcycle.com/"
broken_pages = []

page = requests.get(url)

try:
    page.raise_for_status()
except requests.HTTPError as exc:
    print(f"There was an issue: {exc}")

soup = bs4.BeautifulSoup(page.text, features="html.parser")
link_elem = soup.select("a")

for item in link_elem:
    link = item.get('href')








