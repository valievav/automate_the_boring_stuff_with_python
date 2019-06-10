#! python3
# map_it_Example_Task.py - launches Google maps in the browser using address from clipboard

import webbrowser, pyperclip

url = "https://www.google.com/maps/place/"

# using a clipboard to get the address
pyperclip.copy("226 W 46th St, New York, NY 10036, USA")  # inserting value into clipboard for simplicity
address = pyperclip.paste()  # getting value from the clipboard

# opening Google maps using address from clipboard
print(f"Opening Google maps to search for '{address}'")
webbrowser.open(f'{url}{address}')


