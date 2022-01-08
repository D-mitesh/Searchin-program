class school:
    def __init__(self):
        try:
            self.user=input("Please enter who you are!Student/Teacher/exit : ").lower()
            if self.user=="student":
                self.schstud(self.user)
            elif self.user=="teacher":
                self.schteach(self.user)
            else:
                print("Wrong input")
                exit()
        except Exception as error:
            print("You have been an error occured!")
            print("==>",error)
    def schstud(self,user):
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",user="root",password="0404",database="school")
        print("Connection successfull!")
        pointer=mydb.cursor()
        print("I am in Student!")
        ch=input("Enter Login/Register : ").lower()
        def studlogin():
            uname=input("Enter your username : ")
            pas=input("Enter your password : ")
            show="select * from student"
            pointer.execute(show)
            data=pointer.fetchall()
            for i in data:
                if i[0]==uname:
                    print("You are here!")
                    if i[1]==pas:
                        print("You are logged in!")
                        self.studaccess(user,uname)
                        break
                    else:
                        print("You've entered incorrect password!Please enter correct password")
                        studlogin()
                    break
            else:
                print("You are not here!Please first register yourself")
                reg=input("Enter yes for registration or enter back : ").lower()
                if reg=="yes":
                    studreg()
                else:
                    exit()
        def studreg():
            uname=input("Create your username : ")
            pas=input("Create your password : ")
            name=input("Enter your name : ")
            fname=input("Enter your father's name : ")
            mname=input("Enter your mother's name : ")
            bdate=input("Enter your birthdate : ")
            email=input("Enter your email id : ")
            mno=int(input("Enter your mobile number : "))
            Doa=input("Enter Date of your Admission : ")
            tup=(uname,pas,name,fname,mname,bdate,email,mno,Doa)
            ins="insert into student(Username,Password,Name,Fathername,Mothername,Birthdate,Email,Mobileno,Dateofadmission) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            pointer.execute(ins,tup)
            mydb.commit()
            print("Your data is saved!")
            mydb.close()
        if ch=="login":
            studlogin()
        elif ch=="register":
            print("Please enter your details for registration!")
            studreg()
        else:
            print("Wrong input!")
    def schteach(self,user):
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",user="root",password="0404",database="school")
        print("Connection successfull!")
        pointer=mydb.cursor()
        print("I am in Teacher!")
        ch=input("Enter Login/Register : ").lower()
        def teachlogin():
            uname=input("Enter your username : ")
            pas=input("Enter your password : ")
            show="select * from teacher"
            pointer.execute(show)
            data=pointer.fetchall()
            for i in data:
                if i[0]==uname:
                    print("You are here!")
                    if i[1]==pas:
                        print("You are logged in!")
                        self.teachaccess(user,uname)
                        break
                    else:
                        print("You've entered incorrect password!Please enter correct one")
                        teachlogin()
                    break
            else:
                print("You are not here!Please register yourself")
                reg=input("Enter yes for registration or enter back : ").lower()
                if reg=="yes":
                    teachreg()
                else:
                    exit()
        def teachreg():
            uname=input("Create your username : ")
            pas=input("Create your password : ")
            name=input("Enter your name : ")
            mno=input("Enter your mobile number : ")
            email=input("Enter your email id : ")
            tup=(uname,pas,name,mno,email)
            ins="insert into teacher values(%s,%s,%s,%s,%s)"
            pointer.execute(ins,tup)
            mydb.commit()
            print("Your data is saved!")
            mydb.close()
        if ch=="login":
            teachlogin()
        elif ch=="register":
            print("Please enter your details for registration!")
            teachreg()
        else:
            print("Wrong input!")
    #Access to a student after login:1>View his/her details,2>Update his/her personal details
    def studaccess(self,user,uname):
        try:
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",password="0404",database="school")
            pointer=mydb.cursor()
            print("Hi!"+uname)
            print("1>View his/her details,2>Update his/her personal details")
            opt=input("Enter the option : ").lower()
            if opt=="1":
                view="select * from student where Username=%s"
                pointer.execute(view,(uname,))
                data=pointer.fetchall()
                for i in data:
                    print("Here is your details : ")
                    print(data)
            elif opt=="2":
                self.updation(user,uname)
            else:
                print("Wrong input!")
        except Exception as error:
            print("You have been an error occured!")
            print("==>",error)
    #Access to a teacher after login:1>View his/her details,2>Update his/her personal details,3>View students details,4>Add more students,5>update student details
    def teachaccess(self,user,uname):
        try:
            import mysql.connector
            mydb=mysql.connector.connect(host="localhost",user="root",password="0404",database="school")
            pointer=mydb.cursor()
            print("Hi!"+uname)
            print("1>View his/her details,2>Update his/her personal details,3>View students details,4>Add more students,5>update student details,6>Provide roll number and registration to a student")
            opt=input("Enter the option : ").lower()
            if opt=="1":
                view="select * from teacher where Username=%s"
                pointer.execute(view,(uname,))
                data=pointer.fetchall()
                for i in data:
                    print("Here is your details : ")
                    print(data)
            elif opt=="2":
                self.updation(user,uname)
            elif opt=="3":
                stuname=input("Enter the username of student which data you want to see : ")
                view="select * from student where Username=%s"
                pointer.execute(view,(stuname,))
                data=pointer.fetchall()
                for i in data:
                    print("Here is your details : ")
                    print(data)
            elif opt=="4":
                uname=input("Create your username : ")
                pas=input("Create your password : ")
                name=input("Enter your name : ")
                fname=input("Enter your father's name : ")
                mname=input("Enter your mother's name : ")
                bdate=input("Enter your birthdate : ")
                email=input("Enter your email id : ")
                mno=int(input("Enter your mobile number : "))
                Doa=input("Enter Date of your Admission : ")
                roll=int(input("Assign a roll number : "))
                regid=input("Provide registration id : ")
                tup=(uname,pas,name,fname,mname,bdate,email,mno,Doa,roll,regid)
                ins="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                pointer.execute(ins,tup)
                mydb.commit()
                print("Data is added!")
                mydb.close()
            elif opt=="5":
                self.updation(user,uname)
            elif opt=="6":
                nme=input("Enter the name of student : ")
                roll=int(input("Roll number : "))
                regid=input("Registration id : ")
                pro="update student Rollno=%s,Registrationid=%s where name=%s;"
                pointer.execute(pro,(roll,regid,nme))
                mydb.commit()
                print("Roll no. and registration id is provided!")
                mydb.close()
            else:
                exit()
        except Exception as error:
            print("You have been an error occured!")
            print("==>",error)
    def updation(user,uname):
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",user="root",password="0404",database="school")
        pointer=mydb.cursor()
        def updatestud(stud_username):
            print("To Update ",stud_username,"data : ")
            print("Press 1 for : Name")
            print("Press 2 for : Father's Name")
            print("Press 3 for : Mother's Name")
            print("Press 4 for : Birthdate")
            print("Press 5 for : Mobile Number")
            print("Press 6 for : Email")
            print("Press 7 for : Date Of Admission")
            opt = input("Write Here :").lower()
            if opt=="1":
                val=input("Enter the value : ")
                updt=("update student set Name=%s where Username=%s;")
                pointer.execute(updt,(val,stud_username))
                mydb.commit()
                print("Update successfully")
            elif opt=="2":
                val=input("Enter the value : ")
                updt=("update student set Fathername=%s where Username=%s;")
                pointer.execute(updt,(val,stud_username))
                mydb.commit()
                print("Update successfully")
            elif opt=="3":
                val=input("Enter the value : ")
                updt=("update student set Mothername=%s where Username=%s;")
                pointer.execute(updt,(val,stud_username))
                mydb.commit()
                print("Update successfully")
            elif opt=="4":
                val=input("Enter the value : ")
                updt=("update student set Birthdate=%s where Username=%s;")
                pointer.execute(updt,(val,stud_username))
                mydb.commit()
                print("Update successfully")
            elif opt=="5":
                val=input("Enter the value : ")
                updt=("update student set Mobileno=%s where Username=%s;")
                pointer.execute(updt,(val,stud_username))
                mydb.commit()
                print("Update successfully")
            elif opt=="6":
                val=input("Enter the value : ")
                updt=("update student set email=%s where Username=%s;")
                pointer.execute(updt,(val,stud_username))
                mydb.commit()
                print("Update successfully")
            elif opt=="7":
                val=input("Enter the value : ")
                updt=("update student set dateofadmission=%s where Username=%s;")
                pointer.execute(updt,(val,stud_username))
                mydb.commit()
                print("Update successfully")
            else:
                print("WRONG INPUT!")
                exit()
        if user=="teacher":
            optmain=input("Enter whose data you want to update : Yourself/Students = ").lower()
            if optmain=="yourself":
                print("To update your data : ")
                print("Press 1 for : Name")
                print("Press 2 for : Mobile Number")
                print("Press 3 for : Email")
                choice=input("Enter your choice here : ").lower()
                if choice=="1":
                    val=input("Enter the value : ")
                    updt=("update student set Name=%s where Username=%s;")
                    pointer.execute(updt,(val,uname))
                    mydb.commit()
                    print("Updated successfully!")
                elif choice=="2":
                    val=input("Enter the value : ")
                    updt=("update student set Mobileno=%s where Username=%s;")
                    pointer.execute(updt,(val,uname))
                    mydb.commit()
                    print("Updated successfully!")
                else:
                    val=input("Enter the value : ")
                    updt=("update student set email=%s where Username=%s;")
                    pointer.execute(updt,(val,uname))
                    mydb.commit()
                    print("Updated successfully!")
            else:
                ustud=input("Enter student username which data you want to update : ")
                updatestud(ustud)
        elif user=="student":
            updatestud(uname)
        else:
            print("Wrong input!")
            exit()
obj=school
obj()