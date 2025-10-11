
from pymysql import  Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="V4Nn9fa#Xf!"
)


# 获取游标对像
cursor = conn.cursor()
conn.select_db("box")

# # 执行sql
# cursor.execute("create table test(id int);")

# 查询功能
cursor.execute("select * from user")

result = cursor.fetchall()

for r in result:
    print(r)



conn.close()



