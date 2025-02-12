# db.py
import sqlite3

class Database:
    def __init__(self, db_name="social_media.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                schedule_time TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_post(self, content, schedule_time):
        self.cursor.execute("""
            INSERT INTO posts (content, schedule_time)
            VALUES (?, ?)
        """, (content, schedule_time))
        self.conn.commit()

    def get_scheduled_posts(self):
        self.cursor.execute("SELECT * FROM posts")
        return self.cursor.fetchall()

    def delete_post(self, post_id):
        self.cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        self.conn.commit()