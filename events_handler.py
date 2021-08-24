# -*- coding:utf-8 -*-
# @Project Name:main.py
# @FileName          :events_handler.py
# @Create Date       :2021/8/23 10:27
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
"""
===============================================================================================
@Version: 1.0.0
@Functions:
    1. All functions of handling events from UI.
    2. Notes:
          It is main window of the application with menubar
          after logging in the system.
================================================================================================
"""
import tkinter as tk
import tkinter.messagebox as tkm
import platform as pf
from importlib import reload
from dbm import *
import dbm  # for using database variabls like dbm.db, dbm.cursor etc.
import dialog


def quit(window):
    window.destroy()


def osinfo():
    info = pf.platform()
    info += ' @ ' + pf.machine()
    tkm.showinfo(title='OS information --- SIMS', message=info)


def connectdb(window):
    cdb_dialog = tk.Toplevel(window)
    cdb_dialog.geometry('+320+200')
    cdb_dialog.grab_set()  # set the model dialog
    font = ('consolas', 16, 'bold')
    color = '#EE3030'
    tk.Label(cdb_dialog, text="Host:", font=font, fg=color).grid(row=0, column=0, sticky=tk.E)
    tk.Label(cdb_dialog, text="Port:", font=font, fg=color).grid(row=1, column=0, sticky=tk.E)
    tk.Label(cdb_dialog, text="User:", font=font, fg=color).grid(row=2, column=0, sticky=tk.E)
    tk.Label(cdb_dialog, text="Password:", font=font, fg=color).grid(row=3, column=0, sticky=tk.E)
    tk.Label(cdb_dialog, text="Database:", font=font, fg=color).grid(row=4, column=0, sticky=tk.E)

    host = tk.Entry(cdb_dialog, textvariable=tk.StringVar(value='localhost'), font=font)
    host.grid(row=0, column=1, sticky=tk.W, padx=10)
    port = tk.Entry(cdb_dialog, textvariable=tk.StringVar(value='3306'), font=font)
    port.grid(row=1, column=1, sticky=tk.W, padx=10)
    user = tk.Entry(cdb_dialog, textvariable=tk.StringVar(value='root'), font=font)
    user.grid(row=2, column=1, sticky=tk.W, padx=10)
    password = tk.Entry(cdb_dialog, textvariable=tk.StringVar(value='123456'), font=font, show='*')
    password.grid(row=3, column=1, sticky=tk.W, padx=10)
    database = tk.Entry(cdb_dialog, textvariable=tk.StringVar(value='simsdb'), font=font)
    database.grid(row=4, column=1, sticky=tk.W, padx=10)
    if port.get() == '':
        port = 3306
    else:
        port = int(port.get())
    config = {
        'host': host.get(),
        'port': port,
        'user': user.get(),
        'password': password.get(),
        'database': database.get()
    }

    bnConnect = tk.Button(cdb_dialog, text="连接", width=15, command=lambda: connect(config, cdb_dialog), font=font,
                          fg=color)
    bnConnect.grid(row=5, column=0, sticky=tk.W, padx=5, pady=8)
    bnQuit = tk.Button(cdb_dialog, text="退出", width=15, command=lambda: quit(cdb_dialog), font=font, fg=color)
    bnQuit.grid(row=5, column=1, sticky=tk.E, padx=5, pady=8)


def dbinfo():
    if dbm.db is not None:
        dbm.cursor.execute('select concat(@@version_comment , \' \' , @@version) from dual')
        info = str(dbm.cursor.fetchall()[0][0])
        sql = '''select @@hostname,@@datadir, 
                       @@innodb_data_file_path,@@innodb_data_home_dir, 
                       @@innodb_log_file_size/1024/1024 from dual
              '''
        dbm.cursor.execute(sql)
        info += '\n\r' + str(dbm.cursor.fetchall()[0])
    else:
        info = 'Database server did not be connected yet.'
    tkm.showinfo(title='Database information --- SIMS', message=info)


def others():
    info = 'You can extend other functions from here.'
    tkm.showinfo(title='Other information --- SIMS', message=info)


def userinfo():
    if dialog.username is None:
        tkm.showinfo(title='User information --- SIMS', message='请先登录')
    else:
        info = 'Username: ' + dialog.username + '\r\n' + \
               'Usertype: ' + dialog.usertype
        tkm.showinfo(title='User information --- SIMS', message=info)


def changepsw(window):
    pass_dialog = tk.Toplevel(window)
    pass_dialog.geometry('+320+200')
    pass_dialog.grab_set()  # set the model dialog
    font = ('consolas', 16, 'bold')
    color = '#EE3030'
    tk.Label(pass_dialog, text="Old password:", font=font, fg=color).grid(row=0, column=0, sticky=tk.E)
    tk.Label(pass_dialog, text="New password:", font=font, fg=color).grid(row=1, column=0, sticky=tk.E)
    tk.Label(pass_dialog, text="Confirm NEW:", font=font, fg=color).grid(row=2, column=0, sticky=tk.E)
    old = tk.Entry(pass_dialog, font=font)
    old.grid(row=0, column=1, sticky=tk.W, padx=10)
    new = tk.Entry(pass_dialog, font=font)
    new.grid(row=1, column=1, sticky=tk.W, padx=10)
    confirm = tk.Entry(pass_dialog, font=font)
    confirm.grid(row=2, column=1, sticky=tk.W, padx=10)

    pinfo = {
        'user': dialog.username,
        'old': old.get(),
        'new': new.get()
    }

    def changepassword(pinfo, pass_dialog):
        if new.get() != confirm.get():
            tkm.showinfo(title='Password change information --- SIMS', message='两次输入的口令不一致')
            return
        if dbm.db is None:
            tkm.showinfo(title='Password change information --- SIMS', message='请先连接数据库')
        else:
            # dbm.cursor.execute('SET SQL_SAFE_UPDATES=0')  # needed when first execute
            sql = 'update user set password=\'%s\' where name=\'%s\' and password=\'%s\'' % (
            new.get(), pinfo['user'], old.get())
            print(sql)
            res = dbm.cursor.execute(sql)  # 0 if fail, 1 if success
            if res:
                dbm.db.commit()
                tkm.showinfo(title='Password change information --- SIMS', message='密码已经修改好')
                pass_dialog.destroy()
            else:
                tkm.showinfo(title='Password change information --- SIMS', message='密码修改失败了')

    bnChange = tk.Button(pass_dialog, text="修改", width=15, command=lambda: changepassword(pinfo, pass_dialog),
                         font=font, fg=color)
    bnChange.grid(row=5, column=0, sticky=tk.W, padx=5, pady=8)
    bnQuit = tk.Button(pass_dialog, text="退出", width=15, command=lambda: quit(pass_dialog), font=font, fg=color)
    bnQuit.grid(row=5, column=1, sticky=tk.E, padx=5, pady=8)


def logout():
    dbm.cursor.close()
    dbm.db.close()
    dialog.username = None
    dialog.usertype = None
    tkm.showinfo(title='Log out information --- SIMS', message='退出登录后请重新连接数据库服务器')


def relog():
    reload(dialog)  # can not repeat more than 2 times


def basicinfo(window):
    if dbm.db is not None:
        sql = 'select * from student'
        print(sql)
        dbm.cursor.execute(sql)
        results = dbm.cursor.fetchall()
        showResults_Treeview(window, results)
    else:
        info = 'Database server did not be connected yet.'
        tkm.showinfo(title='Searching information --- SIMS', message=info)


def scoreinfo():
    pass


def newrecord(window):
    enter = tk.Toplevel(window)
    enter.title('录入学生信息')
    enter.geometry('+320+200')
    enter.grab_set()
    font = ('consolas', 16, 'bold')
    color = '#EE3030'
    tk.Label(enter, text=' 学  号 ', font=font, fg=color).grid(row=0, column=0, sticky=tk.E)
    tk.Label(enter, text=' 姓  名 ', font=font, fg=color).grid(row=1, column=0, sticky=tk.E)
    tk.Label(enter, text=' 电  话 ', font=font, fg=color).grid(row=2, column=0, sticky=tk.E)
    tk.Label(enter, text=' 电  邮 ', font=font, fg=color).grid(row=3, column=0, sticky=tk.E)
    tk.Label(enter, text=' 宿  舍 ', font=font, fg=color).grid(row=4, column=0, sticky=tk.E)
    sid = tk.Entry(enter, font=font, textvariable=tk.StringVar(value='一定不能为空'), bg='#FFA0A0')
    sid.grid(row=0, column=1, columnspan=2, sticky=tk.EW, padx=30, pady=7)
    name = tk.Entry(enter, font=font)
    name.grid(row=1, column=1, columnspan=2, sticky=tk.EW, padx=30, pady=7)
    phone = tk.Entry(enter, font=font)
    phone.grid(row=2, column=1, columnspan=2, sticky=tk.EW, padx=30, pady=7)
    email = tk.Entry(enter, font=font)
    email.grid(row=3, column=1, columnspan=2, sticky=tk.EW, padx=30, pady=7)
    dorm = tk.Entry(enter, font=font)
    dorm.grid(row=4, column=1, columnspan=2, sticky=tk.EW, padx=30, pady=7)

    def append():
        record = {
            'sid': sid.get(),
            'name': name.get(),
            'phone': phone.get(),
            'email': email.get(),
            'dorm': dorm.get()
        }
        if dbm.db is not None:
            sql = 'insert into student (studentID, name, phone, email, dorm) VALUES (%d, \'%s\', \'%s\', \'%s\', \'%s\')' \
                  % (int(record['sid']), record['name'], record['phone'], record['email'], record['dorm'])
            print(sql)
            res = dbm.cursor.execute(sql)
            dbm.db.commit()
            if res:
                tkm.showinfo(title='Entering records information --- SIMS', message='增加一条新记录成功')
                enter.destroy()
            else:
                tkm.showinfo(title='Entering records information --- SIMS', message='增加记录不成功')
        else:
            info = 'Database server did not be connected yet.'
            tkm.showinfo(title='Entering records information --- SIMS', message=info)

    def cls():
        sid.delete(0, 'end')
        name.delete(0, 'end')
        phone.delete(0, 'end')
        email.delete(0, 'end')
        dorm.delete(0, 'end')

    def quit():
        enter.destroy()

    bnAdd = tk.Button(enter, text="增加", width=10, command=append, font=font, fg=color)
    bnAdd.grid(row=5, column=0, padx=25, pady=18)
    bnCls = tk.Button(enter, text="清空", width=10, command=cls, font=font, fg=color)
    bnCls.grid(row=5, column=1, padx=25, pady=18)
    bnQuit = tk.Button(enter, text="退出", width=10, command=quit, font=font, fg=color)
    bnQuit.grid(row=5, column=2, padx=25, pady=18)


def scoresentry():
    pass


def revise():
    pass


def delete(window):
    enter = tk.Toplevel(window)
    enter.title('录入学生信息')
    enter.geometry('+320+200')
    enter.grab_set()
    font = ('consolas', 16, 'bold')
    color = '#EE3030'
    tk.Label(enter, text=' 学  号 ', font=font, fg=color).grid(row=0, column=0, sticky=tk.E)
    sid = tk.Entry(enter, font=font, textvariable=tk.StringVar(value='一定不能为空'), bg='#FFA0A0')
    sid.grid(row=0, column=1, columnspan=2, sticky=tk.EW, padx=30, pady=7)

    def append():
        if dbm.db is not None:
            sql = 'delete from student where studentID = %d' % int(sid.get())
            print(sql)
            res = dbm.cursor.execute(sql)
            dbm.db.commit()
            if res:
                tkm.showinfo(title='Deleting records information --- SIMS', message='删除一条新记录成功')
                enter.destroy()
            else:
                tkm.showinfo(title='Deleting records information --- SIMS', message='删除记录不成功')
        else:
            info = 'Database server did not be connected yet.'
            tkm.showinfo(title='Deleting records information --- SIMS', message=info)

    def cls():
        sid.delete(0, 'end')

    def quit():
        enter.destroy()

    bnAdd = tk.Button(enter, text="增加", width=10, command=append, font=font, fg=color)
    bnAdd.grid(row=1, column=0, padx=25, pady=18)
    bnCls = tk.Button(enter, text="清空", width=10, command=cls, font=font, fg=color)
    bnCls.grid(row=1, column=1, padx=25, pady=18)
    bnQuit = tk.Button(enter, text="退出", width=10, command=quit, font=font, fg=color)
    bnQuit.grid(row=1, column=2, padx=25, pady=18)


def histroy():
    pass


def recover():
    pass


if __name__ == '__main__':
    window = tk.Tk()
    # osinfo()
    # dbinfo()
    newrecord(window)
    pass
