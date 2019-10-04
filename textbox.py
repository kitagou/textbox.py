import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QTextEdit, QHBoxLayout, QPushButton, QLabel)
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
import tweepy
from tweepy.auth import OAuthHandler


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.initTwitterAccount()
        self.initUI()
        self.initGui()        

    def initTwitterAccount(self):
        consumer_key = "HJbXGzA8ETRRwt8oDxz5JlWWP"
        consumer_secret = "QUnhmJwvjZiJZOzhqO7JsREZ6Qk2vm8xgA9Ey0llDnsxS8ukY8"
        access_token = "716441363730968576-fUhXjhYy2aLpvCWoddqcKRjhgplY1Ei"
        access_token_secret = "2uBQCqhpD0gitGbaLMA0of5gYq1LKDZ3r2tFtnx0FfvqJ"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        auth.secure = True
        # ツイートを送信するためのapiを取得
        self.api = tweepy.API(auth)
    
    def initUI(self):      
        self.setGeometry(10, 10, 400, 400)
        self.setWindowTitle('Sample_text')

        self.w = QWidget()

        self.label = QLabel('')
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        self.w.setLayout(hbox)
        self.setCentralWidget(self.w)

    def initGui(self):
        self.text = QTextEdit(self)
        self.text.setGeometry(15, 15, 300, 150)
        self.button = QPushButton('tweet', self)
        self.button.setGeometry(170, 200, 120, 30)
        # buttonを押したときのイベントをcountupに指定
        self.button.clicked.connect(self.countup)
        
        self.show()
    
    def countup(self):
        text = self.text.toPlainText()
        # self.label.setText(text)
        self.api.update_status(text)
            
        self.text.clear()


def main():
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
