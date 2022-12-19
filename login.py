# selenium 4

from chrome import ChromeBrowser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os.path
import os
import dotenv
import time


# Extract inputs for username and password and id
def findUsernameInput(browser: ChromeBrowser) -> str:
    '''Extracts the username input from the login page'''
    try:
        inputUsername = browser.find_element(
            By.XPATH, "//input[@name='Login[username]' and @id='login_username']")
    except NoSuchElementException:
        print("Username field not found ❌")
    return inputUsername


def findPasswordInput(browser: ChromeBrowser) -> str:
    '''Extracts the password input from the login page'''
    try:
        inputPassword = browser.find_element(
            By.XPATH, "//input[@name='Login[password]'and @id='login_password'] ")
    except NoSuchElementException:
        print("Password field not found ❌")
    return inputPassword


# define username and password
def fillUsernameInput(inputUsername) -> None:
    '''Fills the username input with the username'''
    dotenv.load_dotenv()
    username = os.getenv("UP4U_USERNAME", )
    inputUsername.send_keys(username)


# Fill inputs with username and password
def fillPassswordInput(inputPassword) -> None:
    '''Fills the password input with the password'''
    dotenv.load_dotenv()
    password = os.getenv("UP4U_PASSWORD", )
    inputPassword.send_keys(password)

# Click on login button


def clickLoginButton(browser: ChromeBrowser) -> None:
    '''Clicks on the login button'''
    try:
        loginButton = browser.find_element(By.ID, "login-button")
        loginButton.click()
    except NoSuchElementException:
        print("Login button not found ❌")


def login(browser: ChromeBrowser) -> str:
    '''Logs in to the UP4U page'''
    try:
        fillUsernameInput(findUsernameInput(browser))
        fillPassswordInput(findPasswordInput(browser))
        clickLoginButton(browser)
        if "User or Password incorrect." in browser.page_source or "contraseña no puede estar vacío." in browser.page_source:
            print("Error message found, login failed ❌")
        else:
            print(
                f"Login successful ✅\nWaiting for the page to load... 🕒\nLet me sleep for 3 seconds\nZZzzzz...")
            time.sleep(3)
            print("Page loaded ✅")
            url = browser.current_url
    except Exception as e:
        print(f'Login failed ❌\n{e}')
    return url


# # copy the page source to horario.html
# with open("horario.html", "w") as f:
#     f.write(browser.page_source)
