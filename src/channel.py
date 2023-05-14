import json
import os
from googleapiclient.discovery import build



class Channel:
    """Класс для ютуб-канала"""

    API_KEY = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info["items"][0]["snippet"]["title"]
        self.description = self.channel_info["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA"
        self.subscriber_count = self.channel_info["items"][0]["statistics"].get("subscriberCount")
        self.video_count = self.channel_info["items"][0]["statistics"].get("videoCount")
        self.view_count = self.channel_info["items"][0]["statistics"].get("viewCount")



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel_info, indent=2, ensure_ascii=False))