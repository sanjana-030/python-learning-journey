#String Programming Questions
#Basic
"""
1. Write a program to count the number of vowels in a string.
st = "aioue"
print(len(st))

2. Reverse a string without using built-in functions.
st = "hello"
print(st[: : -1])

3. Check whether a string is a palindrome.
st = "say"
print(st[: : -1])
if st==st[: : -1]:
    print("palindrome")
else:
    print("not palindrome")
    
4. Count uppercase and lowercase letters in a string.
st = "SATuRday"
upper = 0
lower = 0
for i in st:
    if i.isupper():
        upper +=1
    else:
        if i.islower():
            lower +=1
print("upper:",upper ,"lower:",lower)

5. Replace all spaces in a string with _.
st = "i did not mean that"
print(st.replace(" " ,"_"))

Intermediate
6. Find the frequency of each character in a string.
st = "indiaaa"
for i in set(st):
    print(st.count(i),i)
    
7. Remove duplicate characters from a string
st = "helloworld"
for i in set(st):
        print(i)

8. Find the first non-repeating character in a string.
st = "hhello"
for i in st:
    if st.count(i)==1:
        print("non-repeating",i)
        break

9. Check if two strings are anagrams.        
10. Convert "hello world" → "Hello World" (title case without using .title()).
st = "hello world"
print(st.replace("hello world","Hello World"))

##Tricky
11. Find the longest word in a sentence.
sen ="rahul gandhi is next prime minister"
st1 = sen.split()
longest =""
for i in st1:
    if len(i)>len(longest):
        longest=i
print(longest)
st2 =st.split("613932")
print("words_count:",len(st2))

12. Compress a string like "aaabbc" → "a3b2c1".
13. Count words, characters, and digits in a string.        
st ="indiaa 613932 world"
st2 =st.split("613932")
print(len(st2))
print(len(st))

14. Rotate a string left by n positions.
15. Find all substrings of a given string.

#Set Programming Questions
##Basic
1. Create a set and add elements dynamically.
values = [1, 2, 3]
sett = set()
for i in values:
    sett.add(i)
print(sett)

2. Find the union and intersection of two sets.
set1 ={53,78,21,58,32,65}
set2 ={67,95,53,57,97,32}
print(set1|set2)
print(set1&set2)

3. Remove duplicate elements from a list using a set.
list =[53,43,82,56,43,82]
print(set(list))

4. Check if an element exists in a set.
set ={26,43,56,86,12}
el =12
if el in set:
    print(el)
else:
    print("not found")
5. Find the difference between two sets.
a ={53,78,21,58,32,65}
b ={67,95,53,57,97,32}
print(a-b)

Intermediate
6. Find common elements in two lists using sets
a =[53,78,21,58,32,65]
b =[67,95,53,57,97,32]
s1 = set(a)
s2 = set(b)
s3 = s1 & s2
print(s3)

7. Check whether one set is a subset of another.
8. Find symmetric difference of two sets
a ={53,78,21,58,32,65}
b ={67,95,53,57,97,32}
print(a^b)

9. Count unique elements in a list using a set.
list =[24,54,42,68,34,24,42]
print(len((set(list))))

10. Remove all common elements from two sets.
a ={53,78,21,58,32,65}
b ={67,95,53,65,97,32}
print(a^b)

#Tricky
11. Find missing numbers from 1 to n using sets.
12. Check if two lists have any common elements.
li =[7,9,11,4,]
li2 =[3,6,5,1,2]
for i in li:
    if i in li2:
        print("yes")
        break
else:
     print("no")

13. Convert a set of strings into uppercase.
st = {"sanjana"}
s = str(st)
print(s.upper())

14. Identify unique vowels in a given string using a set.
15. Find elements that appear only once in a list.
list =[12,43,45,12,33,45,43]
for i in list:
    if list.count(i)==1:
        print(i)
        
#Dictionary Programming Questions
#Basic
1. Create a dictionary and print all keys and values.
dic = {1:24,2:45,3:86,4:75,5:32,6:97}
print(dic.items())

2. Count frequency of each word in a sentence.
3. Merge two dictionaries.
dic = {1:24,2:45,3:86,4:75}
d2 = {5:32,6:97}
dic.update(d2)
print(dic)

4. Find the length of a dictionary.
dic = {1:24,2:45,3:86,4:75,5:32,6:97}
print(len(dic))

5. Check if a key exists in a dictionary.
dic = {1:24,2:45,3:86,4:75,5:32,6:97}
print(dic.get(4,"not found"))

Intermediate
6. Sort a dictionary by values.
dic = {1:24,2:45,3:86,4:75,5:32,6:97}
li =list(dic.values())
li.sort()
print(li)

#7. Find the key with the maximum value.
dic = {1:24,2:45,3:86,4:75,5:32,6:97}
print(max(dic.items()))

#8. Remove a key from a dictionary.
dic = {1:24,2:45,3:86,4:75,5:32,6:97}
dic.pop(5)
print(dic)

9. Convert two lists into a dictionary.
10. Count character frequency using a dictionary.

Tricky
11. Invert a dictionary (swap keys and values).
12. Group elements by frequency using a dictionary.
13. Find duplicate values in a dictionary.
dic = {1:24,2:45,3:86,4:75,5:32,6:97,7:24}
li = list(dic.values())
for i in li:
    if li.count(i)>=2:
         print("dt_value:",i)
     
14. Create a nested dictionary for student records.
dic = {1:24,2:45,3:86,4:{5:32,6:97},7:24}
flat=[]
for i in dic:
    if isinstance(dic[i],dict):
        flat.extend(dic[i].items())
    else:
        flat.append(dic[i])
print(flat)

15. Flatten a nested dictionary.
dic = {1:24,2:45,3:86,4:{5:32,6:97},7:24}   
flat ={}
for i in dic:
    if isinstance(dic[i],dict):
        flat.update(dic[i])
    else:
        flat[i]=dic[i]
print(flat)

##Mixed (String + Set + Dictionary)
1. Count unique words in a sentence.
str1="helloindia is helloindia"
s1 = str1.split()
s2 = set(s1)
print(len(s2))

2. Find common characters between two strings.
str1="helloindia"
str2= "helloworld"
s1=set(str1)
s2=set(str2)
s3=s1 & s2
print(s3)

3. Find the most frequent character in a string.
str1 ="i am an indiaan"
fr = 0
ch = ""
for i in str1:
    if str1.count(i)>fr:
        fr =str1.count(i)
        ch = i
print(fr,ch)
    
4. Remove duplicate words from a sentence.
sen ="rahulgandhi"
s1 = set(sen)
print(s1)

5. Find words with the same letters (anagram groups).
"""
