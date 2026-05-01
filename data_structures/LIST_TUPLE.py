#Python Programming Questions – LIST
#Basic Level
#1. Write a Python program to create a list of integers and print its elements
"""
list=[45,19,54,45,87,12]
for i in list:
    print(i)
#2. Write a program to find the sum and average of all elements in a list.
list=[45,19,54,45,87,12]
print("average",sum(list)/len(list))

#3. Write a program to find the largest and smallest element in a list.
list=[45,19,54,45,87,12]
print("smallest value:",min(list))
print("largest value:",max(list))

#4. Write a Python program to count the number of elements in a list without using len().
list=[45,19,54,45,87,12]
count = 0
for i in list:
    count = count+1
    print(i)
print(count)

#5. Write a program to reverse a list without using built-in functions.
list=[45,19,54,45,87,12]
print(list[ : : -1])

#6. Write a program to check if an element exists in a list.
list=[45,19,54,45,87,12]
el = int(input("enter a number"))
for i in list:
    if el in list:
        print("found the element")
else:
    print("not found")
   
#7. Write a Python program to remove duplicate elements from a list.
#8. Write a program to sort a list in ascending and descending order.
list=[45,19,54,45,87,12]
list.sort()
print(list)

list.sort(reverse=True)
print(list)

#Intermediate Level
#9. Write a program to merge two lists and remove duplicates.
li = [43,56,1,2,99,83,4]
list2 =[67,23,99,43,6,56]
list3 =li+list2
print (list(set(list3)))

#10. Write a program to find common elements between two lists.
list=[45,19,54,45,87,12]
list2=[55,19,67,46,97,13]
for i in list and list2:
    if i in list and list2:
        print(i)
        
#11. Write a program to split a list into even and odd numbers.
list=[45,19,54,45,87,12]
for i in list:
    if i%2==0:
        print("even num:",i)
    elif i%2!=0:
        print("odd num:",i)
        
#12. Write a program to rotate a list by n positions.
#13. Write a Python program to find the second largest number in a list.
list=[45,19,54,45,87,12]
list.sort(reverse=True)
print(list)
print("second largest number:",list[1])

#14. Write a program to flatten a nested list.
li = [4,23,7,[82,56,58],47,9,2,[4,6,7,],74,92]
fl =[]
for i in li:
    if isinstance(i,list):
        fl.extend(i)
    else:
        fl.append(i)
print(fl)

#15. Write a program to count frequency of each element in a list.
list=[45,19,54,45,87,12]
for i in list:
    print(list.count(i),i)
    
#16. Write a program to replace all negative numbers with zero in a list.
list=[45,-5,54,45,-2,12]
for i in range(len(list)):
    if list[i]<0:
        list[i]==0
        print(list)
        
#Advanced Level
#17. Write a program to remove all occurrences of a given element from a list.
list=[45,19,54,45,87,12]
list2=[]
el = 45
for i in list:
    if i!=el:
        list2.append(i)
print(list2)

#18. Write a program to check if a list is a palindrome.
list=[1,2,1,1,2,1]
if list==list[: : -1]:
    print("palindrome", list)
else:
    print("not palindrome")
   
#19. Write a Python program to find missing numbers in a given list of consecutive integers
#20. Write a program to perform element-wise addition of two lists.
list =[10,20,30]
list2 =[1,1,1]
list3=[]
if len(list)==len(list):
        for i in range(len(list)):
         list3.append(list[i]+list2[i])
print(list3)

#21.Write a python program  to find the longest increasing subsequence in a list.
#22.Write a program to group elements based on frequency.
li =[11,45,11,45,45,2,2,2]
list2=[]
list3=[]
for i in li:
    if i not in list3:
        list3.append(i)
        list2.extend([i]*li.count(i))
print(list2)
    

##Python Programming question-Tuple
#Basic Level
#23.Write  a pyhton program  to create  a tuple  and  print its elements.
tuple = (24,56,42,84,75)
for i in tuple:
    print(i)
    
#24.Write  a program  to find the length of a tuple.
tuple = (24,56,42,84)
print(tuple)
print(len(tuple))

#25.Write  a program  to find the maximum and minimum element in a tuple.
tuple = (24,56,42,84)
print(min(tuple))
print(max(tuple))

#26.Write a  program to convert  a tuple into a list.
tuple =([53,49,15,70,43,63])
print(tuple)

#27.Write  a program to check if an element exists in a tuple.
tuple =(24,56,42,84,75)
el = int(input("enter a number:"))
for i in tuple:
    if i==el:
        print("element exists")
        break
else:
    print("not exists")

#28. Write a program to count occurrences of an element in a tuple.
tuple =(24,56,42,42,65,56,34,10,54,75)
el = 56
count = 0
for i in tuple:
    if el==i:
        count+=1
        print(el,count)
        
#29. Write a program to slice a tuple and display the result.
tuple =(24,56,42,42,65,56,34,10,54,75)
tuple =(tuple[0:7:1])
print(tuple)

#30. Write a program to find repeated elements in a tuple.
tuple =(24,56,42,42,65,56,34,10,54,75)
repeat = []
count = 0
for i in tuple:
    if tuple.count(i)>1 and i not in repeat:
        repeat.append(i)
print(repeat)

#31. Write a program to merge two tuples.
tuple =(24,56,42,42,65,56,34,10,54,75)
tuple2 =(53,49,15,70,43,63)

tuple3 =tuple + tuple2
print(tuple3)

#32. Write a program to unpack elements of a tuple into variables.
tuple = (65,38,69,26,87)
a,b,c,d,e =tuple
print(d)

#33. Write a Python program to sort a tuple.
t =(53,49,15,70,43,63)
sort_tuple = tuple(sorted(t))
print(sort_tuple)

#34. Write a program to convert a list of tuples into a dictionary.

#Advanced Level
#35. Write a program to find the index of an element in a tuple.
tuple =(53,49,15,70,43,63)
print(tuple.index(70))

#36. Write a program to remove an element from a tuple (without directly modifying it).
tuple =(53,49,15,70,43,63)
el = 70
tuple2=[]
for i in tuple:
    if i!=el:
        tuple2.append(i)
print(tuple2)

#37. Write a program to find common elements between two tuples.
tuple1 =(53,49,15,70,43,63)
tuple2 =(54,49,14,70,89,90)
tuple3 = []
for i in tuple1:
    if i in tuple2:
        tuple3.append(i)
print(tuple3)

#38. Write a Python program to check if a tuple is a palindrome.
tuple =(1,2,1,1,2,1)
tuple =(tuple[: : -1])
if tuple ==(tuple[: : -1]):
    print("palindrome")
else:
    print("not palindrome")

#39. Write a program to find the element with maximum frequency in a tuple.       
tuple =(53,70,63,70,49,15,70,83,83,65,70,56,90,65)
t2=[]
maxx= 0
num = 0
for i in tuple:
    if i not in t2:
        t2.append(i)
        if tuple.count(i)>maxx:
            maxx=tuple.count(i)
            num = i
print("element",num,"frequency",maxx)

#40. Write a program to create a nested tuple and access its elements.
t = (56,48,34,(56,84,39),57,12,(67,29,60),8,94)
flat =[]
for i in t:
    if isinstance(i,tuple):
        flat.extend(i)
    else:
        flat.append(i)
print(flat)
"""   
