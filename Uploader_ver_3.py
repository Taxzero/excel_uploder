from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mbox
import pandas as pd
from datetime import datetime
import tkinter as tk
import tkinter.ttk as ttk
import subprocess
from subprocess import PIPE
from threading import Thread
import sys
import cx_Oracle as cx
from tkinter.ttk import *





def file_find():
    
    # 파일 경로 찾기 창
    file = filedialog.asksaveasfilename(filetypes=(
        ("Excel file", "*.xlsx"), ("all file", "*.xlsx*")), initialdir="C:/Users")
    print(file)
    progressbar.start()    
    test = pd.read_excel(file)
    test['column'] = test['column'].fillna(0).astype('int')
    test['column2'] = test['column2'].fillna(0).astype('int')

    # CSV로 확장자 변경한 파일 저장경로
    test2 = r"D:\file.csv"
    test.to_csv(test2, sep="|", encoding='utf-8-sig', index=False)

    # 실행 파일
    subprocess.call(
        'sqlldr userid=oracle_DB_name/oracle_DB_name@SID_name control=.\file\file.ctl', shell=True,  text=True)
    
    # EMP_NO 인자 받아오기
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])

#    en_filepath.delete('1.0', END)
#    en_filepath.insert(END, file)
    progressbar.stop()
    app.quit()
    exit()



# 멀티스레드
def startTread():
    th1 = Thread(target=file_find)
    th1.setDaemon(True)
    th1.start() 

    
# 화면 구성
app = tk.Tk()
#en_filepath = tk.Entry(app, width=70, state=DISABLED)
#en_filepath.pack(fill="x", padx=3, pady=3, ipady=5)

#프로그레스바
progressbar = ttk.Progressbar(mode="indeterminate")
progressbar.place(x=30, y=30, width=235)

#창크기 X*Y 창위치 X*Y
app.geometry("300x50+800+500")

fr_bt = Frame(app)
fr_bt.pack(fill="x", padx=1, pady=1)

#Button
bt_find = Button(fr_bt, text="Find and upload", width=30, command=startTread)
bt_find.pack(padx=1, pady=1)


app.title('File Uploader')
app.mainloop()
