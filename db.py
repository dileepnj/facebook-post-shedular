# db.py
import sqlite3

class Database:
    def __init__(self, db_name="social_media.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the 'posts' table if it doesn't exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                schedule_time TEXT NOT NULL,
                media_path TEXT,
                is_video INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_post(self, content, schedule_time, media_path=None, is_video=False):
        """
        Add a new post to the database.

        Args:
            content (str): The text content of the post.
            schedule_time (str): The scheduled time in "YYYY-MM-DD HH:MM" format.
            media_path (str, optional): Path to the media file (image or video).
            is_video (bool, optional): Whether the media is a video.

        Returns:
            None
        """
        self.cursor.execute("""
            INSERT INTO posts (content, schedule_time, media_path, is_video)
            VALUES (?, ?, ?, ?)
        """, (content, schedule_time, media_path, int(is_video)))
        self.conn.commit()

    def get_scheduled_posts(self):
        """
        Retrieve all scheduled posts from the database.

        Returns:
            list: A list of tuples containing post details.
        """
        self.cursor.execute("SELECT * FROM posts")
        return self.cursor.fetchall()

    def delete_post(self, post_id):
        """
        Delete a post from the database.

        Args:
            post_id (int): The ID of the post to delete.

        Returns:
            None
        """
        self.cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        self.conn.commit()