import json
from googleapiclient.discovery import build


class Channel:
    obj = 0

    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id
        self.title = self.get_info()['items'][0]['snippet']['title']
        self.description = self.get_info()['items'][0]['snippet']['description']
        self.customUrl = self.get_info()['items'][0]['snippet']['customUrl']
        self.followers = self.get_info()['items'][0]['statistics']['subscriberCount']
        self.views = self.get_info()['items'][0]['statistics']['viewCount']
        self.videos = self.get_info()['items'][0]['statistics']['videoCount']
        Channel.obj = self

    def get_info(self) -> str:
        api_key = 'AIzaSyCemWJ_acfZl3wE85blGxwZ3SkCwCTRGsk'
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = self.__channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self) -> None:
        print(json.dumps(self.get_info(), indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.obj

    def to_json(self, filename):
        with open(filename, 'w') as outfile:
            data = {
                "channel_id": self.channel_id,
                "title": self.title,
                "description": self.description,
                "url": self.customUrl,
                "subscribers": self.followers,
                "video_count": self.videos,
                "views": self.views,
            }
            json.dump(data, outfile)


    @property
    def channel_id(self):
        return self.__channel_id


