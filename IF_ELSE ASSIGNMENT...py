print("multi-#A. Python IF (Single Condition)
#1. Write a Python program to check if a number is positive

num = 20
if num>0:
    print("positive")
    
#2. Print "Eligible to vote" if age is 18 or above.

age =21
if age>=18:
    print("Eligible to vote")

#3.Check if a number is divisible by 7.
num = 14
if num%7==0:
    print("divisible")

#4. Print "Pass" if marks are greater than 40.
marks =50
if marks>40:
    print("pass")

#5. Check if a number is greater than 100.
num = 95
if num>100:
    print(greater)
   
#6. Display a message if temperature exceeds 45°C.
temperature = 55
if temperature>45:
    print("High alert")
    
#7. Check if a string length is more than 8 characters.

#8. Print "Logged In" if password matches "admin123".
password ="admin123"
if password=="admin123":
    print("logged in")

#9. Check if a number is a multiple of 10.
num = 20
if num%10==0:
    print("yes")
    
#10. Print a warning if balance is below minimum limit.
balance = 1000
if balance<2000:
    print("warning")
    
#B. Python IF—ELSE (Two Conditions)
#11. Check whether a number is even or odd.
num =int(input("enter a number:"))
if num%2==0:
    print("even")
else:    
    print("odd")

#12. Find the largest of two numbers.
n1 =300
n2 =40
if n1>n2:
    print(n1)
else:
    print(n2)

#13. Check whether a person is eligible for driving license.
age =13
if age>18:
    print("eligible")
else:
    print("not eligible")
    
#14. Print "Pass" or "Fail" based on marks.
marks = 95
if marks>=55:
    print("pass")
else:
    print("fail")
    
#15. Check whether a number is positive or negative.
num = -4
if num>0:
    print("positive")
else:
    print("negative")
   
#16. Check whether a character is a vowel or consonant
ch = "s"
if ch in "AIOUEaioue":
    print("vowel")
else:
    print("consonant")
 
#17. Check if a year is leap or not
"""
"""
#18. Print "Valid Password" or "Invalid Password".
password = "helloindia"
if password=="helloindia":
    print("valid password")
else:
    print("invalid password")

#19. Determine whether salary is taxable or not.
salary = 500000
if salary>=7000000:
    print("taxable")
else:
    print("not taxable")
    
#20. Check whether a number is greater than 50 or not.
num =int(input("enter a number:"))
if num>50:
    print("yes")
else:
    print("no")
    "
#C. Python NESTED IF—ELSE
#21. Find the largest of three numbers.
n1 = 10000
n2 = 4000000
n3 = 500000
if n1>n2:
    if n1>n3:
        print(n1)
    else:
        print(n3)
else:
    if n2>n3:
        print(n2)
    else:
        print(n3)
        
#22. Check whether a number is positive, negative, or zero.
num = 5
if num>0:
    if num<0:
        print("negative")
    else:
        print("positive")
else:
    print("zero")
        
#23. Assign grades:
#A → marks ≥ 90
#B → marks ≥ 75
#C → marks ≥ 60
#Fail → below 60
marks =45
if marks>=90:
    print("A")
else:
    if marks>=75:
        print("B")
    else:
        if marks>=60:
            print("C")
        else:
            print("fail")
            
        
#24. Check whether a triangle is equilateral, isosceles, or scalene   
#25. Check whether a character is uppercase, lowercase, digit, or special character.
ch ="sanjana"
if ch >="0":
    if ch<="9":
        print("digit")
    else:
        if ch>="a":
            if ch<="z":
                print("lowercase")
            else:
                if ch>="A":
                    if ch<="Z":
                        print("uppercase")
                    else:
                        print("special character")

 
#26. Calculate electricity bill using slab-wise rates.
#27. Validate login using username and password.
username ="sanjana.33"
password ="1234"
if username=="sanjana.33":
    if password=="1234":
        print("login done")
    else:
        print("not valid")
else:
    print("no valid")

#28. Check student result using marks of 3 subjects.
hindi = 40
english = 40
maths = 40
if hindi>=40:
    if english>=40:
        if maths>=40:
            print("pass")
        else:
            print("maths_fail")
    else:
        print("english_fail")
else:
    print("hindi_fail")
    
#29. Find the second largest number among three numbers.
#30. Check loan eligibility using age, salary, and credit score
age = "31"
salary = "50000"
creditscore ="700"

if age>="21":
    if salary>="50000":
        if creditscore>="700":
            print("verified")
        else:
            print("poor cs")
    else:
        print("low salary")
else:
    print("below 21")
    
#D. Python ELIF (Multiple Conditions)
#31. Print day name using day number (1—7).
num =5
if num==1:
    print("monday")
elif num==2:
    print("tuesday")
elif num==3:
    print("wednesday")
elif num==4:
    print("thursday")
elif num==5:
    print("friday")
elif num==6:
    print("saturday")
elif num==7:
    print("sunday")
else:
    print("not valid")    

#32. Print month name using month number.
num =9
if num==1:
    print("january,")
elif num==2:
    print("february")
elif num==3:
    print("march")
elif num==4:
    print("april")
elif num==5:
    print("may")
elif num==6:
    print("june")
elif num==7:
    print("july")
elif num==8:
    print("august")
elif num==9:
    print("september")
elif num==10:
    print("october")
elif num==11:
    print("november")
elif num==12:
    print("december")
else:
    print("not valid")

#33. Display grade based on percentage.
per=74
if per>=90:
    print("A")
elif per>=80:
    print("B")
elif per>=70:
    print("C")
elif per>=60:
    print("D")
else:
    print("fail")
    
#34. Display bonus percentage based on experience years.
year=4
if year>=10:
    print("15%bonus")
elif year>=5:
    print("10%bonus")
elif year>=1:
    print("5%bonus")

#35. Identify traffic signal meaning
signal="yellow"
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("slow down")
elif signal=="green":
    print("go")
    
#36. Categorize temperature as Cold / Warm / Hot.
tem =11
if tem>30:
    print("hot")
elif tem>=20:
    print("warm")
elif tem<=19:
    print("cold")
    
#37. Categorize employee based on salary range.
salary=90000
if salary>=100000:
    print("high salary")
elif salary>=50000:
    print("mid salary")
elif salary<50000:
    print("low salary")
   
#38. Print discount percentage based on purchase amount.
amt =110000
if amt>=10000:
    print("500%")
elif amt>=5000:
    print("100%")
elif amt<5000:
    print("50%")
    
#39. Identify number type: single-digit / double-digit / multi-digit.
num = 67
if num>=100:
digit")
elif num>=10:
    print("double-digit")
elif num>=1:
    print("single digit")
    
#40. Assign performance rating: Poor / Average / Good / Excellent.
rating =1
if rating==10:
    print("excellent")
elif rating==8:
    print("good")
elif rating>=5:
    print("average")
elif rating==1:
    print("poor")
    
#E. Python COMPLEX CONDITIONS (AND / OR / NOT)
#41. Check whether a number is divisible by 5 and 11
num = 55
if num%11==0 and num%5==0:
    print("divisible")
else:
    print("not")
    
#42. Check if a person is eligible for loan:
#● age ≥ 21
#● salary ≥ 25,000
#● credit score ≥ 700
age =23
salary =25000
credit_score =800
if age>=21 and salary>=25000 and credit_score>=700:
    print("eligible")
else:
    print("not eligible")
    
#43. Validate login using username AND password.
user ="sanjana"
password ="124"
if user=="sanjana" and password=="1234":
    print("login done")
else:
    print("invalid")
    
#44. Check student pass condition:
#All subjects ≥ 40
#Average ≥ 50
hindi = 85
maths =40
english =80
history =56
if hindi>=40 and maths>=40 and english>=40 and history>=40:
    print("pass")
else:
    print("fail")
    
#45. Check if a number lies between 10 and 100
num =67
if num>=10 and num<=100:
    print(num)
else:
    print("invalid")
    
#46. Check exam eligibility:
#attendance ≥ 75% OR
#medical certificate available
attendance =84
mc="no"
if attendance>=75 or mc=="yes":
    print("eligible for exam")
else:
    print("not eligible")
   
#47. Validate a date using conditions.
date =30
if date>=1 and date<=31:
    print("valid")
else:
    print("not valid")
    
#48. Check whether an email format is valid.
#49. Determine insurance eligibility using age, health status, and income
#50. Check leap year using complete leap year logic

#F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS
#51. Write a Python program to calculate income tax using slabs.
inc =300000
if inc>=2000000:
    print("25%")
elif inc>=1600000:
    print("20%tax")
elif inc>=1200000:
    print("15%tax")
elif inc>=800000:
    print("10%tax")
elif inc>=400000:
    print("5%tax")
else:
    print("0%tax")
#52. Create an ATM withdrawal program with balance checks.

#53. Check promotion eligibility using experience and performance.
per=6
exp=5
if per>=5 and exp>=4:
    print("eligible")
else:
    print("not eligible")

#54. Implement a grading system using nested if—else.
grade=69
if grade>=90:
    print("A")
else:
    if grade>=80:
        print("B")
    else:
        if grade>=70:
            print("C")
        else:
            if grade>=60:
                print("D")
            else:
                if grade<60:
                    print("fail")

#55. Validate strong password using multiple conditions

#56. Calculate delivery charges based on location and order amount
location = "50km"
order_amt=15000
if location=="50km" and order_amt>=2000:
    print("100rs charges")
elif location=="25km" and order_amt>=1000:
    print("free delivery")
elif location=="15km" and order_amt>=500:
    print("50rs charges")
elif location=="10km" and order_amt>=200:
    print("20rs charges")
    
#57. Determine online exam qualification.
#58. Create movie ticket pricing logic based on age & show time.age = 13
show_time ="3 hour"
if age>=60 and show_time=="3 hour":
    print("200+20%dis")
elif age>=19 and show_time=="3 hour":
    print("300rs")
elif age>=13 and show_time=="2 hour":
    print("100rs")
elif age>=8 and show_time=="1 hour":
    print("50+10%dis")

#59. Determine bank account type based on balance.
#60. Create a menu-driven program using if—elif—else.
