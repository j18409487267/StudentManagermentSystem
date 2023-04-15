import os.path

import pymysql as pymysql

filename = 'stu_text'
class ConnectDatabase:


    def connect_database(self):
        """
        连接数据库
        :return:
        """
        coon = pymysql.connect(
            host='127.0.0.1',
            database='jhs',
            port=3306,
            user='mysql',
            password='jhs@123jhs',
            autocommit=True
        )
        sql = "create table STUDENTMANAGERINFO (" \
                              'STUDENT_NUMBER VARCHAR(120)  NOT NULL,' \
                              'STUDENT_NAME VARCHAR(120) DEFAULT  NULL,' \
                              'MATH_SCORE VARCHAR(120) DEFAULT NULL,' \
                              'CHINESE_SCORE VARCHAR(120) DEFAULT NULL,' \
                              'PRIMARY KEY (STUDENT_NUMBER)' \
                              ") ENGINE=MYISAM DEFAULT CHARSET=utf8;"

        cur = coon.cursor()
        cur.execute(sql)
        coon.close()



    def insert_datas(self):
        coon = pymysql.connect(
            host='127.0.0.1',
            database='jhs',
            port=3306,
            user='mysql',
            password='jhs@123jhs',
            autocommit=True
        )
        cur = coon.cursor()
        if os.path.exists(filename):
           with open(filename,mode='r',encoding='utf-8')  as r_file:
               r_list = r_file.readlines()
               for i in r_list:
                   stu_list = dict(eval(i))
                   print(stu_list)

                   sql = f"insert into STUDENTMANAGERINFO (STUDENT_NUMBER,STUDENT_NAME,MATH_SCORE,CHINESE_SCORE) " \
                   f"values ({stu_list.get('学号')}" \
                   f",'{stu_list.get('姓名')}'," \
                   f"{stu_list.get('数学成绩')}," \
                   f"{stu_list.get('语文成绩')}" \
                   f")"
                   print(sql)
                   cur.execute(sql)
               coon.close()
               cur.close()





        else:
            return


    def query_datas(self):
        pass


if __name__ == '__main__':
    # ConnectDatabase().connect_database()
    ConnectDatabase().insert_datas()