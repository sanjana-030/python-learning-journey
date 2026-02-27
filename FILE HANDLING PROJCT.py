"""
Employee Management System
Features:

Add employees
Salary calculation
Department management
Update / remove records
Search & display


Employee Management System
employee(emp_id,emp_name,emp_add,emp_dept,emp_salary)
department(dept_name,dept_salary)
"""
import pickle
import os
# A METHOD TO REMOVE EMPLOYEE
def removeemployee():
    file = open('emp.bin','rb')
    file2 = open('temp.bin','ab')
    emp_id = input("\n\tEnter Emp_Id To Remove Employee:")
    try:
        while True:
            data = pickle.load(file)
            if data==emp_id:
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
                pass
            else:
                pickle.dump(data,file2)
    except:
         pass
        
    file.close()
    file2.close()
    os.remove('emp.bin')
    os.rename('temp.bin','emp.bin')
    
#METHOD TO VIEW ALL EMPLOYEES
def viewallemployees():
    file = open('emp.bin','rb')
    try:
        print("ID\tNAME\tADD\tDEPT\tSALARY")
        while True:
            for i in range(5):
                data=pickle.load(file)
                print(data,end="\t")
            print()
    except:
        pass
    file.close()
    print("\n\t EMPLOYEES LIST!")
    input("\n\t PRESS ENTER TO CONTINUE....")
            
#METHOD LIBARY
import pickle
#METHOD TO ADD EMPLOYEE
def addemployee():
    file = open('emp.bin','ab')
    emp_id = int(input("\n\tEnter New Emp Id:"))
    emp_name = input("\n\tEnter Emp Name:")
    emp_add = input("\n\tEnter Emp Add:")
    emp_dept = input("\n\tEnter Emp Dept:")
    emp_salary =input("\n\tEnter Emp Salary:")
    pickle.dump(emp_id,file)
    pickle.dump(emp_name,file)
    pickle.dump(emp_add,file)
    pickle.dump(emp_dept,file)
    pickle.dump(emp_salary,file)
    file.close()
    print("\n\t EMPLOYEE ADDED SUCCESFULLY!")
    input("\n\t PRESS ENTER TO CONTINUE....")

print("\n\t Employee Management System")
while True:
    print("\t--------------------------------")
    print("""    0- EXIT
    1- ADD EMPLOYEE
    2- VIEW ALL EMPLOYEES
    3- REMOVE EMPLOYEE
    4- ADD DEPATMENT
    5- VIEW ALL DEPARTMENTS
    6- UPDATE DEPARTMENT
    7- REMOVE DEPARTMENT""")
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
        
    
        
        
    
