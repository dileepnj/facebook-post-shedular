# scheduler.py
import threading
import time
from datetime import datetime
from facebook_api import FacebookAPI
from db import Database

class Scheduler:
    def __init__(self):
        self.db = Database()
        self.facebook_api = FacebookAPI()
        self.running = True

    def schedule(self, content, schedule_time, media_path=None, is_video=False):
        """
        Schedule a post or media upload.

        Args:
            content (str): The text content of the post.
            schedule_time (str): The scheduled time in "YYYY-MM-DD HH:MM" format.
            media_path (str, optional): Path to the media file (image or video).
            is_video (bool, optional): Whether the media is a video.

        Returns:
            None
        """
        self.db.add_post(content, schedule_time, media_path, is_video)
        threading.Thread(target=self.check_and_post).start()

    def check_and_post(self):
        """
        Periodically check for scheduled posts and publish them.
        """
        while self.running:
            posts = self.db.get_scheduled_posts()
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            for post in posts:
                post_id, content, schedule_time, media_path, is_video = post
                if schedule_time <= now:
                    if media_path:
                        if is_video:
                            self.facebook_api.upload_video(media_path, description=content)
                        else:
                            self.facebook_api.upload_photo(media_path, caption=content)
                    else:
                        self.facebook_api.post_to_facebook(content)
                    self.db.delete_post(post_id)
            time.sleep(60)  # Check every minute