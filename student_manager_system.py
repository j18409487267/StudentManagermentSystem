import os

from database_option import ConnectDatabase

filename = 'stu_text'     #将存储学生信息的文件申明为一个变量，方便在别的地方调用
class StudentManagermentSystem:
    def __init__(self):
        self.all_studets = []
    def query_students(self):
        '''
        查询学生信息
        :return:
        '''

        student = []  #存放查到的学生
        while True:
            if os.path.exists(filename):
                num = input('请输入你要查找的学生学号:\n')
                with open(filename,'r',encoding='utf-8')  as file:
                    old_info = file.readlines()
                    for i in old_info:
                        new_info = dict(eval(i))
                        if new_info['学号'] == num:
                            student.append(new_info)
                StudentManagermentSystem().show_student(student)
                student.clear()  # 查询前先清空上次查询的结果
                awser = input('是否继续查找？y/n\n')
                if awser == 'y' or awser == 'Y':
                    continue
                else:
                    break
    def show_student(self,lst):
        '''
        展示学生信息
        :param lst:
        :return:
        '''
        #判断列表中有没有信息
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
                print('{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t'.format(i.get('学号'),  # 从字典中取值可使用get()方法
                                                              i.get('姓名'),
                                                              i.get('数学成绩'),
                                                              i.get('语文成绩'),
                                                              ))
    def show_all_student(self):
        '''
        展示所有学生信息
        :return:
        '''
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as file:
                old_info = file.readlines()
        else:
            return
        #定义学生信息展示格式标题
        new_student = []
        for i in old_info:
            student_dict = dict(eval(i))
            new_student.append(student_dict)
        StudentManagermentSystem().show_student(new_student)
    def add_students(self):
            '''
            添加学生信息
            :return:
            '''
            while True:  #循环使用系统
                print("请输入学生信息:")
                number = input('学号:\n')
                if not  number:  #判断是否为空
                    break
                name = input('姓名:\n')
                if not name:
                    break
                try:
                    math = int(input("数学成绩:\n"))
                    chinese = int(input("语文成绩:\n"))
                except:
                    print('你的输入有误，请重新输入!')
                    continue
                #将学生信息存入字典保存
                student_info = {
                    '学号': number,
                    '姓名': name,
                    '数学成绩': math,
                    '语文成绩': chinese
                }
                #将学生信息存到列表保存
                self.all_studets.append(student_info)
                awser = input('是否继续录入？y/n\n')
                if awser == 'y' or awser == 'Y':
                    print('请继续录入！')
                    continue
                else:
                    break
             #将学生信息保存到文件中
            StudentManagermentSystem().save(self.all_studets)
            ConnectDatabase().insert_datas()
            print('学生信息录入完毕！')
            StudentManagermentSystem().show_all_student()
    def save(self,list):
         try:
             stu_text = open(filename,'a',encoding='utf-8')
         except:
             stu_text = open(filename, 'w', encoding='utf-8')
         for i in list:
             stu_text.write(str(i)+'\n')
         stu_text.close()
    def update_students(self):
            '''
            修改学生信息
            :return:
            '''
            ConnectDatabase().query_datas()
            if os.path.exists(filename):   #判断文件是否存在
                with open(filename, 'r', encoding='utf-8') as f:
                    old_stu_info = f.readlines()
            else:
                return
            student = []
            updata_num = input('请输入需要修改的学生学号:\n')
            if  updata_num: #判断输入是否为空
                with open(filename, 'w', encoding='utf-8') as w:
                    if old_stu_info: #判断列表是否为空，为空则退出，不为空则修改
                        for i in old_stu_info:
                            new_stu_info = dict(eval(i))
                            if new_stu_info['学号'] == updata_num:
                                student.append(new_stu_info)
                                print(f'找到学号为[{updata_num}]的学生信息为\n')
                                StudentManagermentSystem().show_student(student)
                                sure = input('是否确定要修改？y/n\n') #询问用户是否确认要修改学生信息
                                if sure == 'y' or sure == 'Y':
                                    while True:#无异常退出修改，有输入异常则提示用户循环输入
                                        try:
                                            new_stu_info['数学成绩'] = input('请输入数学成绩:')
                                            new_stu_info['语文成绩'] = input('请输入语文成绩:')
                                        except:
                                            print('你的输入有误，请重新输入！')
                                        else:
                                            break
                                    w.write(str(new_stu_info) + '\n')  #修改完成后将修改后的学生信息写入文件
                                    print('学生信息修改成功！')
                                else:
                                    return
                            else:
                                w.write(str(new_stu_info) + '\n')  #当用户输入的学号查询不到时将旧文件（原文件）写入文件
                    else:  #列表为空时直接退出
                        print('无学生信息可修改！')
                        return
            StudentManagermentSystem().show_all_student()
            awser = input('是否继续修改？y/n\n')
            if awser == 'y' or awser == 'Y':
                StudentManagermentSystem().update_students() #再次修改
            ConnectDatabase().insert_datas()
    def delete_students(self):
            '''
            删除学生信息
            :return:
            '''
            StudentManagermentSystem().show_all_student()
            while True:
                num = input('请输入学生学号:')
                #判断输入是否为空
                if num != "":
                    if os.path.exists(filename):  #判断文件是否存在，存在则读取后存到old_stu_info，不存在则创建一个空old_stu_info
                        with open(filename,'r',encoding='utf-8')  as f:
                            old_stu_info = f.readlines()
                    else:
                        old_stu_info = []
                    #设置一个删除的标志，默认False
                    flag = False
                    #判断列表是否为空，不为空则写入到stu_info_new
                    if old_stu_info :
                        with open(filename,'w',encoding='utf-8')  as old_f:

                            for i in old_stu_info:
                                stu_info_new = dict(eval(i))
                                if num != stu_info_new['学号']:
                                    old_f.write(str(stu_info_new)+'\n')
                                else:
                                    flag =True
                            if flag:
                                print(f'学号为{num}的学生信息已删除')
                            else:
                                print('没有学号为{}的学生'.format(num))
                    else:
                        print('无学生信息')
                        break
                    awnser = input("是否继续删除学生信息？y/n\n")
                    if awnser == 'y' or awnser == 'Y':
                        continue
                    else:
                        break
            StudentManagermentSystem().show_all_student()
    def counts_students(self):
        '''
        统计学生数量
        :return:
        '''
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8')  as rfile:
                student = rfile.readlines()
                if student:
                    print(f'共有【\t{len(student)}\t】名学生')  #实际是判断列表的长度，因为列表中每一个元素则为一个学生
        else:
            print('无学生信息！')
    def revers_students(self):
        '''
        学生排序
        :return:
        '''
        global asc_or_desc_mode
        StudentManagermentSystem().show_all_student()
        new_student =[]
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as r_file:
                student = r_file.readlines()
            for i in student:
                student_dict = dict(eval(i))
                new_student.append(student_dict)
        else:
            print('无学生信息')
            return
        num = int(input('请选择排序方式\t 1-升序\t0-降序\n') ) #标记排序方式，供sort()方法使用
        if num == 1:
            asc_or_desc_mode = False
        elif num == 0:
            asc_or_desc_mode = True
        else:
            print('你的输入有误，请重新输入！')
            StudentManagermentSystem().revers_students()
        sort_mode = int(input('请选择排序类别\t1-按学号排序\t2-按语文成绩排序\t3-按数学成绩排序\n'))
        if sort_mode == 1 :
            new_student.sort(key=lambda d: d['学号'],reverse=asc_or_desc_mode)   #lambda为匿名参数，d实际为new_student列表中的每一项
        elif sort_mode == 2:
            new_student.sort(key=lambda d: int(d['语文成绩']),reverse=asc_or_desc_mode)  #成绩需要转换成整型，避免排序出错
        elif sort_mode == 3:
            new_student.sort(key=lambda d: int(d['数学成绩']),reverse=asc_or_desc_mode)
        else:
            print('你的输入有误，请重新输入！')
            StudentManagermentSystem().revers_students()
        StudentManagermentSystem().show_student(new_student)  #排序结束后展示学生信息


    def truc_files(self):
        '''
        清空文件
        :return:
        '''
        if os.path.exists(filename):
            with open(filename,'w',encoding='utf-8')  as file:
                file.truncate()
        else:
            return
