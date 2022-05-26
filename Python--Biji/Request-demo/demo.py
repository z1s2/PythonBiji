# coding=utf8
from pymysql import connect, cursors
from pymysql.err import OperationalError
import sys, time


class DataBase():  # 类名和模块名一致，robot导入时不用写类名@@@@@
    def __init__(self, mysql_name):
        try:
            self.conn = connect(host='123.。。。',
                                port=3306,
                                user='mys。。。',
                                password='。。。',
                                db=mysql_name,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor
                                )

        except OperationalError as e:
            print
            e



# 批量插入数据




# 关闭数据库


def close(self):
    self.conn.close()


if __name__ == '__main__':
    tb = DataBase('manager')
    tb.insert_inspection_list('inspection_list')
