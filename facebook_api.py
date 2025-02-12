# facebook_api.py
import requests
from config import FACEBOOK_ACCESS_TOKEN, FACEBOOK_PAGE_ID

class FacebookAPI:
    BASE_URL = "https://graph.facebook.com/v16.0"

    def __init__(self):
        """
        Initialize the FacebookAPI class with access token and page ID.
        """
        self.access_token = FACEBOOK_ACCESS_TOKEN
        self.page_id = FACEBOOK_PAGE_ID

    def post_to_facebook(self, message):
        """
        Publish a text-only post to the Facebook page.

        Args:
            message (str): The content of the post.

        Returns:
            None
        """
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

    def upload_photo(self, image_path, caption=""):
        """
        Upload a photo to the Facebook page.

        Args:
            image_path (str): Path to the image file.
            caption (str): Optional caption for the photo.

        Returns:
            None
        """
        url = f"{self.BASE_URL}/{self.page_id}/photos"
        with open(image_path, 'rb') as image_file:
            files = {
                'source': image_file
            }
            params = {
                "caption": caption,
                "access_token": self.access_token
            }
            response = requests.post(url, files=files, data=params)
        
        if response.status_code == 200:
            print("Photo successfully uploaded to Facebook!")
        else:
            print(f"Failed to upload photo: {response.json()}")

    def upload_video(self, video_path, description=""):
        """
        Upload a video to the Facebook page.

        Args:
            video_path (str): Path to the video file.
            description (str): Optional description for the video.

        Returns:
            None
        """
        url = f"{self.BASE_URL}/{self.page_id}/videos"
        with open(video_path, 'rb') as video_file:
            files = {
                'file_url': video_file
            }
            params = {
                "description": description,
                "access_token": self.access_token
            }
            response = requests.post(url, files=files, data=params)
        
        if response.status_code == 200:
            print("Video successfully uploaded to Facebook!")
        else:
            print(f"Failed to upload video: {response.json()}")

    def get_post_analytics(self, post_id):
        """
        Fetch analytics for a specific post.

        Args:
            post_id (str): The ID of the post.

        Returns:
            dict: Analytics data (e.g., impressions, engaged users).
        """
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
            return None