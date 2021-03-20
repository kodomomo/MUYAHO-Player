import os
import boto3


class SqsObserver:
    def __init__(self, music_player):
        self.queue_url = os.getenv("SQS_ADDRESS")
        self.client = boto3.client(
            "sqs",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
            region_name="ap-northeast-2"
        )
        self.music_player = music_player

    def get_music(self):
        while True:
            print("GET MUSIC IS RUN")
            pass
            # if self.get_messages():
            #     self.music_player.play("Query")

    def get_messages(self):
        response = self.client.receive_message(
            QueueUrl=self.queue_url,
            WaitTimeSeconds=3
        )

        try:
            for message in response["Messages"]:
                self.client.delete_message(
                    QueueUrl=self.queue_url,
                    ReceiptHandle=message["ReceiptHandle"]
                )
                return True
        except KeyError:
            return False

    def purge(self):
        self.client.purge_queue(QueueUrl=self.queue_url)