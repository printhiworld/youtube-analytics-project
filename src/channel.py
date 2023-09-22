import json
import os

from googleapiclient.discovery import build

import isodate

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key = 'AIzaSyCemWJ_acfZl3wE85blGxwZ3SkCwCTRGsk'
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

