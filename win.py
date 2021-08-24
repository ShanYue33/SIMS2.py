# -*- coding:utf-8 -*-
# @Project Name:main.py
# @FileName          :win.py
# @Create Date       :2021/8/23 10:29
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
"""
===========================================================================================
@Version: 1.0.0
@Functions:
    1. All functions of handling events from UI.
    2. Notes:
          It is main window of the application with menubar
          after logging in the system.
==========================================================================================
"""
import tkinter as tk
import tkinter.messagebox as tmbox

window = tk.Tk()  # 创建主窗口对象
window.title('SIMS——岳姗')  # 设置主窗口标题
window.geometry('800x600')  # 设置主窗口大小
# window.state('zoomed')
# window.attributes("-fullscreen", True)  # maxize window without title
# 建立标签对象，第一参数是window，表示它的宿主是window对象
banner = tk.Label(window, text='学生信息管理系统\n\rVersion 2.0',
                  font=('幼圆', 42, 'bold'), fg='#E02022',
                  height=4).pack()


# 调用pack()函数，把它和window主窗口配到一起

def say_hi():
    tmbox.showinfo(title='Hi', message='Hello Python World.')


def say_bye():
    tmbox.showwarning(title='bye', message='See you again!')


# 把函数名作为按钮对象command参数值传过去，使用command=lambda: 的形式传参
hi = tk.Button(window, text='Say Hello',
               font=('consolas', 18, 'bold'), fg='#5020EE',
               command=say_hi)
# hi.pack(side='left')
# Tkinter中提供的三个常规几何管理器中最简单的是Place几何管理器。
# 它允许您以绝对值或相对于另一个窗口的方式显式设置窗口的位置和大小。
# 您可以通过place()方法访问位置管理器，该方法可用于所有标准小部件。
hi.place(x=180, y=400)
bye = tk.Button(window, text=' Bye Bye ',
                font=('consoles', 18, 'bold'), fg='#3050EE',
                command=say_bye)
# bye.pack(side='right')
bye.place(x=520, y=400)

footnote = tk.Label(window, text='昆明理工大学管经学院信息管理与信息系统专业2019级暑期实践课程\n\rCopyright @ 2021.08-2021.10\n\r',
                    font=('幼圆', 16)).pack(side='bottom')

window.mainloop()  # window.mainloop()不断重复GUI代码，以便窗口及其小部件保持在屏幕上。
# 启动窗口的是件主循环，监听鼠标点击等事件
