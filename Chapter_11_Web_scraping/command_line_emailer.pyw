'''
Write a program that takes an email address and string of text on the command
line and then, using Selenium, logs into your email account and
sends an email of the string to the provided address. (You might want to set
up a separate email account for this program.)
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import sys

def send_email(email_service, to_email, from_email, password, text):
    """
    Sends email letter using provided email and text from command line.
    If values are missing, it's using a default recipient email and text.
    Used browser - Firefox.\n
    :param email_service: link
    :param to_email: valid email
    :param from_email: valid email
    :param password:
    :param text:
    :return: nothing
    """

    # open browser
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(email_service)
    print(f"Opened {email_service} to send an e-mail")

    wait = WebDriverWait(driver, 10)

    # enter email
    email_field = wait.until(ec.visibility_of_element_located((By.ID, "identifierId")))
    email_field.clear()
    email_field.send_keys(from_email)

    next_button_email = wait.until(ec.visibility_of_element_located((By.ID, "identifierNext")))
    next_button_email.click()

    # enter password
    password_field = wait.until(ec.visibility_of_element_located((By.NAME, "password")))
    password_field.clear()
    password_field.send_keys(password)

    next_button_password = wait.until(ec.visibility_of_element_located((By.ID, "passwordNext")))
    next_button_password.click()

    # open new email window
    compose_button = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".aic .z0 div")))
    compose_button.click()

    # enter recipient email
    recipient_field = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".oj>div>textarea")))
    recipient_field.clear()
    recipient_field.send_keys(to_email)

    # enter email text
    text_element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".Ar.Au div")))
    text_element.clear()
    text_element.send_keys(text)

    # send the email
    send_button = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".dC div")))
    send_button.click()
    print(f"Email to {recipient_email} is sent")

    driver.quit()


# use cmd vars if it's not empty
if sys.argv:
    recipient_email = sys.argv[1]
    email_text = sys.argv[2:]

# use default values if cmd is empty
else:
    recipient_email = "nonexistent-email@panda.panda.panda"
    email_text = "Just a test e-mail. Please don't mind."

gmail_service = "https://gmail.com"
my_email = "test@gmail.com"
my_password = "test123*"

send_email(gmail_service, recipient_email, my_email, my_password, email_text)

