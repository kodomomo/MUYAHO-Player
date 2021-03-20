from player.app.sqs_observer import SqsObserver


class Player:
    def __init__(self):
        self.observer = SqsObserver(
            music_player=None)

    def run(self):
        self.observer.get_music()
