'''
Write a program that checks the websites of several web comics
and automatically downloads the images if the comic was updated since the program’s last visit.
'''

import requests, os, bs4
from urllib.request import urlretrieve


def web_comics_downloader(storage_folder, urls_list):
    """
    Downloads comics for passed URLs.
    :param storage_folder: abs path
    :param urls_list: list of valid URLs
    :return:
    """

    def get_html_from_url(url):
        html_page = requests.get(url)
        html_page.raise_for_status()
        print(f"Got html for url {url}")
        return html_page

    def record_html_to_file(url, page_html):
        html_file_name = f"{url.strip('/').split('/')[-1]}_html.txt"
        file = open(html_file_name, "wb")
        for chunk in page_html.iter_content(chunk_size=100000):
            file.write(chunk)
        file.close()
        print(f"Recorded html for {url} in file {html_file_name}")

    # create general comics folder
    if not os.path.isdir(storage_folder):
        os.mkdir(storage_folder)
    os.chdir(storage_folder)

    # iterate over each comic url
    for comic_url in urls_list:
        html = get_html_from_url(comic_url)

        # save html page in file for reference
        record_html_to_file(comic_url, html)

        # create comic folder
        comic_folder = f"{comic_url.strip('/').split('/')[-1]}"
        if not os.path.isdir(comic_folder):
            os.mkdir(comic_folder)
        os.chdir(comic_folder)

        # find and iterate over each comic issue url
        issue_soup = bs4.BeautifulSoup(html.text, "html.parser")
        issue_elements = issue_soup.select("#post-area a")
        for issue in issue_elements:
            issue_link = issue.get("href")
            issue_html = get_html_from_url(issue_link)

            # save html page in file for reference
            record_html_to_file(issue_link, issue_html)

            # create issue folder
            issue_folder = issue_link.strip("/").split("/")[-1]
            if not os.path.isdir(issue_folder):
                os.mkdir(issue_folder)

            # find and save each comic image
            img_soup = bs4.BeautifulSoup(issue_html.text, "html.parser")
            img_elements = img_soup.select(".pinbin-copy>p>a")
            img_number = 1
            for image in img_elements:
                img_link = image.get("href")
                if img_link:
                    file_name = f"{img_number}_page.jpg"
                    urlretrieve(img_link, os.path.join(issue_folder, file_name))
                    print(f"Saved file {file_name} in {issue_folder}")
                    img_number += 1


comics_storage_folder_comics = "D:\\Comics"
comic_urls = ["https://read-comic.com/category/monstress/"]

web_comics_downloader(comics_storage_folder_comics, comic_urls)

