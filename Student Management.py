#SOURCE CODE FOR Student Management
print("****Student Management****")

#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists pystudent")
mycursor.execute("use pystudent")
#creating required tables 
mycursor.execute("create table if not exists pystudent(id varchar(25) not null,name varchar(50) not null,class varchar(25) not null,roll_no varchar(25),gender char(1))")
mycursor.execute("create table if not exists login(username varchar(25) not null,password varchar(25) not null)")
mycursor.execute("create table if not exists test_marks(id varchar(25) not null,name varchar(25) not null,class varchar(25) not null,eng varchar(25) not null,maths varchar(25) not null, science varchar(25) not null,hindi varchar(25) not null,computer varchar(25) not null)")
mycursor.execute("create table if not exists exam_marks(id varchar(25) not null,name varchar(25) not null,class varchar(25) not null,eng varchar(25) not null,maths varchar(25) not null, science varchar(25) not null,hindi varchar(25) not null,computer varchar(25) not null)")
mycursor.execute("create table if not exists passout(id varchar(25) not null,name varchar(50) not null,class varchar(25) not null,roll_no varchar(25),gender char(1))")
j=0
mycursor.execute("select * from login")
for i in mycursor:
    j=1
if(j==0):
    mycursor.execute("insert into login values('Admin','ng')")
else:
    pass
mydb.commit()
while(True):
    passwrd=input("Enter your password: ")
    mycursor.execute("select * from login")
    for i in mycursor:
        username,paswrd=i
    if(paswrd==passwrd):
        loop1='y'
        while(loop1=='y' or loop1=='Y'):
            print("______________________________________________")
            print("1.Enter Data for new student")
            print("2.Enter Marks of Students")
            print("3.Displaying Student Data")
            print("4.Displaying marks of any student")
            print("5.Remove student record")
            print("6.Displaying passed out students")
            print("7.Change Password")
            print("8.Change Session")
            print("9.Logout")
            print("_______________________________________________")
            ch=int(input("Enter your choice:"))
#PROCEDURE FOR Entering A NEW Student Record
            if(ch==1):
                print("All information prompted are mandatory to be filled")
                mycursor.execute("select * from pystudent")
                j=1
                for i in mycursor:
                    j+=1
                name=input("Enter name(limit 35 characters):")
                classs=str(input("Enter Class:"))
                roll_no=str(input("Enter Roll Number:"))
                gender=str(input("Enter Gender(M/F):"))
        
                mycursor.execute("insert into pystudent values('"+str(j)+"','"+name+"','"+classs+"','"+roll_no+"','"+gender+"')")
                mydb.commit()
                print("Student record has been saved successfully!!")
        
#PROCEDURE FOR Entering Marks of student
            elif(ch==2):
                marks_optn='y'
                while(marks_optn=='y' or marks_optn=='Y'):
                    print("________________________________________")
                    print("1.Enter Tests Marks: ")
                    print("2.Enter Exam Marks: ")
                    print("________________________________________")
                    
                    ch=int(input("Enter your choice: "))
                    if(ch==1):
                            ######################Test marks
                        idd=input("Enter the id of that student")
                        mycursor.execute("select * from pystudent where id='"+idd+"'")
                        for i in mycursor:
                            t_id,t_name,t_class,t_roll,t_gender=i
                        print(f"name of the student is {t_name}")
                        print("please enter marks less than 25....")
                        eng=int(input("Enter marks in english: "))
                        maths=int(input("Enter marks in maths: "))
                        science=int(input("Enter marks in science: "))
                        hindi=int(input("Enter marks in hindi: "))
                        computer=int(input("Enter marks in computer: "))
                        if(eng<=25 and maths<=25 and science<=25 and hindi<=25 and computer<=25):
                            mycursor.execute("insert into test_marks values('"+t_id+"','"+t_name+"','"+t_class+"','"+str(eng)+"','"+str(maths)+"','"+str(science)+"','"+str(hindi)+"','"+str(computer)+"')")
                            mydb.commit()
                        else:
                            print("marks are incorrect")
                        marks_optn=input("Do you want to enter more marks(y/n): ")
                                ########################Exam marks
                    elif(ch==2):
                        idd=input("Enter the id of that student")
                        mycursor.execute("select * from pystudent where id='"+idd+"'")
                        for i in mycursor:
                            t_id,t_name,t_class,t_roll,t_gender=i
                        print(f"name of the student is {t_name}")
                        print("please enter marks less than 100....")
                        eng=int(input("Enter marks in english: "))
                        maths=int(input("Enter marks in maths: "))
                        science=int(input("Enter marks in science: "))
                        hindi=int(input("Enter marks in hindi: "))
                        computer=int(input("Enter marks in computer: "))
                        if(eng<=100 and maths<=100 and science<=100 and hindi<=100 and computer<=100):
                            mycursor.execute("insert into exam_marks values('"+t_id+"','"+t_name+"','"+t_class+"','"+str(eng)+"','"+str(maths)+"','"+str(science)+"','"+str(hindi)+"','"+str(computer)+"')")
                            mydb.commit()
                        else:
                            print("marks are incorrect")
                        marks_optn=input("Do you want to enter more marks(y/n): ")
#PROCEDURE FOR displaying Student record

            elif(ch==3):
                roll_no=str(input("Enter student roll_no:"))
                mycursor.execute("select * from pystudent where roll_no='"+roll_no+"'")
                for i in mycursor:
                    t_id,name,classs,roll_no,gender=i
                print(f"id:- {t_id}")
                print(f'Name:- {name}')
                print(f'Class:- {classs}')
                print(f'Roll Number:- {roll_no}')
                print(f'gender:- {gender}')
#Procedure for displaying marks
            elif(ch==4):
                idd=input("Enter student id: ")
                mycursor.execute("select * from test_marks where id='"+idd+"'")
                print("---------------------------Test Marks----------------------------------------")
                print("|ID | NAME | CLASS | ENGLISH | MATHS | SCIENCE | HINDI | COMPUTER |")
                for i in mycursor:
                    t_id,t_name,t_class,ts1,ts2,ts3,ts4,ts5=i
                    print(f"{t_id} | {t_name} | {t_class} | {ts1} | {ts2} | {ts3} | {ts4} | {ts5} ")
                print("\n---------------------------Exam Marks---------------------------------------")
                mycursor.execute("select * from exam_marks where id='"+idd+"'")
                print("|ID | NAME | CLASS | ENGLISH | MATHS | SCIENCE | HINDI | COMPUTER |")
                for i in mycursor:
                    t_id,t_name,t_class,ts1,ts2,ts3,ts4,ts5=i
                    print(f"{t_id} | {t_name} | {t_class} | {ts1} | {ts2} | {ts3} | {ts4} | {ts5} ")
                print("")
                    

#PROCEDURE FOR DELETING STUDENT RECORD
            elif(ch==5):
                idd=str(input("Enter Student id: "))
                mycursor.execute("delete from pystudent where id='"+idd+"'")
                mydb.commit()
                mycursor.execute("delete from test_marks where id='"+idd+"'")
                mycursor.execute("delete from exam_marks where id='"+idd+"'")
                mydb.commit()
            
                print("Student Record is successfully Deleted")
            elif(ch==6):
                mycursor.execute("select * from passout")
                print("| ID | NAME | CLASS | ROLL NO | GENDER |")
                for i in mycursor:
                    t_id,t_name,t_class,t_roll,t_gender=i
                    print(f" {t_id} | {t_name} | {t_class} | {t_roll} | {t_gender} |")
#procedure for changing password
            elif(ch==7):
                pas=input("Enter Old Password: ")
                mycursor.execute("select * from login")
                for i in mycursor:
                    user_name,password=i
                if(pas==password):
                    npas=input("Enter new password: ")
                    mycursor.execute("update login set password='"+npas+"'")
                    mydb.commit()
                    print("password has been successfully Changed...")
            elif(ch==8):
                confirm=input("Do you really want to change Session(y/n): ")
                if(confirm=='y'or confirm=='Y'):
                    mycursor.execute("select * from pystudent")
                    for i in mycursor:
                        t_id,t_name,t_class,t_roll,t_gender=i
                        t_class=int(t_class)+1
                        if(int(t_class)<=12):
                            mycursor.execute("update pystudent set class='"+str(t_class)+"'")
                        else:
                            mycursor.execute("delete from pystudent where id='"+t_id+"'")
                            mycursor.execute("insert into passout values('"+t_id+"','"+t_name+"','passes out','"+t_roll+"','"+t_gender+"')")
                            mydb.commit()
                        
                            
                    

        
            else:
                break
                    
            
