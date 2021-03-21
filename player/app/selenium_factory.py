from selenium import webdriver


def create_driver():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    return driver

