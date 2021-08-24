# -*- coding:utf-8 -*-
# @Project Name:main.py
# @FileName          :mysql_1.py
# @Create Date       :2021/8/23 10:28
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
import mysql.connector as mc

db = mc.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="simsdb"  # 指定数据库
)

cursor = db.cursor()  # 操作句柄（游标）

sql = 'show tables'
cursor.execute(sql)
for item in cursor:
    print(item)

sql = 'select * from student limit 0,3'
cursor.execute(sql)
for item in cursor:
    print(item)

db.commit()  # 如果数据库有变化，必须commit之后才能持久化
cursor.close()
db.close()

