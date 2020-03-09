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
        consumer_key = "＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊"
        consumer_secret = "＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊"
        access_token = "＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊"
        access_token_secret = "＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        auth.secure = True
        # ツイートを送信するためのapiを取得
        self.api = tweepy.API(auth)
        # アカウント関連
    def initUI(self):      
        self.setGeometry(10, 10, 400, 400)
        self.setWindowTitle('Sample_text')

        self.w = QWidget()

        self.label = QLabel('')
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        self.w.setLayout(hbox)
        self.setCentralWidget(self.w)
       # 投稿画面設定 
    def initGui(self):
        self.text = QTextEdit(self)
        self.text.setGeometry(15, 15, 300, 150)
        self.button = QPushButton('tweet', self)
        self.button.setGeometry(170, 200, 120, 30)
        # buttonを押したときのイベントをcountupに指定
        self.button.clicked.connect(self.countup)
        
        self.show()
       # TLの画面設定
    def countup(self):
        text = self.text.toPlainText()
        self.label.setText(text)         
        self.api.update_status(text)
        self.listWidget.insertItem(0, text)   
        self.text.clear() 
       #投稿後投稿画面から文字を消す         

def main():
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
