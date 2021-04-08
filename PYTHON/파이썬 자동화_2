Pimport pyautogui
import time
import keyboard
import pyperclip
import os
import shutil
from openpyxl import load_workbook
import datetime
import glob
import math

# 자동화 시작 이전 파일 경로 삭제
if os.path.isdir('C:/Users/user/Desktop/아파트 만들기'):
    shutil.rmtree('C:/Users/user/Desktop/아파트 만들기')
APP_DATA = ["FeatureBuilderFloorGenerateWindow","FeatureRebarMaterialWindow","FeatureBuilderStoryMaterialWindow"]
def APP():
    # 바탕화면에서 실행파일을 찾아서 자동 실행 하기
    file_name = "Chang.NX.NXBuilderStart.exe"
    file_path = "C:/Users/"
    files = glob.glob(file_path + "/**/"+ file_name, recursive= True)
    file_start = files[0]
    os.popen(file_start)
    time.sleep(10)
    gongs = pyautogui.locateAllOnScreen('C:/image/all.jpg', confidence=0.9)
    gongs = list(gongs)
    gongs_len = (len(gongs))
    if gongs_len == 1 :
        pyautogui.moveTo(pyautogui.center(gongs[0]))
        pyautogui.doubleClick()
    else :
        time.sleep(1)
        gongs = pyautogui.locateAllOnScreen('C:/image/all.jpg', confidence=0.99)
        gongs = list(gongs)
        gongs_len = (len(gongs))
        if gongs_len == 1 :
            pyautogui.moveTo(pyautogui.center(gongs[0]))
            pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.click(25,21) # APP 메뉴 클릭
    time.sleep(0.5)
    pyautogui.click(31, 71) # 새로 만들기 클릭
    time.sleep(2)
    gongs = pyautogui.locateAllOnScreen('C:/image/main.jpg', confidence=0.95)
    gongs = list(gongs)
    gongs_len = (len(gongs))
    if gongs_len == 1 :
        pyautogui.moveTo(pyautogui.center(gongs[0]))
        pyautogui.click()
    else :
        gongs = pyautogui.locateAllOnScreen('C:/image/main.jpg', confidence=0.98)
        gongs = list(gongs)
        gongs_len = (len(gongs))
        if gongs_len == 1 :
            pyautogui.moveTo(pyautogui.center(gongs[0]))
            pyautogui.click()
    time.sleep(2)
    gongs = pyautogui.locateAllOnScreen('C:/image/file_name.jpg', confidence=0.9)
    gongs = list(gongs)
    gongs_len = (len(gongs))
    if gongs_len == 1 :
        pyautogui.moveTo(pyautogui.center(gongs[0]))
        pyautogui.click()
    else :
        gongs = pyautogui.locateAllOnScreen('C:/image/file_name.jpg', confidence=0.88)
        gongs = list(gongs)
        gongs_len = (len(gongs))
        if gongs_len == 1 :
            pyautogui.moveTo(pyautogui.center(gongs[0]))
            pyautogui.click()
    time.sleep(1)
    pyautogui.move(100,0)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
    pyperclip.copy('아파트 만들기')
    pyautogui.hotkey("ctrl","v")
    time.sleep(3)
    gongs = pyautogui.locateAllOnScreen('C:/image/save.jpg', confidence=0.95)
    gongs = list(gongs)
    gongs_len = (len(gongs))
    if gongs_len == 1 :
        pyautogui.moveTo(pyautogui.center(gongs[0]))
        pyautogui.click()
    file_name = "아파트 만들기.rhb"
    file_path = "C:/Users/"
    files = glob.glob(file_path + "/**/"+ file_name, recursive= True)
    file_start = 0
    for i in files:
        file_start = i
    # 파일 경로에 만들어 졌으면 테스트 성공/실패 
    if os.path.exists(file_start) == True :
        print("ID:2-1-1     테스트요약:새로만들기       결과:PASS")
    else:
        print("ID:2-1-1     테스트요약:새로만들기       결과:FAIL")
        APP()

def FLOOR():
    # 이미지 처리를 위해 PYAUTOGUI 사용,미리 저장해둔 경로에 이미지를 전체 스크린샷 하여 같은 이미지 매칭. 
    gongs = pyautogui.locateAllOnScreen('C:/image/floor.jpg', confidence=0.95)
    gongs = list(gongs)
    gongs_len = (len(gongs))
    if gongs_len == 1 :
        pyautogui.moveTo(pyautogui.center(gongs[0]))
        pyautogui.click()
    else :
        gongs = pyautogui.locateAllOnScreen('C:/image/floor.jpg', confidence=0.95-0.01)
        gongs = list(gongs)
        gongs_len = (len(gongs))
        if gongs_len == 1 :
            pyautogui.moveTo(pyautogui.center(gongs[0]))
            pyautogui.click()
    time.sleep(1)
    pyautogui.doubleClick(866,283)
    pyautogui.hotkey('delete')
    pyautogui.typewrite(['2','6'])
    time.sleep(1)
    pyautogui.doubleClick(865,307)
    pyautogui.hotkey('delete')
    pyautogui.typewrite(['1'])
    time.sleep(1)
    pyautogui.doubleClick(1154,307)
    pyautogui.hotkey('delete')
    time.sleep(1)
    pyautogui.typewrite(['2','8','5','0'])
    time.sleep(1)
    pyautogui.click(1162,337)
    time.sleep(1)
    pyautogui.doubleClick(850,426)
    pyautogui.hotkey("delete")
    pyperclip.copy('옥탑지붕층')
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)
    pyautogui.doubleClick(853,456)
    pyautogui.hotkey("delete")
    pyperclip.copy('옥탑층')
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)
    pyautogui.doubleClick(839,480)
    pyautogui.hotkey("delete")
    pyperclip.copy('지붕층')
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)
    pyautogui.doubleClick(934,455)
    pyautogui.hotkey("delete")
    pyautogui.typewrite(['2','7','0','0'])
    time.sleep(0.5)
    pyautogui.doubleClick(939,481)
    pyautogui.hotkey("delete")
    pyautogui.typewrite(['2','7','0','0'])
    time.sleep(0.5)
    pyautogui.doubleClick(932,505)
    pyautogui.hotkey("delete")
    pyautogui.typewrite(['2','9','5','0'])    
    time.sleep(0.5)
    pyautogui.moveTo(1207,748)
    for i in range(10):
        pyautogui.click(1207,748)
    time.sleep(0.5)
    pyautogui.doubleClick(930,736)
    pyautogui.hotkey("delete")
    pyautogui.typewrite(['4','9','5','0'])
    time.sleep(0.5)
    pyautogui.doubleClick(935,762)
    pyautogui.hotkey("delete")
    pyautogui.typewrite(['4','9','5','0'])
    time.sleep(0.5)
    pyautogui.click(930,736)
    pyautogui.click(1138,800)    
    pyautogui.hotkey("esc")

# 로그 파일을 읽기위해 파일 경로 찾기
file_name = "아파트 만들기.rhb.Data/"
file_path = "C:/Users/"
files = glob.glob(file_path + "/**/"+ file_name, recursive= True)
file_start = files[0]
find_lastlog = os.listdir(file_start)
log_file = []
for i in find_lastlog :
    if i == "LogData" :
        log_file.append(i)
        break
last_log = (file_start +  log_file[0])
find_lastlog = os.listdir(last_log)
list_log = []
for i in find_lastlog:
    list_log.append(i)
    list_log.sort()
path = len(list_log)
log_data_file = list_log[path -1]
f = open( last_log+"\\" + log_data_file , 'r',encoding='UTF8')
a = f.read()
for i in APP_DATA:
    if i in a :
        print("ID:2-1-2     테스트요약:층               결과:PASS")
        print("ID:2-1-3     테스트요약:재질               결과:PASS")
        print("ID:2-1-4     테스트요약:층재질               결과:PASS")
        break
    else:
        print("테스트 실패")
f.close()

#현재 시간으로 부터 로그를 읽어오면서 while 문으 원하는 문자열 찾음 
start1 = datetime.datetime.now()
start_sec = start1.strftime('%H:%M:%S')
file_name = "아파트 만들기.rhb.Data/"
file_path = "C:/Users/"
files = glob.glob(file_path + "/**/"+ file_name, recursive= True)
file_start = files[0]
find_lastlog = os.listdir(file_start)
log_file = []
for i in find_lastlog :
    if i == "LogData" :
        log_file.append(i)
        break
last_log = (file_start +  log_file[0])
find_lastlog = os.listdir(last_log)
list_log = []
for i in find_lastlog:
    list_log.append(i)
    list_log.sort()
path = len(list_log)
log_data_file = list_log[path -1]
f = open( last_log+"\\" + log_data_file , 'r',encoding='UTF8')
line_num = 1
line_data = f.readline()
log_line = []
while 1:
    serch = "[[ 배근 물량 산출 Finish ]]"
    line_data = f.readline()
    if line_data[0:8] >= start_sec :
        line_data = f.readline() #로그 파일 행 읽기
        line_num += 1 #로그 파일 행
        if serch in line_data:
            break
#xlms 파일 경로 찾고 행,열 찾아 데이터 round로 저장 하여 소수점 제외한 정수 읽어와 데이터 비교후 테스트 성공/실패 판단
time.sleep(15)
file_name = "일반.xlsx"
file_path = "C:/Users/"
files = glob.glob(file_path + "/**/"+ file_name, recursive= True)
excel_name = files[0]
if os.path.isfile(excel_name):
    time.sleep(1)
    gongs = pyautogui.locateAllOnScreen('C:/image/SAVE_EXCEL.jpg', confidence=0.9)
    gongs = list(gongs)
    gongs_len = (len(gongs))
    if gongs_len == 1 :
        pyautogui.moveTo(pyautogui.center(gongs[0]))
        pyautogui.click()
    else :
        gongs = pyautogui.locateAllOnScreen('C:/image/SAVE_EXCEL.jpg', confidence=0.95)
        gongs = list(gongs)
        gongs_len = (len(gongs))
        if gongs_len == 1 :
            pyautogui.moveTo(pyautogui.center(gongs[0]))
            pyautogui.click()
    time.sleep(1)
    gongs = pyautogui.locateAllOnScreen('C:/image/CLOSE_EXCEL.jpg', confidence=0.9)
    gongs = list(gongs)
    gongs_len = (len(gongs))
    if gongs_len == 1 :
        pyautogui.moveTo(pyautogui.center(gongs[0]))
        pyautogui.click()
    else :
        gongs = pyautogui.locateAllOnScreen('C:/image/CLOSE_EXCEL.jpg', confidence=0.95)
        gongs = list(gongs)
        gongs_len = (len(gongs))
        if gongs_len == 1 :
            pyautogui.moveTo(pyautogui.center(gongs[0]))
            pyautogui.click()
    time.sleep(3)
    COMPARE_FLOOR = [3579,22757,224]
    COMPARE_LIST = []
    if os.path.isfile(excel_name):
        load_wb = load_workbook(excel_name,read_only=True, data_only=True)
        load_ws = load_wb['총괄분석표']
        concrete = math.trunc(load_ws['T7'].value)
        formwork = math.trunc(load_ws['V7'].value)
        rc = math.trunc(load_ws['X7'].value)
        COMPARE_LIST.append(concrete)
        COMPARE_LIST.append(formwork)
        COMPARE_LIST.append(rc)
        print("-----------------------------------------------------------------------")
        print("Version_1.4.8_기준 값")
        print("콘크리트:{} 거푸집:{} 철근:{}".format(COMPARE_FLOOR[0],COMPARE_FLOOR[1],COMPARE_FLOOR[2]))
        print("-----------------------------------------------------------------------")
        print("실제 테스트 결과:")
        print("콘크리트:{} 거푸집:{} 철근:{}".format(concrete,formwork,rc))
        if set(COMPARE_FLOOR) == set(COMPARE_LIST) :
            print("ID:2-5-1     테스트요약:아파트적산       결과:PASS")
        else :
            print("ID:2-5-1     테스트요약:아파트적산       결과:FAIL")


