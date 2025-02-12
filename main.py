# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QLineEdit
from scheduler import Scheduler
from facebook_api import FacebookAPI
from db import Database

class SocialMediaManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Social Media Manager")
        self.setGeometry(100, 100, 400, 300)

        # Initialize components
        self.scheduler = Scheduler()
        self.facebook_api = FacebookAPI()
        self.db = Database()

        # Setup UI
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.post_input = QTextEdit(self)
        self.post_input.setPlaceholderText("Enter your post content here...")
        layout.addWidget(self.post_input)

        self.time_input = QLineEdit(self)
        self.time_input.setPlaceholderText("Enter schedule time (YYYY-MM-DD HH:MM)")
        layout.addWidget(self.time_input)

        schedule_button = QPushButton("Schedule Post", self)
        schedule_button.clicked.connect(self.schedule_post)
        layout.addWidget(schedule_button)

        post_now_button = QPushButton("Post Now", self)
        post_now_button.clicked.connect(self.post_now)
        layout.addWidget(post_now_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def schedule_post(self):
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
        content = self.post_input.toPlainText()
        if content:
            self.facebook_api.post_to_facebook(content)
            self.post_input.clear()
            print("Post published immediately.")
        else:
            print("Please enter post content.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SocialMediaManagerApp()
    window.show()
    sys.exit(app.exec_())