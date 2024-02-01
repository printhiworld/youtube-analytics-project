from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        try:
            self.__video_id = video_id
            self.title = self.get_info()['items'][0]['snippet']['title']
            self.customUrl = f'https://www.youtube.com/watch?v={video_id}'
            self.views = self.get_info()['items'][0]['statistics']['viewCount']
            self.likes = self.get_info()['items'][0]['statistics']['likeCount']
        except IndexError:
            self.__video_id = video_id
            self.title = None
            self.customUrl = None
            self.views = None
            self.likes = None

    def get_info(self) -> str:
        api_key = 'AIzaSyCemWJ_acfZl3wE85blGxwZ3SkCwCTRGsk'

        youtube = build('youtube', 'v3', developerKey=api_key)
        video_id = self.__video_id
        video_response = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
        return video_response

    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):
    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.__pl_id = pl_id