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

    def schedule(self, content, schedule_time):
        self.db.add_post(content, schedule_time)
        threading.Thread(target=self.check_and_post).start()

    def check_and_post(self):
        while self.running:
            posts = self.db.get_scheduled_posts()
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            for post in posts:
                post_id, content, schedule_time = post
                if schedule_time <= now:
                    self.facebook_api.post_to_facebook(content)
                    self.db.delete_post(post_id)
            time.sleep(60)  # Check every minute