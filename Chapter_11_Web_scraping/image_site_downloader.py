'''
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that has
a search feature.
'''

import os, requests, bs4, urllib.request, re

def download_images(url, keywords, cwd):
    """
    Downloads images from Flickr after the keywords search.\n
    :param url:
    :param keywords:
    :param cwd: absolute path
    :return: nothing
    """

    # create folder to store results
    os.makedirs(cwd, exist_ok=True)
    os.chdir(cwd)

    # get images page
    page = requests.get(url + "/search?q=" + keywords)
    page.raise_for_status()

    # extract images
    soup = bs4.BeautifulSoup(page.text, features="html.parser")
    images = soup.find_all('div', attrs={'class' : 'view photo-list-photo-view requiredToShowOnServer awake'})  # targeting only top 24 img for now

    for n in range(0, len(images)-1):

        # extracting .jpg image from style attribute
        element = images[n].get('style')
        img = re.search(f'\/\/live.staticflickr.com\/.+\.jpg', element).group()

        # saving images
        path = img.split("/")
        img_name = path[-2] + "_" + path[-1]
        urllib.request.urlretrieve("https:" + img, cwd + img_name)
        print(f"Image {img_name} is saved")


website = "https://www.flickr.com"
search_keywords = "blade runner 2049"
website_name = website.replace("https://www.", "")
working_directory = f"D:\\Images from {website_name}\\"

download_images(website, search_keywords, working_directory)

