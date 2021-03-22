import os
import boto3


class SqsObserver:
    def __init__(self, music_player):
        self.queue = ["https://www.youtube.com/watch?v=Rc0WOYHReSA", "kda pop/stars"]
        self.queue_url = os.getenv("SQS_ADDRESS")
        # self.client = boto3.client(
        #     "sqs",
        #     aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        #     aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        #     region_name="ap-northeast-2"
        # )
        self.music_player = music_player

    def get_music(self):
        a = 0
        while True:
            print(self, a)
            self.music_player.play(self.get_messages())
            a += 1

    def get_messages(self):
        m = self.queue.pop()
        print(self.queue)
        print(f"que : {m}")
        return m
    #     response = self.client.receive_message(
    #         QueueUrl=self.queue_url,
    #         WaitTimeSeconds=3
    #     )
    #
    #     try:
    #         for message in response["Messages"]:
    #             self.client.delete_message(
    #                 QueueUrl=self.queue_url,
    #                 ReceiptHandle=message["ReceiptHandle"]
    #             )
    #             return True
    #     except KeyError:
    #         return False

    def purge(self):
        self.client.purge_queue(QueueUrl=self.queue_url)