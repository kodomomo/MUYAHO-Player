import json
from time import sleep

import requests


class MusicPlayer:
    def __init__(self, driver):
        self.driver = driver
        pass

    def play(self, query: str):
        driver = self.driver
        if query.startswith('http'):
            video_id = query.split('?v=')[1]
            time = self.play_by_video_id(video_id)
            sleep(time)
            return
        html = requests.get(
            'https://www.googleapis.com/youtube/v3/search?part=id&key=AIzaSyDrXIG0YwGgN2XQfCHo8Iaa66aI5hvOx-U&q=' + query).text
        result = json.loads(html)['items']
        if len(result) == 0:
            return

        for i in result:
            video_id = i['id']['videoId']
            time = self.play_by_video_id(video_id)
            if time != 0:
                sleep(time)
                return

    def play_by_video_id(self, video_id) -> int:
        driver = self.driver
        driver.get('https://www.youtube.com/embed/' + video_id)
        driver.implicitly_wait(5)
        driver.find_element_by_class_name('ytp-large-play-button').click()
        if len(driver.find_elements_by_class_name('ytp-error-icon-container')) != 0:
            return 0
        return int(driver.find_element_by_class_name('ytp-progress-bar').get_attribute('aria-valuemax'))
