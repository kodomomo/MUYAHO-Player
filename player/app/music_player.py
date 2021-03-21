import json
from time import sleep

import requests

from player.app.selenium_factory import create_driver


class MusicPlayer:
    def __init__(self):
        self.driver = create_driver()
        pass

    def play(self, query):
        driver = self.driver
        html = requests.get('https://www.googleapis.com/youtube/v3/search?part=id&key=AIzaSyDrXIG0YwGgN2XQfCHo8Iaa66aI5hvOx-U&q=' + query + ' 노래').text
        result = json.loads(html)['items']
        if len(result) == 0:
            return
        time = 0
        for i in result:
            video_id = i['id']['videoId']
            driver.get('https://www.youtube.com/embed/' + video_id)
            driver.implicitly_wait(5)
            driver.find_element_by_class_name('ytp-large-play-button').click()
            time = int(driver.find_element_by_class_name('ytp-progress-bar').get_attribute('aria-valuemax'))
            if len(driver.find_elements_by_class_name('ytp-error-icon-container')) == 0:
                break
        sleep(time)
        pass
