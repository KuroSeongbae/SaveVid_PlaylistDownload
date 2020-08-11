from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

def InputFunction(message, inputType):
    print(message)
    x = None
    while type(x) != type(inputType):
        print("A ", type(inputType), " is required!")
        x = input()
        try:
            x = type(inputType)(x)
        except:
            print("Wrong input")
    return x

path = os.path.join(os.path.dirname(__file__), 'geckodriver.exe')
driver = webdriver.Firefox(executable_path=path)
web_url = InputFunction("Give in the URL of the first element in the Playlist: ", "")
web_url = web_url[1:]
driver.get(web_url)
try:
    while (True):
        time.sleep(12)
        download_button = driver.find_element_by_id('buybuddy-download-mp3')
        download_button.click()
        link = driver.find_element_by_class_name("ytp-next-button")
        link.click()
        url = driver.current_url
        if ("index=" not in url and "list=" not in url):
            break;
except:
    print("The page needed too long to load: Try setting a higher waiting time.")
print("The last element in the Playlist was reached.")
driver.close()