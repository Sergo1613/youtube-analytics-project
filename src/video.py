from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Video:
    video_id = '9lO06Zxhu88'

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            youtube = build('youtube', 'v3', developerKey="AIzaSyCiYdDqOKDUKPRnJF7023I4NwZGsCrQqpo")
            video = youtube.captions().list(videoId=self.video_id, part='snippet').execute()
        except HttpError:
            self.title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None

        self.url = f"https://www.youtube.com/watch?v={video_id}"


    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):
    def __init__(self, video_id, video_playlist):

        super().__init__(video_id)
        self.video_playlist = video_playlist

    def __str__(self):
        return f"{self.title}"










