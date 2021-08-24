# -*- coding:utf-8 -*-
# @Project Name:main.py
# @FileName          :dialog.py
# @Create Date       :2021/8/23 10:23
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
"""
============================================================================
@Version: 1.0.0
@Functions:
    1. Logging window
    2. Notes:
          不要试图在一个主窗口中混合使用pack和grid.
============================================================================
"""
import tkinter.messagebox as tkm
from tkinter import *

import pymysql as ps

import dbm

username = None
usertype = None
login = Tk()
login.title('LOG IN')
width = 455
height = 120
screenwidth = login.winfo_screenwidth()
screenheight = login.winfo_screenheight()
login.geometry('%dx%d+%d+%d' % (width, height, \
                                (screenwidth - width) / 2, (screenheight - height) / 2))
login.resizable(False, False)

font = ('consolas', 16, 'bold')
color = '#EE3030'
Label(login, text="Username:", font=font, fg=color).grid(row=0, column=0, sticky=E)
Label(login, text="Password:", font=font, fg=color).grid(row=1, column=0, sticky=E)
# StringVar()跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
username = StringVar()
password = StringVar()
username.set('guest')
# Entry：Tkinter用来接受字符串等输入的控件，允许用户输入一行文字

user = Entry(login, textvariable=username, font=font)
pawd = Entry(login, textvariable=password, show='*', font=font)
user.grid(row=0, column=1, columnspan=2, sticky=W)
pawd.grid(row=1, column=1, columnspan=2, sticky=W)


def log():
    print("user name:", user.get())
    print(" password:", pawd.get())
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '2770205',
        'database': 'simsdb'
    }
    dbm.db = ps.connect(**config)
    dbm.cursor = dbm.db.cursor()
    sql = 'select name, type from user where name = \'%s\' and password = \'%s\'' % (user.get(), pawd.get())
    dbm.cursor.execute(sql)
    results = dbm.cursor.fetchall()
    if results == ():
        info = '用户名不存在或者密码输入错误'
        print(info)
        tkm.showinfo(title='User logging --- SIMS', message=info)
    else:
        print(results)
        global username, usertype
        username = results[0][0]
        usertype = results[0][1]
        info = '登录成功'
        print(info)
        tkm.showinfo(title='User logging --- SIMS', message=info)
        login.destroy()  # enter main UI


def delete():
    user.delete(0, END)
    pawd.delete(0, END)


def quit():
    login.destroy()
    sys.exit()


login_ = Button(login, text="Login", width=10, command=log, font=font, fg=color)
reset = Button(login, text="Reset", width=10, command=delete, font=font, fg=color)
quit_ = Button(login, text=" Quit", width=10, command=quit, font=font, fg=color)

login_.grid(row=3, column=0, sticky=W, padx=10, pady=5)
reset.grid(row=3, column=1, padx=10, pady=5)
quit_.grid(row=3, column=2, sticky=E, padx=10, pady=5)

mainloop()

if __name__ == '__main__':
    print(username)
    print(usertype)
