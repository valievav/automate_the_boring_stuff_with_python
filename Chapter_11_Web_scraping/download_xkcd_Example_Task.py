#! python3
# download_xkcd_Example_Task.py - downloads comic images from the most recent to the first one

import requests, bs4, os, urllib.request


def download_img(url, cwd):
    """
    Downloads image from the current url page and all previous page images up to the last one.\n
    :param url:
    :param cwd: absolute path
    :return: nothing
    """

    if not os.path.abspath(cwd):
        print("Please enter an absolute path")

    base_url = url  # will be used for changing web pages

    # iterating through all images up to the last one, which has # in url
    while not url.endswith("#"):

        # extracting page html
        page = requests.get(url)
        page.raise_for_status()

        # getting html element for comic image
        soup = bs4.BeautifulSoup(page.text, features="html.parser")
        image_elem = soup.select("#comic img")

        # retrieving the image link
        if not image_elem:
            print("No comic image found")
        else:
            image = image_elem[0].get("src")  # list contains only 1 element, hence [0] usage

            # extracting web file name
            path = image.split("/")
            file_name = path[-1]

            # saving image to the cwd
            urllib.request.urlretrieve("http:" + image, cwd + file_name)
            print(f"Image '{file_name}' is saved")

            # getting html element for previous page button
            soup = bs4.BeautifulSoup(page.text, features="html.parser")
            button_elem = soup.select("a[rel='prev']")

            # retrieving the button link
            if not button_elem:
                print("No previous button found")
            else:
                button = button_elem[0].get("href")  # list contains only 1 element, hence [0] usage

                # moving to the previous page
                url = base_url + button
                print(f"Going to the next page - {url}")


target_url = "https://xkcd.com/"
working_folder = "D:\\xkcd comics\\"

# creating folder to store images in
os.makedirs(working_folder, exist_ok=True)

# running method to download comic images from url
download_img(target_url, working_folder)
















