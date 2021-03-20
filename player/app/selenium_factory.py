from selenium import webdriver


def create_driver():
    driver = webdriver.Chrome(executable_path='C:/Users/user/PycharmProjects/MUYAHO-Player/chromedriver.exe')
    return driver

