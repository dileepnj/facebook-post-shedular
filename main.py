# main.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QLineEdit, QFileDialog
)
from scheduler import Scheduler
from facebook_api import FacebookAPI
from db import Database

class SocialMediaManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Social Media Manager")
        self.setGeometry(100, 100, 400, 400)

        # Initialize components
        self.scheduler = Scheduler()
        self.facebook_api = FacebookAPI()
        self.db = Database()

        # Setup UI
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Post Content Input
        self.post_input = QTextEdit(self)
        self.post_input.setPlaceholderText("Enter your post content here...")
        layout.addWidget(self.post_input)

        # Schedule Time Input
        self.time_input = QLineEdit(self)
        self.time_input.setPlaceholderText("Enter schedule time (YYYY-MM-DD HH:MM)")
        layout.addWidget(self.time_input)

        # Schedule Post Button
        schedule_button = QPushButton("Schedule Post", self)
        schedule_button.clicked.connect(self.schedule_post)
        layout.addWidget(schedule_button)

        # Post Now Button
        post_now_button = QPushButton("Post Now", self)
        post_now_button.clicked.connect(self.post_now)
        layout.addWidget(post_now_button)

        # Upload Photo Button
        photo_button = QPushButton("Upload Photo", self)
        photo_button.clicked.connect(self.upload_photo)
        layout.addWidget(photo_button)

        # Upload Video Button
        video_button = QPushButton("Upload Video", self)
        video_button.clicked.connect(self.upload_video)
        layout.addWidget(video_button)

        # Set Layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def schedule_post(self):
        """
        Schedule a post to be published at a later time.
        """
        content = self.post_input.toPlainText()
        schedule_time = self.time_input.text()
        if content and schedule_time:
            self.scheduler.schedule(content, schedule_time)
            self.post_input.clear()
            self.time_input.clear()
            print(f"Post scheduled for {schedule_time}")
        else:
            print("Please enter both post content and schedule time.")

    def post_now(self):
        """
        Publish a text-only post immediately.
        """
        content = self.post_input.toPlainText()
        if content:
            self.facebook_api.post_to_facebook(content)
            self.post_input.clear()
            print("Post published immediately.")
        else:
            print("Please enter post content.")

    def upload_photo(self):
        """
        Open a file dialog to select an image and upload it to Facebook.
        """
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.jpg *.jpeg *.png)"
        )
        if image_path:
            caption = self.post_input.toPlainText()
            self.facebook_api.upload_photo(image_path, caption)
            self.post_input.clear()
            print("Photo uploaded successfully!")

    def upload_video(self):
        """
        Open a file dialog to select a video and upload it to Facebook.
        """
        file_dialog = QFileDialog()
        video_path, _ = file_dialog.getOpenFileName(
            self, "Select Video", "", "Video Files (*.mp4 *.mov *.avi)"
        )
        if video_path:
            description = self.post_input.toPlainText()
            self.facebook_api.upload_video(video_path, description)
            self.post_input.clear()
            print("Video uploaded successfully!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SocialMediaManagerApp()
    window.show()
    sys.exit(app.exec_())