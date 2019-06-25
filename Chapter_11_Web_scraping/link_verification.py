'''
Write a program that, given the URL of a web page, will attempt to download
every linked page on the page. The program should flag any pages
that have a 404 “Not Found” status code and print them out as broken links.
'''

import requests, bs4, os


def verify_links(url, cwd):
    """
    Processes all links for given url and does the following:\n
    * if links is valid - records content of the link into a file
    * if link is empty - records tags into separate file
    * if link is broken - records links into separate file
    :param url: working url
    :param cwd: absolute path
    :return: nothing
    """

    # create folder to store results
    os.makedirs(cwd, exist_ok=True)
    os.chdir(cwd)

    checked_links = []
    broken_links = []
    empty_links = []

    # open the url
    page = requests.get(url)
    page.raise_for_status()

    # search for links inside of the url
    soup = bs4.BeautifulSoup(page.text, features="html.parser")
    link_elem = soup.select("a")

    # follow each link and check response
    for item in link_elem:
        href = item.get('href')

        try:
            if href is not None:  # catch empty links

                if href.startswith("/"):
                    href = url + href  # create full href address for internal links like "/about"

                # process each link once time only (for cases when the same link appears multiple times on the page)
                if href not in checked_links:
                    page = requests.get(href)

                    # record broken href
                    if page.status_code == 404:
                        broken_links.append(href)

                    # save page for valid href
                    elif page.status_code == 200:
                        file_name = f"Results for page {href}.txt".replace("https://", "").replace("http://", "").replace("/", "_")
                        file = open(os.path.join(cwd, file_name), "wb")

                        # write href at the top of the file page
                        top_line = f"Results for page: {href}\n\n"
                        b = bytearray()
                        b.extend(map(ord, top_line))
                        file.write(b)

                        # write content of the href
                        for chunk in page.iter_content(1000000):
                            file.write(chunk)
                        file.close()

                    checked_links.append(href)
            else:
                empty_links.append(item)

        except Exception as exc:
            print(f"Occurred exception: {exc}")

    # record results in broken links file
    broken_links_file = open("Broken links list.txt", "w")
    for item in broken_links:
        broken_links_file.write(f"{item}\n")
        broken_links_file.close()

    # record results in empty links file
    empty_links_file = open("Empty links elements.txt", "w")
    for item in empty_links:
        empty_links_file.write(f"{str(item)}\n")
        empty_links_file.close()


website = "https://www.archmotorcycle.com"
working_folder = "D:\\Broken links"

verify_links(website, working_folder)

