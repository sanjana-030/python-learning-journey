Python Programming Questions
(Functions, lambda, map, filter, reduce)

A. Questions on def (Functions)
Basic

1. Write a function to add two numbers.
def add(a,b):
    return a+b
print(add(46,75))

2. Write a function to find square of a number.
def sq(a):
    return a*a
print(sq(8))

3. Write a function to check even or odd.
def even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(even(13))

4. Write a function to find maximum of two numbers.
def maxx(a,b):
    return max(a,b)
print(maxx(96,72))

5. Write a function to count vowels in a string.
def vowel(st):
    vowels = "aioue"
    count=0
    for i in vowels:
        if i in st:
            count +=1
    return count
print(vowel("rahul gandhi is next prime minister f india"))

Medium

6. Write a function to check palindrome string.
def palindrome(st):
    st1 = st[::-1]
    if st==st1:
        return "palindrome"
    else:
        return "not palindrome"
print(palindrome("sanjana"))

7. Write a function to find factorial of a number.
def fact(num):
    ft = 1
    for i in range(1,num+1):
        ft = ft*i
    return ft
print(fact(21))

8. Write a function to return second largest number from a list.    
def largest(li):
    li.sort()
    second largest =li[-2]
    return second largest
print(largest([65,39,52,98,63,84]))

9. Write a function to remove duplicates from a list
def uniqe(li):
    s1= set(li)
    return s1
print(uniqe([76,48,1,2,1,84,48]))

10. Write a function to calculate Fibonacci series.
def fibonacci(num):
    a = 0
    b = 1
    d = [0]
    while a<num:
        c = a+b
        a = b
        b = c
        d.append(a)
    return d
print(fibonacci(10))

Advanced

11. Write a recursive function for factorial.
def fact(num):
    if num==1:
        return 1
    else:
        return num* fact(num-1)

print(fact(5))
12. Write a function to check prime number
def prime(num):
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                return False
        return True
    else:
        return False
print(prime(1))

13. Write a function to find GCD of two numbers.
def GCD(n1,n2):
    gcd = 1
    for i in range(1,n1+1):
        if n1%i==0 and n2%i==0:
            gcd = i
    return gcd
print(GCD(3,92))
    
14. Write a function to count frequency of characters in a string.
def fr(st):
    ch = []
    for i in set(st):
        ch.append((i,st.count(i)))
    return ch       
print(fr("rahul gandhi is next prime minister of india"))

15. Write a function that accepts any number of arguments and returns sum.
def total(*a):
    return sum(a)
print(total(1,3,45,65,2))

B. Questions on lambda
1. Write a lambda function to add two numbers
add = lambda a,b:a+b
print(add(4,8))

2. Write a lambda function to check even number.
checkeven = lambda num: "Even" if num%2==0 else "odd"
print(checkeven(78))

3. Write a lambda function to find maximum of two numbers.
maxx = lambda a,b: max(a,b)
print(maxx(75,88))

4. Write a lambda to return square of a number
sq = lambda num : num**2
print(sq(2))

5. Write a lambda to return "Pass" if marks > 40 else "Fail".
result = lambda num : "pass" if num>40 else "fail"
print(result(23))

##C. Questions on map()

1. Use map() to square all elements in a list.
list = [32,73,64,12,3,43,12,93]
sq = tuple(map(lambda num:num**2,list))
print(sq)

2. Use map() to convert list of strings into uppercase.
list = ["aman"]
caps = tuple(map(lambda st:st.upper(),list))
print(caps)

3. Use map() to convert list of strings into integers.
li =["243478956"]
intt = tuple(map(int,li))
print(intt)

4. Use map() to add elements of two lists.
li = [36,12,24,35]
li2 = [72,73,53,87,36]
li3 = tuple(map(lambda a,b: a+b,li,li2))
print(li3)

5. Use map() to find length of each word in a list.
li ="my name is sanjana"
li2 = li.split()
length = tuple(map(lambda st:len(st),li2))
print(length)

##D. Questions on filter()

1. Use filter() to get even numbers from a list.
list = [ 1,2,3,5,22]
checkeven = tuple(filter(lambda num:True if num%2==0 else False,list))
print(checkeven)

2. Use filter() to get odd numbers from a list.
li = [24,46,75,23]
checkodd = tuple(filter(lambda num:True if num%2==1 else False,li))
print(checkodd)

3. Use filter() to get numbers greater than 50.
numbers = [53,35,27,39]
check = tuple(filter(lambda num:True if num>50 else False,numbers))
print(check)

4. Use filter() to get words starting with vowel.
s1 = "indian currency is an worst currency"
s2 = s1.split()
vowel = tuple(filter(lambda st:True if st.startswith(('a','e','o','u','i'))else False,s2))
print(vowel)

5. Use filter() to get prime numbers from a list
list =[2,385,4,5,67,7]
def prime(num):
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                return False
        return True
    else:
        return False
checkprime = tuple(filter(prime,list))
print(checkprime)

5. Questions on reduce()
(Use: from functools import reduce)

1. Use reduce() to find sum of elements in a list.
from functools import reduce
li = [63,92,41,42,21]
total = reduce(lambda *num:sum(num),li)
print(total)

2. Use reduce() to find product of elements in a list.
list = [53,28,52,10,89]
product = reduce(lambda a,b: a*b,list)
print(product)

3. Use reduce() to find maximum element in a list
list = [53,28,52,10,89]
maxx = reduce(lambda *num: max(num),list)
print(maxx)

4. Use reduce() to concatenate a list of strings.
st = "aman"
st2 = "kumar"
con = reduce(lambda a,b:a+b,st2,st)
print(con)

5. Use reduce() to flatten a list of lists.
def flatten(li2,i):
    li2 =[]
    for i in li:
        if isinstance(i,list):
            li2.extend(i)
        else:
            li2.append(i)
    return li2
from functools import reduce
li = [1,2,3,4,[5,6,7],8,9,10]
flat = reduce(flatten,li,[])
print(flat)

##6. Mixed Practice Questions

1. Use map() and lambda to square all numbers in a list           
list= [1,3,4,5,6,2]
sq = tuple(map(lambda num:num**2,list))
print(sq)

2. Use filter() and lambda to get numbers greater than 10.
list= [11,3,4,15,6,2]
greater = tuple(filter(lambda num:True if num>10 else False,list))
print(greater)

3. Use map() and filter() to square only even numbers.
li = [11,3,4,15,6,2]
print(tuple(map(lambda num:num**2,filter(lambda i:True if i%2==0 else False,li))))

4. Use reduce() to find factorial of a number.
from functools import reduce
num = int(input("enter a number:"))
fact = reduce(lambda n1,n2:n1*n2,range(1,num+1),1)
print(fact)

5. From a list, remove duplicates and return only even numbers.
list = [1,34,21,56,12,34,21,1,65]
li = set(list)
even = tuple(filter(lambda num:True if num%2==0 else False,li))
print(even)


Interview Basics (Write Answers for these Questions)
1. Difference between def and lambda.
2. Difference between map() and filter().
3. Difference between filter() and list comprehension.
4. Why reduce() is not a built-in function in Python?
5. Can lambda have multiple statements?
