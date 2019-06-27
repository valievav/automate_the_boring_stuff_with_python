'''
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that has
a search feature.
'''

import os, requests, bs4, urllib.request

def download_pictures(url, keywords, cwd):

    # create folder to store results
    os.makedirs(cwd, exist_ok=True)
    os.chdir(cwd)

    # get images page
    page = requests.get(url + "/search?q=" + keywords)
    page.raise_for_status()

    # extract all images
    soup = bs4.BeautifulSoup(page.text, features="html.parser")
    images = soup.select("div.view.photo-list-view.requiredToShowOnServer")

    # save each image
    for n in range(len(images)-1):
        href = images[n].get('href')

        if href:
            image_url = url + href
            path = image_url.split("/")
            file_name = path[-1]
            destination_file = cwd + file_name
            urllib.request.urlretrieve(image_url, destination_file)
            print(f"Image '{file_name}' is saved")
            pass



website = "https://www.flickr.com"
search_keywords = "blade runner 2049"
website_name = website.replace("https://www.", "")
working_directory = f"D:\\Images from {website_name}\\"

download_pictures(website, search_keywords, working_directory)

