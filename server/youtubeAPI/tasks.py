from celery import shared_task
from .models import API_Key, Video
import requests


request_url = "https://youtube.googleapis.com/youtube/v3/search"


def create_video_data(video_list):

    for i in range(len(video_list.json()["items"])):
        videos = video_list.json()["items"]
        Video.objects.get_or_create(
            title=videos[i]["snippet"]["title"],
            description=videos[i]["snippet"]["description"],
            published_at=videos[i]["snippet"]["publishedAt"],
            video_thumbnail=videos[i]["snippet"]["thumbnails"]["high"]["url"],
            youtube_id=videos[i]["id"]["videoId"]
        )


def get_video_list(valid_api_key):
    return requests.get(
        url=request_url,
        params={
            'part': 'snippet',
            'maxResults': 50,
            'q': 'football',
            'type': 'video',
            'publishedAfter': '2022-07-07T00:00:00Z',
            'order': 'date',
            'key': valid_api_key.key
        }
    )


@shared_task()
def youtube_get_video_data():

    while True:
        valid_api_key = API_Key.objects.filter(quota_exceeded=False).first()

        if valid_api_key != None:
            video_list = get_video_list(valid_api_key)

            if video_list.status_code == 200:
                create_video_data(video_list)
                break

            elif video_list.status_code == 403:
                valid_api_key.quota_exceeded = True
                valid_api_key.save()
                print("Quota exceeded for this API key!")

            else:
                print("Error occured while API call!")

        else:
            print("All API Keys have exhausted! Please add new API Keys")
            break
