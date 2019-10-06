'''
Write a program that checks the websites of several web comics
and automatically downloads the images if the comic was updated since the program’s last visit.
'''

import requests, os, bs4, datetime, time
from urllib.request import urlretrieve  # to save image to local directory
import schedule  # to schedule program run

def web_comics_downloader(storage_folder, urls_list):
    """
    Downloads comics for passed URLs.
    If process was interrupted, program will skip downloaded issues and start process from one,
    on which it was terminated. Also it will skip images, that have already been downloaded.
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
        print(f"Created file '{html_file_name}'")

    last_run_time = datetime.datetime(1, 1, 1, 1, 1, 1)

    # create general Comics folder
    if not os.path.isdir(storage_folder):
        os.mkdir(storage_folder)
    os.chdir(storage_folder)

    # iterate over each comic url
    for comic_base_url in urls_list:

        # find number of pages for iteration
        html = get_html_from_url(comic_base_url)
        soup = bs4.BeautifulSoup(html.text, "html.parser")
        pages_number_elem = soup.find('nav', {'class': 'navigation'}).find_all('a')
        max_page = 1

        for elem in pages_number_elem:
            x = elem.text
            try:
                next_page = int(x)
                if max_page < next_page:
                    max_page = next_page
            except ValueError:
                pass

        issues_downloaded = 0

        for page in range(1, max_page+1):
            print(f"Going through page {page}...")
            comic_url = f"{comic_base_url}page/{page}/"
            comic_html = get_html_from_url(comic_url)

            # save html page in file for reference
            record_html_to_file(comic_url, comic_html)

            # create separate comic folder
            comic_folder = f"{comic_base_url.strip('/').split('/')[-1]}"
            if not os.path.isdir(comic_folder):
                os.mkdir(comic_folder)
            os.chdir(comic_folder)

            # sort all sub-folders by latest updated date
            # will be used to start uploading files from latest updated folder (for cases when process was interrupted)
            all_folders = sorted(filter(os.path.isdir, os.listdir('.')), key=os.path.getmtime)

            # find and iterate over each comic issue block
            issues_soup = bs4.BeautifulSoup(comic_html.text, "html.parser")
            issue_elem = issues_soup.find_all('div', {'class': 'pinbin-copy'})

            for issue in issue_elem:
                # find issue date
                issue_date_elem = issue.find('p', {'class': 'pinbin-date'})
                issue_date = datetime.datetime.strptime(issue_date_elem.text.strip(), '%B %d, %Y')
                # find issue name
                issue_name_elem = issue.find('a')
                issue_name = issue_name_elem.text.strip("…").strip()

                # skip sub-folders that already exists
                # start downloading from latest updated sub-folder issue OR if such issue does not have sub-folder
                if issue_name in all_folders[:-1]:
                    print(f"    Skipping issue '{issue_name}' as it already exists")
                    continue

                # download issue if it's older than last runtime
                if issue_date < last_run_time:
                    print(f"    Skipping issue '{issue_name}' - issue date {issue_date} < last runtime date {last_run_time}")
                else:
                    print(f"    Downloading issue '{issue_name}' - issue date {issue_date} > last runtime date {last_run_time}")
                    issue_link = issue_name_elem.get('href')
                    issue_html = get_html_from_url(issue_link)

                    # save html page in file for reference
                    record_html_to_file(issue_link, issue_html)

                    # create issue folder
                    if not os.path.isdir(issue_name):
                        os.mkdir(issue_name)

                    # find and save each comic image
                    img_soup = bs4.BeautifulSoup(issue_html.text, "html.parser")
                    img_elem = img_soup.select(".pinbin-copy>p>a")
                    existing_files = os.listdir(issue_name)

                    for image in img_elem:
                        img_link = image.get("href")
                        if img_link:
                            file_name = f"{img_link.strip('/').split('/')[-1]}"

                            # save file if it doesn't exists already, else skip it (for cases when process was interrupted)
                            if file_name not in existing_files:
                                img_path = os.path.join(issue_name, file_name)
                                urlretrieve(img_link, img_path)
                                print(f"        Saved file '{file_name}' into '{issue_name}'")
                            else:
                                print(f"        Skipping '{file_name}' as it already exists")

            print(f"Downloaded {len(issue_elem)} issues from page {page}")
            issues_downloaded += len(issue_elem)

        print(f"Process finished. Issues downloaded = {issues_downloaded}")
        # record last runtime
        last_run_time = datetime.datetime.now()
        print(f"Last run time = {last_run_time}")


comics_storage_folder_comics = "D:\\Comics"
comic_urls = ["https://read-comic.com/category/monstress/"]

schedule.every().day.at("20:00").do(web_comics_downloader, comics_storage_folder_comics, comic_urls)

# wait for the scheduled program to run
while True:
    schedule.run_pending()
    time.sleep(1)

