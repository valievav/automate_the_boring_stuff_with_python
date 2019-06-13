#! python3
# lucky_Example_Task.pyw - opens top results for some search in separate tabs

import sys, webbrowser, requests, bs4


def open_top_search_results():
    full_search = url + search_keywords

    # getting search page content
    page = requests.get(f"{full_search}", headers={'User-agent': 'run 0.1'})
    print(f"Getting results for {full_search}")
    page.raise_for_status()

    # finding link elements on a search results page
    soup = bs4.BeautifulSoup(page.text, features="html.parser")
    elements = soup.select(".r a")

    # opening each search link in a browser
    tabs_count = min(5, len(elements))  # returns smallest number between results_count and elements length
    for n in range(tabs_count):
        link = url+elements[n].get("href")
        webbrowser.open(link)
        print(f"Opening {link}")


search_keywords = " ".join(sys.argv[1:])
url = "https://www.bing.com/search?q="

open_top_search_results()


