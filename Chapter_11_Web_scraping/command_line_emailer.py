'''
Write a program that takes an email address and string of text on the command
line and then, using Selenium, logs into your email account and
sends an email of the string to the provided address. (You might want to set
up a separate email account for this program.)
'''

from selenium import webdriver
import sys, time


def send_email(email_service, to_email, from_email, password, text):
    """
    Sends email using provided email and text from command line.
    If values are missing, it's using a default recipient email and text.\n
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

    # enter email
    email_field = driver.find_element_by_id("identifierId")
    email_field.clear()
    email_field.send_keys(from_email)

    next_button_email = driver.find_element_by_id("identifierNext")
    next_button_email.click()

    time.sleep(2)

    # enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    next_button_password = driver.find_element_by_id("passwordNext")
    next_button_password.click()
    
    time.sleep(5)

    # open new e-mail window
    compose_button = driver.find_element_by_css_selector(".aic .z0 div")
    compose_button.click()

    time.sleep(5)

    # enter recipient email
    recipient_field = driver.find_element_by_css_selector(".oj>div>textarea")
    recipient_field.clear()
    recipient_field.send_keys(to_email)

    # enter email text
    text_element = driver.find_element_by_css_selector(".Ar.Au div")
    text_element.clear()
    text_element.send_keys(text)

    # send the email
    send_button = driver.find_element_by_css_selector(".dC div")
    send_button.click()
    print(f"Email to {recipient_email} is sent")

    time.sleep(5)
    driver.quit()


command_line_string = " ".join(sys.argv[1:])

# use cmd vars if it's not empty
if command_line_string:
    recipient_email = command_line_string[1]
    email_text = command_line_string[2:]

# use default values if cmd is empty
else:
    recipient_email = "nonexistent-email@panda.panda.panda"
    email_text = "Just a test e-mail. Please don't mind."

gmail_service = "https://gmail.com"
my_email = "test@gmail.com"
my_password = "test123*"

send_email(gmail_service, recipient_email, my_email, my_password, email_text)

