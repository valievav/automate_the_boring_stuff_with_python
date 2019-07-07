'''
2048 is a simple game where you combine tiles by sliding them up, down,
left, or right with the arrow keys. You can actually get a fairly high score
by repeatedly sliding in an up, right, down, and left pattern over and over
again. Write a program that will open the game at https://gabrielecirulli
.github.io/2048/ and keep sending up, right, down, and left keystrokes to
automatically play the game.
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as selenium_exceptions
import random


def play_game(url):
    """
    Plays tile game using UP, DOWN, LEFT, RIGHT keys from the keyboard until the game is over or won.\n
    :param url: valid url
    :return: nothing
    """

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    print(f"Opened {url}")

    tile = driver.find_element_by_tag_name("html")
    print("Playing the game...")

    while True:
        result = driver.find_element_by_css_selector("div.score-container").text

        # check if game is over
        try:
            game_over = driver.find_element_by_css_selector("div.game-message.game-over")
            if game_over:
                print(f"GAME OVER. Your result is {result}")
                break

        # if not over - check if game is won
        except selenium_exceptions.NoSuchElementException:

            try:
                game_won = driver.find_element_by_css_selector("div.game-message.game-won")
                if game_won:
                    print(f"WOW! YOU'VE WON THE GAME!!! CONGRATULATIONS! Your result is {result}")
                    break

            # if neither over nor won - play game
            except selenium_exceptions.NoSuchElementException:
                direction = random.randint(1, 4)

                if direction == 1:
                    tile.send_keys(Keys.UP)
                elif direction == 2:
                    tile.send_keys(Keys.RIGHT)
                elif direction == 3:
                    tile.send_keys(Keys.DOWN)
                elif direction == 4:
                    tile.send_keys(Keys.LEFT)


game_url = "https://gabrielecirulli.github.io/2048/"
play_game(game_url)

