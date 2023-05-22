import os.path

import pymysql as pymysql



filename = 'stu_text'


def insert_datas():
    coon = ConnectDatabase()  #实例化类对象，调用类下的connect_database()方法
    cur = coon.connect_database().cursor()    #调用connect_database()方法下的cursor()属性
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
                           # print(sql_update)
                           cur.execute(sql_update)
                       else:
                           sql_insert = f"insert into STUDENTMANAGERINFO (STUDENT_NUMBER,STUDENT_NAME,MATH_SCORE,CHINESE_SCORE) " \
                                        f"values ('{stu_list.get('学号')}'," \
                                        f"'{stu_list.get('姓名')}'," \
                                        f"'{stu_list.get('数学成绩')}'," \
                                        f"'{stu_list.get('语文成绩')}'" \
                                        f")"
                           # print(sql_insert)
                           cur.execute(sql_insert)
               else:
                   #如果元组大小为0，说明没有查到数据，直接插入
                   sql_insert = f"insert into STUDENTMANAGERINFO (STUDENT_NUMBER,STUDENT_NAME,MATH_SCORE,CHINESE_SCORE) " \
                                f"values ('{stu_list.get('学号')}'," \
                                f"'{stu_list.get('姓名')}'," \
                                f"'{stu_list.get('数学成绩')}'," \
                                f"'{stu_list.get('语文成绩')}'" \
                                f")"
                   # print(sql_insert)
                   cur.execute(sql_insert)
       cur.close()
       coon.connect_database().close()

    else:
        return


def query_datas():
    connect =ConnectDatabase()
    sql = """
    select * from STUDENTMANAGERINFO order by STUDENT_NUMBER desc limit 10;
    """
    connect.connect_database()
    cur = connect.connect_database().cursor()
    cur.execute(sql)
    rev = cur.fetchall()
    lst = []
    for msg in rev:
        msg_list = list(msg)
        msg_dict = {'学号': msg_list[0], '姓名': msg_list[1], '数学成绩': msg_list[2], '语文成绩': msg_list[3]}
        lst.append(msg_dict)
    if len(lst) == 0:
        print('无学生信息！')
    else:
        #定义学生信息标题
        format_text = '{}\t\t\t{}\t\t\t{}\t\t\t{}\t'
        print(format_text.format('学 号', '姓 名', '数学成绩', '语文成绩'))
        print('*' * 50)
        for i in lst:
            # for key,value in stu_info_dict:
            # 定义学生信息展示内容
            print('{}\t\t\t{}\t\t\t{}\t\t\t{}\t'.format(i.get('学号'),  # 从字典中取值可使用get()方法
                                                          i.get('姓名'),
                                                          i.get('数学成绩'),
                                                          i.get('语文成绩'),
                                                          ))


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
        # sql = "create table STUDENTMANAGERINFO (" \
        #                       'STUDENT_NUMBER VARCHAR(120)  NOT NULL,' \
        #                       'STUDENT_NAME VARCHAR(120) DEFAULT  NULL,' \
        #                       'MATH_SCORE VARCHAR(120) DEFAULT NULL,' \
        #                       'CHINESE_SCORE VARCHAR(120) DEFAULT NULL,' \
        #                       'PRIMARY KEY (STUDENT_NUMBER)' \
        #                       ") ENGINE=MYISAM DEFAULT CHARSET=utf8;"
        #
        # cur = coon.cursor()
        # cur.execute(sql)
        # coon.close()
        return coon
    def insert_datas(self):
        coon = ConnectDatabase()  #实例化类对象，调用类下的connect_database()方法
        cur = coon.connect_database().cursor()    #调用connect_database()方法下的cursor()属性
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
                               # print(sql_update)
                               cur.execute(sql_update)
                           else:
                               sql_insert = f"insert into STUDENTMANAGERINFO (STUDENT_NUMBER,STUDENT_NAME,MATH_SCORE,CHINESE_SCORE) " \
                                            f"values ('{stu_list.get('学号')}'," \
                                            f"'{stu_list.get('姓名')}'," \
                                            f"'{stu_list.get('数学成绩')}'," \
                                            f"'{stu_list.get('语文成绩')}'" \
                                            f")"
                               # print(sql_insert)
                               cur.execute(sql_insert)
                   else:
                       #如果元组大小为0，说明没有查到数据，直接插入
                       sql_insert = f"insert into STUDENTMANAGERINFO (STUDENT_NUMBER,STUDENT_NAME,MATH_SCORE,CHINESE_SCORE) " \
                                    f"values ('{stu_list.get('学号')}'," \
                                    f"'{stu_list.get('姓名')}'," \
                                    f"'{stu_list.get('数学成绩')}'," \
                                    f"'{stu_list.get('语文成绩')}'" \
                                    f")"
                       # print(sql_insert)
                       cur.execute(sql_insert)
           cur.close()
           coon.connect_database().close()

        else:
            return
    def query_datas(self):
        connect =ConnectDatabase()
        sql = """
        select * from STUDENTMANAGERINFO order by STUDENT_NUMBER desc limit 10;
        """
        connect.connect_database()
        cur = connect.connect_database().cursor()
        cur.execute(sql)
        rev = cur.fetchall()
        lst = []
        for msg in rev:
            msg_list = list(msg)
            msg_dict = {'学号': msg_list[0], '姓名': msg_list[1], '数学成绩': msg_list[2], '语文成绩': msg_list[3]}
            lst.append(msg_dict)
        if len(lst) == 0:
            print('无学生信息！')
        else:
            #定义学生信息标题
            format_text = '{}\t\t\t{}\t\t\t{}\t\t\t{}\t'
            print(format_text.format('学 号', '姓 名', '数学成绩', '语文成绩'))
            print('*' * 50)
            for i in lst:
                # for key,value in stu_info_dict:
                # 定义学生信息展示内容
                print('{}\t\t\t{}\t\t\t{}\t\t\t{}\t'.format(i.get('学号'),  # 从字典中取值可使用get()方法
                                                              i.get('姓名'),
                                                              i.get('数学成绩'),
                                                              i.get('语文成绩'),
                                                              ))




if __name__ == '__main__':
    # ConnectDatabase().connect_database()
    query_datas()