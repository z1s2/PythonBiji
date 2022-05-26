import pymysql as mdb
import sys
#将con设定为全局变量，连接数据库
db = mdb.connect(host='10.231.128.65', port=3306, user='dev_w', passwd='6nvjq0_HW',
                         charset='utf8')
#获取连接的游标 cursor,
cursor = db.cursor()

#SQL插入语句
#插入日维度有发布订单的商户信息数据结构：
sql1 = """INSERT INTO `bd_api`.`api_div_supplier_day`
(`id`, `cal_dt`, `supplier_id`, `supplier_name`, `city_id`, `div_id`, `div_name`, `supplier_category`, `bill_finish_order_cnt`)
VALUES (5552950, 20211202, 45743079, '豆腐脑包子铺(天安们店)', 2, 23676, '北京-天通苑区域', 5, 3)"""

##插入日维度商户雨强单量数据
sql2 ="""INSERT INTO `bd_api`.`api_rainfall_order_supplier_day`
(`id`, `cal_dt`, `supplier_id`, `city_id`, `rainfall_intensity`, `bill_finish_order_cnt`)
VALUES (606193, 20211129, 100104219, 1, 0.67, 3)"""

#循环数据：
li = []
for i in range(20,30):
    li.append((i,"学生%s" %i))


try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    db.commit()
except:
    #Rollback in case there is any error
    db.rollback()

db.close()

##执行查询条件
with db:
    cur = db.cursor()
    cur.execute('SELECT * FROM bd_api.api_rainfall_order_supplier_day order by id desc limit 0,50')
    #使用fetchall，将结果集（插入数据，多维元祖类型）存入rows里面
    rows = cur.fetchall()
    for row in rows:
        print(row)








####同时插入大批量数据
import pymysql

conn = pymysql.connect(
    host = "127.0.0.1",
    port=3306,
    user='root',
    password='root',
    database='pytest3',
    charset='utf8'
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# res = cursor.execute(""" select * from aaa ;""")
li = []
for i in range(20,30):
    li.append((i,"学生%s" %i))

cursor.executemany(""" insert into aaa(id, name) values(%s,"%s")""", li)

conn.commit()

print('ok')



