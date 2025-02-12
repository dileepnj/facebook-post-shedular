# facebook_api.py
import requests
from config import FACEBOOK_ACCESS_TOKEN, FACEBOOK_PAGE_ID

class FacebookAPI:
    BASE_URL = "https://graph.facebook.com/v16.0"

    def __init__(self):
        self.access_token = FACEBOOK_ACCESS_TOKEN
        self.page_id = FACEBOOK_PAGE_ID

    def post_to_facebook(self, message):
        url = f"{self.BASE_URL}/{self.page_id}/feed"
        params = {
            "message": message,
            "access_token": self.access_token
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print("Post successfully published to Facebook!")
        else:
            print(f"Failed to post: {response.json()}")

    def get_post_analytics(self, post_id):
        url = f"{self.BASE_URL}/{post_id}/insights"
        params = {
            "metric": "post_impressions,post_engaged_users",
            "access_token": self.access_token
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch analytics: {response.json()}")