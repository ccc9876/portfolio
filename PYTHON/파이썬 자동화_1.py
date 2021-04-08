import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PIL import ImageGrab
import datetime
import time


# QT5 사용하여 반자동화 테스트 
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # 전체적인 화면 크기 , 모니터 해상도 1920 * 1080 사이즈 구성으로 위치 고정 
        self.setWindowIcon(QIcon("C:/Users/F190033/icon/radio.png"))
        self.setWindowTitle('DAB')
        self.setGeometry(1800, 1000, 1800, 1000)

        # 위치 중앙으로 고정 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        
        btn0 = QPushButton('LOG', self)
        btn0.move(1600, 50)
        btn0.resize(300, 32)
        btn0.setStyleSheet('background-color:rgb(1, 166, 255);')

        self.move(qr.topLeft())
        self.initUI()

    def initUI(self):

        # 버튼 이름,위치,색상설정 하고 클릭시 함수 연결 
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Frequency Tune/001")
        self.b1.move(20,50)
        self.b1.resize(300,32)
        self.b1.clicked.connect(self.t001)

        ##############################################################
        ###################### PASS/FAIL LABEL########################
        ##############################################################
        
        
        
        btn101 = QPushButton('PASS/FAIL LIST', self)
        btn101.move(20, 510)
        btn101.resize(300, 32)
        btn101.setStyleSheet('background-color:rgb(1, 166, 255);')

        #로그 파일 읽어온 부븐을 GUI 상에 라벨로 읽어옴 
        self.label99 = QtWidgets.QLabel(self)
        self.label99.setText("log:")

        #라벨 위치,사이즈
        self.label99.move(1400, 50)
        self.label99.resize(500, 200)

        self.text = QTextBrowser(self)
        self.text.resize(900,700)
        self.text.move(1400,200)
        self.text.setFontPointSize(14)
        self.text.setStyleSheet("border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px")



    ######################################################################
    ################ DAB btn conncet event ###############################
    ######################################################################

    def t001(self):
        self.text.setText("")
        #고정된 로그 위치에 파일들을 읽어옴
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        #메인 화면을 스크린샷 하여 스크린샷 기준의 좌표(1763,434) 색상을 RGB로 저장함 
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        #메인 RGB 값이 맞으면은 pyautogui로 테스트 셋팅값 입력
        if im == tera_color:
            pyautogui.typewrite('f 0 174928 1')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "tune" # 주파수가 잡혀야 
                        self.text.append(line)
                        #라벨로 테스트 성공/실패 판단
                        if serach in line:
                            self.label1.setText("Frequency Tune/001:  PASS")
                            self.label1.setStyleSheet("Color : blue")
                            break
                        else:
                            self.label1.setText("Frequency Tune/001:  FAIL")
                            self.label1.setStyleSheet("Color : red")
                break
        #메인 RGB 값이 다르면 Q메세지 박스로 경고창 이벤트 나오면서 테스트 실행 불가
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()
