import json
import os
from googleapiclient.discovery import build



class Channel:
    """Класс для ютуб-канала"""

    API_KEY = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.channel_info = self.youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info["items"][0]["snippet"]["title"]
        self.description = self.channel_info["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA"
        self.subscriber_count = self.channel_info["items"][0]["statistics"].get("subscriberCount")
        self.video_count = self.channel_info["items"][0]["statistics"].get("videoCount")
        self.view_count = self.channel_info["items"][0]["statistics"].get("viewCount")


    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = self.youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel_info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey='AIzaSyCiYdDqOKDUKPRnJF7023I4NwZGsCrQqpo')
        return youtube

    def to_json(self, filename):
        data = {
            "channel_id": self._channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count

        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return data