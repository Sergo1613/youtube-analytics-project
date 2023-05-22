from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Video:
    video_id = '9lO06Zxhu88'

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            youtube = build('youtube', 'v3', developerKey="AIzaSyCiYdDqOKDUKPRnJF7023I4NwZGsCrQqpo")
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            if 'items' in video_response and len(video_response['items']) > 0:
                self.video_title: str = video_response['items'][0]['snippet']['title']
                self.view_count: int = video_response['items'][0]['statistics']['viewCount']
                self.like_count: int = video_response['items'][0]['statistics']['likeCount']
                self.comment_count: int = video_response['items'][0]['statistics']['commentCount']
            else:
                self.video_title = None
                self.view_count = None
                self.like_count = None
                self.comment_count = None
        except HttpError:
            self.video_title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None

        self.url = f"https://www.youtube.com/watch?v={video_id}"


    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):
    def __init__(self, video_id, video_playlist):

        super().__init__(video_id)
        self.video_playlist = video_playlist

    def __str__(self):
        return f"{self.video_title}"










