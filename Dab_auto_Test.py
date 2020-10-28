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

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowIcon(QIcon("C:/Users/F190033/icon/radio.png"))
        self.setWindowTitle('DAB')
        self.setGeometry(1800, 1000, 1800, 1000)

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

        btn0 = QPushButton('DAB MODE', self)
        btn0.move(20, 10)
        btn0.resize(300, 32)
        btn0.setStyleSheet('background-color:rgb(1, 166, 255);')

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Frequency Tune/001")
        self.b1.move(20,50)
        self.b1.resize(300,32)
        self.b1.clicked.connect(self.t001)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Frequency Tune/002")
        self.b2.move(20, 80)
        self.b2.resize(300, 32)
        self.b2.clicked.connect(self.t002)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Frequency Tune/003")
        self.b3.move(20, 110)
        self.b3.resize(300, 32)
        self.b3.clicked.connect(self.t003)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Select service/004")
        self.b4.move(20, 140)
        self.b4.resize(300, 32)
        self.b4.clicked.connect(self.t004)

        self.b5 = QtWidgets.QPushButton(self)
        self.b5.setText("Select service/005")
        self.b5.move(20, 170)
        self.b5.resize(300, 32)
        self.b5.clicked.connect(self.t005)

        self.b6 = QtWidgets.QPushButton(self)
        self.b6.setText("Select service/006")
        self.b6.move(20, 200)
        self.b6.resize(300, 32)
        self.b6.clicked.connect(self.t006)

        self.b7 = QtWidgets.QPushButton(self)
        self.b7.setText("Select service/007")
        self.b7.move(20, 230)
        self.b7.resize(300, 32)
        self.b7.clicked.connect(self.t007)

        self.b8 = QtWidgets.QPushButton(self)
        self.b8.setText("Select service/008")
        self.b8.move(20, 260)
        self.b8.resize(300, 32)
        self.b8.clicked.connect(self.t008)

        self.b9 = QtWidgets.QPushButton(self)
        self.b9.setText("AutoScan/009")
        self.b9.move(20, 290)
        self.b9.resize(300, 32)
        self.b9.clicked.connect(self.t009)

        self.b10 = QtWidgets.QPushButton(self)
        self.b10.setText("AutoScan/010")
        self.b10.move(20, 320)
        self.b10.resize(300, 32)
        self.b10.clicked.connect(self.t010)

        self.b11 = QtWidgets.QPushButton(self)
        self.b11.setText("Background autoscan/011")
        self.b11.move(20, 350)
        self.b11.resize(300, 32)
        self.b11.clicked.connect(self.t011)

        self.b12 = QtWidgets.QPushButton(self)
        self.b12.setText("Background autoscan/012")
        self.b12.move(20, 380)
        self.b12.resize(300, 32)
        self.b12.clicked.connect(self.t012)

        self.b13 = QtWidgets.QPushButton(self)
        self.b13.setText("Seek Frequency/013")
        self.b13.move(20, 410)
        self.b13.resize(300, 32)
        self.b13.clicked.connect(self.t013)

        self.b14 = QtWidgets.QPushButton(self)
        self.b14.setText("Seek Frequency/014")
        self.b14.move(20, 440)
        self.b14.resize(300, 32)
        self.b14.clicked.connect(self.t014)

        self.b15 = QtWidgets.QPushButton(self)
        self.b15.setText("Seek Frequency/015")
        self.b15.move(20, 470)
        self.b15.resize(300, 32)
        self.b15.clicked.connect(self.t015)

        self.b16 = QtWidgets.QPushButton(self)
        self.b16.setText("Seek Service/016")
        self.b16.move(400, 50)
        self.b16.resize(300, 32)
        self.b16.clicked.connect(self.t016)

        self.b17 = QtWidgets.QPushButton(self)
        self.b17.setText("Seek Service/017")
        self.b17.move(400, 80)
        self.b17.resize(300, 32)
        self.b17.clicked.connect(self.t017)

        self.b18 = QtWidgets.QPushButton(self)
        self.b18.setText("Seek Service/018")
        self.b18.move(400, 110)
        self.b18.resize(300, 32)
        self.b18.clicked.connect(self.t018)

        self.b58 = QtWidgets.QPushButton(self)
        self.b58.setText("Seek Service/058")
        self.b58.move(400, 140)
        self.b58.resize(300, 32)
        self.b58.clicked.connect(self.t058)

        self.b59 = QtWidgets.QPushButton(self)
        self.b59.setText("Seek Service/059")
        self.b59.move(400, 170)
        self.b59.resize(300, 32)
        self.b59.clicked.connect(self.t059)

        self.b60 = QtWidgets.QPushButton(self)
        self.b60.setText("Seek Service/060")
        self.b60.move(400, 200)
        self.b60.resize(300, 32)
        self.b60.clicked.connect(self.t060)

        self.b60 = QtWidgets.QPushButton(self)
        self.b60.setText("Seek Service/060")
        self.b60.move(400, 200)
        self.b60.resize(300, 32)
        self.b60.clicked.connect(self.t060)

        self.b69 = QtWidgets.QPushButton(self)
        self.b69.setText("Manual frequency/069")
        self.b69.move(400, 230)
        self.b69.resize(300, 32)
        self.b69.clicked.connect(self.t069)

        self.b70 = QtWidgets.QPushButton(self)
        self.b70.setText("Manual frequency/070")
        self.b70.move(400, 260)
        self.b70.resize(300, 32)
        self.b70.clicked.connect(self.t070)

        self.b71 = QtWidgets.QPushButton(self)
        self.b71.setText("Manual frequency/071")
        self.b71.move(400, 290)
        self.b71.resize(300, 32)
        self.b71.clicked.connect(self.t071)

        self.b72 = QtWidgets.QPushButton(self)
        self.b72.setText("Manual frequency/072")
        self.b72.move(400, 320)
        self.b72.resize(300, 32)
        self.b72.clicked.connect(self.t072)
        ##############################################################
        ###################### PASS/FAIL LABEL########################
        ##############################################################
        btn101 = QPushButton('PASS/FAIL LIST', self)
        btn101.move(20, 510)
        btn101.resize(300, 32)
        btn101.setStyleSheet('background-color:rgb(1, 166, 255);')

        self.label99 = QtWidgets.QLabel(self)
        self.label99.setText("log:")

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

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Frequency Tune/001:")
        self.label1.move(20, 540)
        self.label1.resize(300,20)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Frequency Tune/002:")
        self.label2.move(20,570)
        self.label2.resize(300, 20)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Frequency Tune/003:")
        self.label3.move(20, 600)
        self.label3.resize(300, 20)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText("Select service/004:")
        self.label4.move(20, 630)
        self.label4.resize(300, 20)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText("Select service/005:")
        self.label5.move(20, 660)
        self.label5.resize(300, 20)

        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText("Select service/006:")
        self.label6.move(20, 690)
        self.label6.resize(300, 20)

        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText("Select service/007:")
        self.label7.move(20, 720)
        self.label7.resize(300, 20)

        self.label8 = QtWidgets.QLabel(self)
        self.label8.setText("Select service/008:")
        self.label8.move(20, 750)
        self.label8.resize(300, 20)

        self.label9 = QtWidgets.QLabel(self)
        self.label9.setText("AutoScan/009:")
        self.label9.move(20, 780)
        self.label9.resize(300, 20)

        self.label10 = QtWidgets.QLabel(self)
        self.label10.setText("AutoScan/010:")
        self.label10.move(20, 810)
        self.label10.resize(300, 20)

        self.label11 = QtWidgets.QLabel(self)
        self.label11.setText("Background autoScan/011:")
        self.label11.move(20, 840)
        self.label11.resize(300, 20)

        self.label12 = QtWidgets.QLabel(self)
        self.label12.setText("Background autoScan/012:")
        self.label12.move(20, 870)
        self.label12.resize(300, 20)

        self.label13 = QtWidgets.QLabel(self)
        self.label13.setText("Seek frequency/013:")
        self.label13.move(20, 900)
        self.label13.resize(300, 20)

        self.label14 = QtWidgets.QLabel(self)
        self.label14.setText("Seek frequency/014:")
        self.label14.move(20, 930)
        self.label14.resize(300, 20)

        self.label15 = QtWidgets.QLabel(self)
        self.label15.setText("Seek frequency/015:")
        self.label15.move(20, 960)
        self.label15.resize(300, 20)

        self.label16 = QtWidgets.QLabel(self)
        self.label16.setText("Seek Service/016:")
        self.label16.move(20, 990)
        self.label16.resize(300, 20)

        self.label17 = QtWidgets.QLabel(self)
        self.label17.setText("Seek Service/017:")
        self.label17.move(20, 1020)
        self.label17.resize(300, 20)

        self.label18 = QtWidgets.QLabel(self)
        self.label18.setText("Seek Service/018:")
        self.label18.move(20, 1050)
        self.label18.resize(300, 20)

        self.label58 = QtWidgets.QLabel(self)
        self.label58.setText("Seek Service/058:")
        self.label58.move(20, 1080)
        self.label58.resize(300, 20)

        self.label59 = QtWidgets.QLabel(self)
        self.label59.setText("Seek Service/059:")
        self.label59.move(20, 1110)
        self.label59.resize(300, 20)

        self.label60 = QtWidgets.QLabel(self)
        self.label60.setText("Seek_Service/060:")
        self.label60.move(20, 1140)
        self.label60.resize(300, 20)

        self.label69 = QtWidgets.QLabel(self)
        self.label69.setText("Manual frequency/069:")
        self.label69.move(400, 540)
        self.label69.resize(300, 20)

        self.label70 = QtWidgets.QLabel(self)
        self.label70.setText("Manual frequency/070:")
        self.label70.move(400, 570)
        self.label70.resize(300, 20)

        self.label71 = QtWidgets.QLabel(self)
        self.label71.setText("Manual frequency/071:")
        self.label71.move(400, 600)
        self.label71.resize(300, 20)

        self.label72 = QtWidgets.QLabel(self)
        self.label72.setText("Manual frequency/072:")
        self.label72.move(400, 630)
        self.label72.resize(300, 20)

    ######################################################################
    ################ DAB btn conncet event ###############################
    ######################################################################

    def t001(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
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
                        serach = "tune"
                        self.text.append(line)
                        if serach in line:
                            self.label1.setText("Frequency Tune/001:  PASS")
                            self.label1.setStyleSheet("Color : blue")
                            break
                        else:
                            self.label1.setText("Frequency Tune/001:  FAIL")
                            self.label1.setStyleSheet("Color : red")
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t002(self):
        self.text.setText("")
        all_file3 = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file2 = open("C:\\Users\\F190033\\log\\t1.txt", "w")
        fr1 = all_file3.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 174928 0 0')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr1:
                        line = all_file3.readline()
                        all_file2.write(line)
                        serach = "bash"
                        self.text.append(line)
                        if serach in line:
                            self.label2.setText("Frequency Tune/002:  PASS")
                            self.label2.setStyleSheet("Color : blue")
                            break
                        else:
                            self.label2.setText("Frequency Tune/002:  FAIL")
                            self.label2.setStyleSheet("Color : red")
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t003(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 225648 1')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "tune fail"
                        self.text.append(line)
                        if serach in line:
                            self.label3.setText("Frequency Tune/003:  PASS")
                            self.label3.setStyleSheet("Color : blue")
                            break
                        else:
                            self.label3.setText("Frequency Tune/003:  FAIL")
                            self.label3.setStyleSheet("Color : red")
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t004(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('s 0 0 174928 0xdab06 0xd122 0x0 0')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "tune"
                        self.text.append(line)
                        if serach in line:
                            self.label4.setText("Select service/004:  PASS")
                            self.label4.setStyleSheet("Color : blue")
                            break
                        else:
                            self.label4.setText("Select service/004:  FAIL")
                            self.label4.setStyleSheet("Color : red")
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t005(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('s 0 0 174928 0xdab06 0xd122 0x0 0')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "tune fail"
                        self.text.append(line)
                        if serach in line:
                            self.label5.setText("Select service/005:  PASS")
                            self.label5.setStyleSheet("Color : blue")
                            break
                        else:
                            self.label5.setText("Select service/005:  FAIL")
                            self.label5.setStyleSheet("Color : red")
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t006(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('s 0 0 174928 0xdab06 0xd122 0x0 0')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "tune fail"
                        self.text.append(line)
                        if serach in line:
                            self.label5.setText("Select service/006:  PASS")
                            self.label5.setStyleSheet("Color : blue")
                            break
                        else:
                            self.label6.setText("Select service/006:  FAIL")
                            self.label6.setStyleSheet("Color : red")
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t007(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
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
                        serach = "bash"
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('s 0 0 225648 0xdab88 0xd199 0x0 0')
                            pyautogui.press('enter')
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            time.sleep(5)
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "0xd199"
                                    self.text.append(line)
                                    if serach in line:
                                        self.label7.setText("Select service/007:  PASS")
                                        self.label7.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label7.setText("Select service/007:  FAIL")
                                        self.label7.setStyleSheet("Color : red")
                            break
                break

        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t008(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
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
                        serach = "bash"
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('s 0 0 211648 0xdab88 0xd199 0x0 0')
                            pyautogui.press('enter')
                            time.sleep(5)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"
                                    self.text.append(line)
                                    if serach in line:
                                        self.label8.setText("Select service/008:  PASS")
                                        self.label8.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label8.setText("Select service/008:  FAIL")
                                        self.label8.setStyleSheet("Color : red")
                            break
                 break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t009(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('a 0 0 1')
            pyautogui.press('enter')
            time.sleep(15)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash" #유요한 주파수 DB , 첫번로 찾은 주파수 수신,
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('a 0 0 0')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  # None 인경우는 아무동작하지 않는다. 아무런 주파수를 찾지 못해야함.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label10.setText("AutoScan/009:  PASS")
                                        self.label10.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label9.setText("AutoScan/009:  FAIL")
                                        self.label9.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t010(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
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
                        serach = "bash" #유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('a 0 1 1')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail" # 174928 이 아닌 다른 주파수를 잡아야 한다..
                                    self.text.append(line)
                                    if serach in line:
                                        self.label10.setText("AutoScan/010:  PASS")
                                        self.label10.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label10.setText("AutoScan/010:  FAIL")
                                        self.label10.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t011(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 1 174928 1')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('a 1 1 1')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  # 174928 이 아닌 다른 주파수를 잡아야 한다..
                                    self.text.append(line)
                                    if serach in line:
                                        self.label11.setText("Background autoscan/011:  PASS")
                                        self.label11.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label11.setText("Background autoscan/011:  FAIL")
                                        self.label11.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t012(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 1 174928 1')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('a 1 1 1')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  # 174928 이 아닌 다른 주파수를 잡아야 한다..
                                    self.text.append(line)
                                    if serach in line:
                                        self.label12.setText("Background autoscan/012:  PASS")
                                        self.label12.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label12.setText("Background autoscan/012:  FAIL")
                                        self.label12.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t013(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 239200 1')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('k 0 0 0 0')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  # 174928 이 아닌 다른 주파수를 잡아야 한다..
                                    self.text.append(line)
                                    if serach in line:
                                        self.label13.setText("Seek frequency/013:  PASS")
                                        self.label13.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label13.setText("Seek frequency/013:  FAIL")
                                        self.label13.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t014(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
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
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('k 0 1 0 0')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  #  174928 주파수의 첫번째 서비스가 선택 되어야 한다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label14.setText("Seek frequency/014:  PASS")
                                        self.label14.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label14.setText("Seek frequency/014:  FAIL")
                                        self.label14.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t015(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 239200 1')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('k 0 1 0 1')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  # 174928 주파수의 마지막 서비스가 선택 되어야 한다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label15.setText("Seek frequency/015:  PASS")
                                        self.label15.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label15.setText("Seek frequency/015:  FAIL")
                                        self.label15.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t016(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('s 0 0 239200 0xdab6 0xd123 0x0 0')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('v 0 0 0')
                            pyautogui.press('enter')
                            time.sleep(10)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "0xd122"  # 239200 주파수의 Oxd122 서비스가 선택 되어야 한다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label16.setText("Seek Service/016:  PASS")
                                        self.label16.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label16.setText("Seek Service/016:  FAIL")
                                        self.label16.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t017(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('s 0 0 239200 0xdab6 0xd122 0x0 0')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('v 0 1 0')
                            pyautogui.press('enter')
                            time.sleep(10)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "0xd123"  # 239200 주파수의 Oxd122 서비스가 선택 되어야 한다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label17.setText("Seek Service/017:  PASS")
                                        self.label17.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label17.setText("Seek Service/017:  FAIL")
                                        self.label17.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t018(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 174928 0')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('v 0 1 0')
                            pyautogui.press('enter')
                            time.sleep(10)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  # 서비스가 선택 되어야 하지 않는다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label18.setText("Seek Service/018:  PASS")
                                        self.label18.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label18.setText("Seek Service/018:  FAIL")
                                        self.label18.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t058(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('s 0 0 174928 0xdab6,0xd121 0x0 0')
            pyautogui.press('enter')
            time.sleep(10)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('v 0 1 5')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  # 174928,239200 주파수의 해당 서비스가 선택 되어 하지 않는다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label58.setText("Seek Service/058:  PASS")
                                        self.label58.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label58.setText("Seek Service/058:  FAIL")
                                        self.label58.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t059(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('s 0 0 174928 0xdab6,0xd121 0x0 0')
            pyautogui.press('enter')
            time.sleep(10)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('v 0 0 10')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  # 174928,239200 주파수의 해당 서비스가 선택 되어 하지 않는다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label59.setText("Seek Service/059:  PASS")
                                        self.label59.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label59.setText("Seek Service/059:  FAIL")
                                        self.label59.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t060(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('s 0 0 174928 0xdab6,0xd121 0x0 0')
            pyautogui.press('enter')
            time.sleep(5)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 유요한 주파수 DB
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('v 0 0 10')
                            pyautogui.press('enter')
                            time.sleep(15)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune fail"  # 174928,239200 주파수의 해당 서비스가 선택 되어 하지 않는다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label60.setText("Seek Service/060:  PASS")
                                        self.label60.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label60.setText("Seek Service/060:  FAIL")
                                        self.label60.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t069(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 174928 1')
            pyautogui.press('enter')
            time.sleep(50)
            pyautogui.typewrite('x 0 0')
            pyautogui.press('enter')
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  #  취소
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('y 0 0 0')
                            pyautogui.press('enter')
                            time.sleep(10)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune dune"  # 239200 주파수의 첫번째 서비스가 선택 되어 한다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label69.setText("Manual frequency/069:  PASS")
                                        self.label69.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label69.setText("Manual frequency/069:  FAIL")
                                        self.label69.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t070(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 174928 1')
            pyautogui.press('enter')
            time.sleep(50)
            pyautogui.typewrite('x 0 0')
            pyautogui.press('enter')
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  #  취소
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('y 0 0 0')
                            pyautogui.press('enter')
                            time.sleep(5)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune dune"  # 239200 주파수의 첫번째 서비스가 선택 되어 한다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label70.setText("Manual frequency/070:  PASS")
                                        self.label70.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label70.setText("Manual frequency/070:  FAIL")
                                        self.label70.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t071(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 239200 1')
            pyautogui.press('enter')
            time.sleep(50)
            pyautogui.typewrite('x 0 0')
            pyautogui.press('enter')
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 취소
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('y 0 1 1')
                            pyautogui.press('enter')
                            time.sleep(5)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune dune"  # 174928 주파수의 첫번째 서비스가 선택 되어 한다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label71.setText("Manual frequency/071:  PASS")
                                        self.label71.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label71.setText("Manual frequency/071:  FAIL")
                                        self.label71.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def t072(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 239200 1')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite('x 0 0')
            pyautogui.press('enter')
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "bash"  # 취소
                        self.text.append(line)
                        if serach in line:
                            pyautogui.typewrite('y 0 1 1')
                            pyautogui.press('enter')
                            time.sleep(5)
                            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                            for i, line in enumerate(part_file):
                                if i >= fr:
                                    line = all_file.readline()
                                    all_file1.write(line)
                                    serach = "tune dune"  # 174928 주파수의 첫번째 서비스가 선택 되어 한다.
                                    self.text.append(line)
                                    if serach in line:
                                        self.label72.setText("Manual frequency/072:  PASS")
                                        self.label72.setStyleSheet("Color : blue")
                                        break
                                    elif serach not in line:
                                        self.label72.setText("Manual frequency/072:  FAIL")
                                        self.label72.setStyleSheet("Color : red")
                            break
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def seek_service_tune_fail(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 174928 1')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite('v 0 0 8')
            pyautogui.press('enter')
            time.sleep(20)
            part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
            while 1:
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "tune fail"
                        self.text.append(line)
                        if serach in line:
                            self.label11.setText("seek_service_tune_fail:  PASS")
                            self.label11.setStyleSheet("Color : blue")
                            break
                        else:
                            self.label11.setText("seek_service_tune_fail:  FAIL")
                            self.label11.setStyleSheet("Color : red")
                break
        else:
            QMessageBox.critical(self, 'caution', "Plese Tera Term on main screen")

    def manual_frequency_tune(self):
        self.text.setText("")
        all_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
        all_file1 = open("C:\\Users\\F190033\\log\\t.txt", "w")
        fr = all_file.read().count("\n")
        pyautogui.moveTo(1763, 434)
        pyautogui.click()
        ImageGrab.grab()
        screen = ImageGrab.grab()
        pos = pyautogui.position()
        screen.getpixel(pos)
        im = screen.getpixel(pos)
        tera_color = (15, 25, 42)
        pyautogui.click()
        if im == tera_color:
            pyautogui.typewrite('f 0 174928 1')
            pyautogui.press('enter')
            time.sleep(30)
            pyautogui.moveTo(1763, 434)
            pyautogui.click()
            pyautogui.typewrite('y 0 0 0')
            pyautogui.press('enter')
            while 1:
                part_file = open("C:\\Users\\F190033\\log\\r.txt", "r")
                for i, line in enumerate(part_file):
                    if i >= fr:
                        line = all_file.readline()
                        all_file1.write(line)
                        serach = "tune fail"
                        self.text.append(line)
                        if serach in line:
                            self.label12.setText("manual_frequency_tune:  PASS")
                            self.label12.setStyleSheet("Color : blue")
                            break
                        else:
                            self.label12.setText("manual_frequency_tune:  FAIL")
                            self.label12.setStyleSheet("Color : red")
                break
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()

