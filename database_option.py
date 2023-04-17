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
               r_list = r_file.readlines()  #去读文件，遍历文件，获取学生信息，
               for i in r_list:
                   stu_list = dict(eval(i))
                   #查询数据库中已经存在的学生学号
                   sql_rev = f"select STUDENT_NUMBER from STUDENTMANAGERINFO  where STUDENT_NUMBER in ('{stu_list.get('学号')}') "
                   cur.execute(sql_rev)
                   new_stu_number = cur.fetchall()
                   #判断查到的学生信息是否为空
                   if len(new_stu_number) > 0:
                       query_number = list(new_stu_number)[0]  #将查到的学生信息转为列表，取列表中的元素

                       for i in query_number:  #遍历列表，将获取到的学号与文件中的学号作比较，不存在的插入，存在的更新
                           if i == stu_list.get("学号"):
                               sql_update = f"update STUDENTMANAGERINFO  set " \
                                            f"STUDENT_NAME='{stu_list.get('姓名')}'," \
                                            f"MATH_SCORE= '{stu_list.get('数学成绩')}'," \
                                            f"CHINESE_SCORE = '{stu_list.get('语文成绩')}'" \
                                            f"where STUDENT_NUMBER='{stu_list.get('学号')} '"
                               print(sql_update)
                               cur.execute(sql_update)
                           else:
                               sql_insert = f"insert into STUDENTMANAGERINFO (STUDENT_NUMBER,STUDENT_NAME,MATH_SCORE,CHINESE_SCORE) " \
                                            f"values ('{stu_list.get('学号')}'," \
                                            f"'{stu_list.get('姓名')}'," \
                                            f"'{stu_list.get('数学成绩')}'," \
                                            f"'{stu_list.get('语文成绩')}'" \
                                            f")"
                               print(sql_insert)
                               cur.execute(sql_insert)
                   else:
                       #如果元组大小为0，说明没有查到数据，直接插入
                       sql_insert = f"insert into STUDENTMANAGERINFO (STUDENT_NUMBER,STUDENT_NAME,MATH_SCORE,CHINESE_SCORE) " \
                                    f"values ('{stu_list.get('学号')}'," \
                                    f"'{stu_list.get('姓名')}'," \
                                    f"'{stu_list.get('数学成绩')}'," \
                                    f"'{stu_list.get('语文成绩')}'" \
                                    f")"
                       print(sql_insert)
                       cur.execute(sql_insert)
           cur.close()
           coon.close()

        else:
            return


    def query_datas(self):
        sql = """
        select * from STUDENTMANAGERINFO ;
        """


if __name__ == '__main__':
    # ConnectDatabase().connect_database()
    ConnectDatabase().insert_datas()