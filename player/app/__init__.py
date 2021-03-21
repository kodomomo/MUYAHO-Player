from player.app.music_player import MusicPlayer
from player.app.sqs_observer import SqsObserver

from player.app.selenium_factory import create_driver


class Player:
    def __init__(self):
        self.driver = create_driver()
        self.music_player = MusicPlayer(self.driver)
        self.observer = SqsObserver(music_player=self.music_player)

    def run(self):
        self.observer.get_music()


def create_app():
    app = Player()
    return app
