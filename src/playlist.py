from datetime import datetime
import datetime
import isodate
from googleapiclient.discovery import build


class PlayList:
    def __init__(self, pl_id):
        self.pl_id = pl_id
        self.title = self.title()
        self.url = f"https://www.youtube.com/playlist?list={self.pl_id}"

    def title(self):
        api_key = 'AIzaSyDpDq-CsLp0jkDsSN_sO-hJLFrG8tag9Mw'
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_info = youtube.playlists().list( part='snippet', id=self.pl_id).execute()
        return  playlist_info['items'][0]['snippet']['title']

    @property
    def total_duration(self):
        api_key = 'AIzaSyCemWJ_acfZl3wE85blGxwZ3SkCwCTRGsk'
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_id = self.pl_id
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails',
                                                       maxResults=50, ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        s = 0
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            duration = str(duration)
            duration = duration.split(':')
            s += (int(duration[0]) * 60 * 60) + (int(duration[1]) * 60) + (int(duration[2]))
        td = datetime.timedelta(0, s, 0)
        return td

    def total_seconds(self):
        api_key = 'AIzaSyCemWJ_acfZl3wE85blGxwZ3SkCwCTRGsk'
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_id = self.pl_id
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails',
                                                       maxResults=50, ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        s = 0
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            duration = str(duration)
            duration = duration.split(':')
            s += (int(duration[0]) * 60 * 60) + (int(duration[1]) * 60) + (int(duration[2]))
        return s


    def show_best_video(self):
        max = 0
        url = ''
        api_key = 'AIzaSyCemWJ_acfZl3wE85blGxwZ3SkCwCTRGsk'
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_id = self.pl_id
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50,).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='statistics', id=','.join(video_ids)).execute()
        for video in video_response['items']:
            like_count = int(video['statistics']['likeCount'])
            if like_count > max:
                max = like_count
                url = video['id']
        return f"https://youtu.be/{url}"