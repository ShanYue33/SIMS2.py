# -*- coding:utf-8 -*-
# @Project Name:main.py
# @FileName          :main_1.py
# @Create Date       :2021/8/23 10:44
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
"""
=================================================================================
@Version: 1.0.0
@Functions:
    1. Main window
    2. Notes:
          It is main window of the application with menubar
          after logging into the system.
    3.Explanation:
        First of all, there is a connection database menu bar in the menu bar.
        We connect this menu bar with an interface for
        opening the connection database parameter configuration, that is,
        the menu event processing (callback) is realized by a function,
        and this function is connected with the menu ( Register to listen),
        use the following code to achieve.
=================================================================================
"""
from events_handler import *

window = tk.Tk()
window.title('SIMS ———— 学生信息管理系统（信管专业小学期实践工程项目——姗）')
window.state('zoomed')
window.resizable(False, False)  # 不可改变窗口大小
# window.overrideredirect(True)  # 不可拖动窗口

menubar = tk.Menu(window)  # 建立一个菜单条对象

# 二级菜单，创建若干个菜单对象
adminMenu = tk.Menu(menubar)
for item in [('操作系统信息', osinfo),
             ('连接数据服务器', lambda: connectdb(window)),
             ('数据库信息', dbinfo),
             ('退出系统', lambda: quit(window)),
             ('其它', others)]:
    # 为每个菜单增加菜单项，菜单项可以响应鼠标点击，需要关联处理函数
    adminMenu.add_command(label=item[0], command=item[1])
userMenu = tk.Menu(menubar)
for item in [('用户信息', userinfo),
             ('口令修改', lambda: changepsw(window)),
             ('退出登录', logout),
             ('重新登录', relog)]:
    userMenu.add_command(label=item[0], command=item[1])
aboutMenu = tk.Menu(menubar)

for item in ['版权信息', '系统更新', '联系我们']:
    aboutMenu.add_command(label=item)

studentMenu = tk.Menu(menubar)
for item in [('基本信息查询', lambda: basicinfo(window)),
             ('学生成绩查询', scoreinfo),
             ('其它查询', others)]:
    studentMenu.add_command(label=item[0], command=item[1])
    # add_separator()：一个下拉菜单的分割线
studentMenu.add_separator()
for item in [('录入学生信息', lambda: newrecord(window)),
             ('录入学生成绩', scoresentry),
             ('修改', revise)]:
    studentMenu.add_command(label=item[0], command=item[1])
studentMenu.add_separator()
for item in [('删除学生信息', lambda: delete(window)),
             ('删除历史', histroy),
             ('恢复', recover),
             ('其它', others)]:
    studentMenu.add_command(label=item[0], command=item[1])
studentMenu.add_separator()

# 三级菜单
statMenu = tk.Menu(studentMenu)
for item in ['学生总成绩', '单科总分平均分', '年级成绩汇总统计',
             '不及格学生统计', '优秀学生统计']:
    statMenu.add_command(label=item)
    # 把菜单增加到菜单条
studentMenu.add_cascade(label='统计', menu=statMenu)

# 一级菜单
for each in [('系统管理', adminMenu),
             ('学生信息管理', studentMenu),
             ('用户管理', userMenu),
             ('关于', aboutMenu)]:
    menubar.add_cascade(label=each[0], menu=each[1])
    # 把菜单条加到window窗口
window['menu'] = menubar

sb = tk.Scrollbar(window)
sb.pack(side='right', fill='y')
list_box = tk.Listbox(window, setgrid=True,
                      font=('幼圆', 16), fg='#101036',
                      yscrollcommand=sb.set)
list_box.pack(fill='both', expand=True)
list_box.insert(0, ' 还没有连接数据库服务器......')
list_box.select_set(0, 0)  # 默认选中第一行
for item in range(100):
    list_box.insert('end', '   学生  ' + str(item))
sb.config(command=list_box.yview)

window.mainloop()
