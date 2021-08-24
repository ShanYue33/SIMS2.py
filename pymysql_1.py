# -*- coding:utf-8 -*-
# @Project Name:main.py
# @FileName          :pymysql_1.py
# @Create Date       :2021/8/23 10:28
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
import pymysql as ps

config = {
"host":"localhost",
"port":3306,  # 端口
"user":"root",  # 用户名
"password":"2770205",  # 密码
"database":"simsdb",  # 数据库名
}
db = ps.connect(**config)

cursor = db.cursor()

sql = '''select * from student
         where name='张三丰'
      '''
cursor.execute(sql)
results = cursor.fetchall()  # fetchone() 取第一个结果记录
for i in results:
    print(i)

cursor.close()
db.close()
