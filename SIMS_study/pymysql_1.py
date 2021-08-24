# -*- coding:utf-8 -*-
# @Project Name:main.py
# @FileName          :pymysql_1.py
# @Create Date       :2021/8/23 15:14
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
import pymysql as ps

# 定义一个配置字典config,指定数据库服务器的连接地址和端口，同时指定数据库名
config = {
    "host": "localhost",
    "port": 3306,  # 端口
    "user": "root",  # 用户名
    "password": "123456",
    "database": "simsdb",  # 数据库名
}
db = ps.connect(**config)
cursor = db.cursor()
sql = '''select*from student where name='张三丰'''
cursor.execute(sql)
results = cursor.fetchall()  # fetchall()取第一个结果记录
for i in results:
    print(i)
cursor.close()
db.close()  # 结尾要关闭句柄和数据库
