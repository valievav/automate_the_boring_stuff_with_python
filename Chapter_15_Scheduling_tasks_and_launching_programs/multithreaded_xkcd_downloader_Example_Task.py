'''
re-write download_xkcd_Example_Task.py to use multithreading to complete the task faster
'''

import threading
import requests, bs4, os, urllib.request


def download_img(base_url, cwd, start_page="", end_page=1):
    """
    Downloads images for provided ur from starting page till the end page.\n
    :param base_url:
    :param cwd: absolute path
    :param start_page: int, optional
    :param end_page: int, optional
    :return:
    """

    def save_image(url):
        print(f"Working with {url}")

        # extracting page html
        page = requests.get(url)
        page.raise_for_status()

        # getting html element for comic image
        soup = bs4.BeautifulSoup(page.text, features="html.parser")
        image_elem = soup.select("#comic img")

        # retrieving the image link
        if not image_elem:
            print("    No comic image found")
        else:
            image = image_elem[0].get("src")  # list contains only 1 element, hence [0] usage

            # extracting web file name
            path = image.split("/")
            file_name = path[-1]

            # saving image to the cwd
            urllib.request.urlretrieve("http:" + image, cwd + file_name)
            print(f"    Image '{file_name}' is saved")

            # getting html element for previous page button
            soup = bs4.BeautifulSoup(page.text, features="html.parser")
            button_elem = soup.select("a[rel='prev']")

            # retrieving the button link
            if not button_elem:
                print("    No previous button found")
            else:
                button = button_elem[0].get("href")  # list contains only 1 element, hence [0] usage

                # moving to the previous page
                url = base_url + button
                print(f"    Going to the next page - {url}")
                return url

    print(f"START PAGE: {start_page}. END PAGE: {end_page}")

    if not os.path.abspath(cwd):
        print("Please enter an absolute path")

    # create working folder if absent
    if not os.path.exists(cwd):
        os.mkdir(cwd)

    # iterating through all images up to the last one, which has # in url (if no start/end page provided)
    if not start_page and not end_page:
        url = base_url
        while not url.endswith("#"):
            save_image(url)

    # iterating through selected scope of images (if start/end page provided)
    if start_page or end_page:
        url = base_url + str(start_page)
        while not url.endswith(str(end_page-1)+'/'):
                url = save_image(url)



url = "https://xkcd.com/"
working_dir = "D:\\xkcd comics\\"
threads = []

for i in range(1, 50, 5):
    thread = threading.Thread(target=download_img, args=[url, working_dir, i+99, i])
    threads.append(thread)
    thread.start()

