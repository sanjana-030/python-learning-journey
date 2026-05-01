"""
Employee Management System
Features:

Add employees
Salary calculation
Department management
Update / remove records
Search & display


Employee Management System
employee(emp_id,emp_name,emp_add,emp_mob)
department(dept_id,dept_name,dept_salary)
report(emp_id,dept_id,salary)
"""
# A METHOD TO GET EMPLOYEE
def getemployee():
    emp = []
    file = open('emp.bin', 'rb')
    emp_id = int(input("\n\tENTER EMP_ID: "))

    try:
        while True:
            data = pickle.load(file)

            if data == emp_id:
                emp.append(data)

                for i in range(3):
                    emp.append(pickle.load(file))

    except :
        pass
    file.close()
    if len(emp) == 4:
        print("\n\tEMPLOYEE FOUND")
        print("\tID:", emp[0])
        print("\tName:", emp[1])
        print("\tAddress:", emp[2])
        print("\tMobile:", emp[3])
    else:
        print("\n\tEMPLOYEE NOT FOUND")

    input("\n\tPRESS ENTER TO CONTINUE...")
# A METHOD TO VIEWREPORT
def viewreport():
    file= open('rep.bin','rb')
    try:
        print("EMP_ID\tDEPT_ID\tSALARY")
        while True:
            for i in range(3):
                data=pickle.load(file)
                print(data,end="\t")
            print()
    except:
        pass
    file.close()
    print("\n\t HERE IS REPORT !")
    input("\n\t PRESS ENTER TO CONTINUE....")
# REPORT
def report():
    file = open('rep.bin','ab')
    emp_id = int(input("ENTER A EMP_ID:"))
    file2 = open('dept.bin', 'rb')
    print("DEPARTMENTS")
    print("ID\tNAME\tSALARY")
    print("----------------------")
    try:
        while True:
            for i in range(3):
               data = pickle.load(file2)
               print(data,end="\t")
            print()
    except:
        pass
    file2.close()
           
    dept_id = int(input("ENTER A DEPT_ID:"))
    salary = int(input("ENTER A SALARY:"))
    pickle.dump(emp_id,file) 
    pickle.dump(dept_id,file)             
    pickle.dump(salary,file)        
    file.close()   
    print("\n\t EMPLOYEE ADDED SUCCESFULLY!")
    input("\n\t PRESS ENTER TO CONTINUE....")             
# A METHOD TO REMOVE DEPARTMENT
def removedepartment():
    file = open('dept.bin','rb')
    file2 = open('temp.bin','ab')
    dept_id = int(input("ENTER A DEPT_ID TO REMOVE:"))
    flag = 0
    try:
        while True:
            data = pickle.load(file)
            if dept_id==data:
                pickle.load(file)
                pickle.load(file)
                flag=1
            else:
                pickle.dump(data,file2)
    except:
        pass            
    file.close()
    file2.close()
    os.remove('dept.bin')
    os.rename('temp.bin','dept.bin')
    if flag==1:
        print("\n\t REMOVED SUCCESSFULLY:")
    else:
        print("\n\t NOT FOUND !")
    input("\n\t PRESS ENTER TO CONTINUE....")
#A METHOD TO UPDATE DEPARTMENT
def updatedepartment():
    file = open('dept.bin','rb')
    file2 = open('temp.bin','wb')
    dept_id =int(input("ENTER DEPT_ID UPDATED:"))
    flag = 0
    try:
        while True:
            data = pickle.load(file)
            if dept_id==data:
                pickle.dump(data,file2)
                name = pickle.load(file)
                print("\n\tName",name)
                pickle.dump(name,file2)
                pickle.load(file)
                salary = input("ENTER A NEW SALARY:")
                pickle.dump(salary,file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        pass
    file.close()
    file2.close()
    os.remove('dept.bin')
    os.rename('temp.bin','dept.bin')
    if flag==1:
        print("UPDATED")
    else:
        print("NOT FOUND")
        input("\n\t PRESS ENTER TO CONTINUE....")
        
    
#A METHOD TO VIEW ALL DEPARTMENTS
def viewalldepartments():
    file = open('dept.bin','rb')
    try:
        print("ID\tNAME\tSALARY")
        while True:
            for i in range(3):
                data = pickle.load(file)
                print(data,end="\t")
            print()
    except:
        pass
    file.close()
    print("\n\t DEPARTMENTS LIST!")
    input("\n\t PRESS ENTER TO CONTINUE....")
            

#A METHOD TO ADD DEPARTMENT
def adddepartment():
    file = open('dept.bin','ab')
    dept_id = int(input("Enter Department ID:"))
    dept_name = input("Enter Department NAME:")
    dept_salary = input("Enter Department SALARY:")
    pickle.dump(dept_id,file)
    pickle.dump(dept_name,file)
    pickle.dump(dept_salary,file)
    file.close()
    print("\n\t EMPLOYEE ADDED SUCCESFULLY!")
    input("\n\t PRESS ENTER TO CONTINUE....")
    
import pickle
import os
# A METHOD TO REMOVE EMPLOYEE
def removeemployee():
    file = open('emp.bin','rb')
    file2 = open('temp.bin','ab')
    emp_id = int(input("\n\tEnter Emp_Id To Remove Employee:"))
    flag = 0
    try:
        while True:
            data = pickle.load(file)
            if emp_id ==data:
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
                falg = 1
            else:
                pickle.dump(data,file2)
    except:
         pass
        
    file.close()
    file2.close()        
    os.remove('emp.bin')
    os.rename('temp.bin','emp.bin')
    if flag==1:
        print("\n\t EMPLOYEES REMOVED!")
    else:
        print("\n\t EMPLOYEE NOT FOUND!")
    input("\n\t PRESS ENTER TO CONTINUE....")
#METHOD TO VIEW ALL EMPLOYEES           
def viewallemployees():
    file = open('emp.bin','rb')
    try:
        print("ID\tNAME\tADD\tMOB")
        while True:
            for i in range(4):
                data=pickle.load(file)
                print(data,end="\t")
            print()
    except:
        pass
    file.close()
    print("\n\t DEPARTMENTS LIST!")
    input("\n\t PRESS ENTER TO CONTINUE....")
            
#METHOD LIBARY
import pickle
#METHOD TO ADD EMPLOYEE
def addemployee():
    file = open('emp.bin','ab')
    emp_id = int(input("\n\tEnter New Emp Id:"))
    emp_name = input("\n\tEnter Emp Name:")
    emp_add = input("\n\tEnter Emp Add:")
    emp_mob = input("\n\tEnter Emp_Mob:")
    pickle.dump(emp_id,file)
    pickle.dump(emp_name,file)
    pickle.dump(emp_add,file)
    pickle.dump(emp_mob,file)
    file.close()
    print("\n\t EMPLOYEE ADDED SUCCESFULLY!")
    input("\n\t PRESS ENTER TO CONTINUE....")

print("\n\t Employee Management System")
while True:
    print("\t--------------------------------")
    print("""  0- EXIT
    1- ADD EMPLOYEE
    2- VIEW ALL EMPLOYEES
    3- REMOVE EMPLOYEE
    4- ADD DEPATMENT
    5- VIEW ALL DEPARTMENTS
    6- UPDATE DEPARTMENT
    7- REMOVE DEPARTMENT
    8- CREATE REPORT
    9- VIEW REPORT
    10-GET EMPLOYEE""")
    
    
    choice =int(input("Enter your choice:"))
    if choice==0:
        print("\n\tThank you!")
        break
    if choice==1:
        addemployee()
    if choice==2:
        viewallemployees()
    if choice==3:
        removeemployee()
    if choice==4:
        adddepartment()
    if choice==5:
        viewalldepartments()
    if choice==6:
        updatedepartment()
    if choice==7:
        removedepartment()
    if choice==8:
        report()
    if choice==9:
        viewreport()
    if choice ==10:
        getemployee()
    
