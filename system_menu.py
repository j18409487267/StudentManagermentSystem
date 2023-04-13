from student_manager_system import  StudentManagermentSystem



class SystemMenu:

    def system_menu(self):
        while True:
            try:
                SystemMenu().system_interface()
                num = int(input("请输入你要进行的操作！！！" + '\n'))
                if num in [0, 1, 2, 3, 4, 5, 6, 7]:
                    if num == 0:
                        num1 = input('你确定要退出吗？y/n \n')
                        if num1 == 'y' or num1 == 'Y':
                            print('谢谢使用！')
                            break  # 退出系统
                    elif num == 1:
                        StudentManagermentSystem().query_students()
                    elif num == 2:
                        StudentManagermentSystem().add_students()
                    elif num == 3:
                        StudentManagermentSystem().update_students()
                    elif num == 4:
                        StudentManagermentSystem().delete_students()
                    elif num == 5:
                        StudentManagermentSystem().show_all_student()
                    elif num == 6:
                        StudentManagermentSystem().revers_students()
                    else:
                        StudentManagermentSystem().counts_students()
                else:
                    print("你的输入有误，请重新输入！")
                    continue
            except:
                print('你的输入有误，请重新输入！')
                continue
    def system_interface(self):
        print("===================欢迎使用学生管理系统====================")
        print('=======================功能菜单==========================')
        print("\t\t\t\t\t\t1、查询学生信息")
        print("\t\t\t\t\t\t2、添加学生信息")
        print("\t\t\t\t\t\t3、修改学生信息")
        print("\t\t\t\t\t\t4、删除学生信息")
        print("\t\t\t\t\t\t5、展示所有学生信息")
        print("\t\t\t\t\t\t6、学生排序")
        print("\t\t\t\t\t\t7、统计学生人数")
        print('\t\t\t\t\t\t0、退出系统')
        print('========================================================')

