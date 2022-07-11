# Find square root
# a=8
# b=a**2
# print(b)

#Swap Two Variable
# a=5
# b=10
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

#Random number
#a<=n<=b
# import random
# print(random.randint(10,19))

#Number is positive negative or 0
# num=int(input("Enter The Number : "))
# if num>0:
#     print(f"The Numer {num} is positive")
# elif num<0:
#     print(f"The Numer {num} is negative")   
# else:
#     print(f"The Numer {num} is zero")    

# Number is odd or even
num=int(input("Enter the number : ")) 
if num%2==0:
    print(f"The Number {num} is even")
else:
    print(f"The Numer {num} is odd")    

# num=[11,12,14,15]
# for i in num:
#     if i%2==0:
#         print(f"The Number {i} is even")
#     else:
#         print(f"The Numer {i} is odd")   

# num=int(input("Enter the numer : "))
# i=1
# while i<=num:
#     if i%2==0:
#         print(f"The Number {num} is even")    
#     else:
#         print(f"The Numer {num} is odd")   ......wrong prog

# Find out 1 to 10 odd number
# sum = 0
# for i in range(10):
#     if i % 2 == 0:
#         print(i)
#         sum = sum + i
# print(sum)

# Python Program to Calculate Sum of Even Numbers from 1 to N
 
# maximum = int(input(" Please Enter the Maximum Value : "))
# total = 0

# for number in range(1, maximum+1):
#     if(number % 2 == 0):
#         print("{0}".format(number))
#         total = total + number

# print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))

# a=10
# sum=0
# for i in range(a):
#     if i%2==0:
#         print(i)
#         sum=sum+i
# print(sum)
# a=[1,2,3,4,5]
# sum=0
# i=1
# while i<10:
#     if i%2==0:
#         print(i)

# num=[11,12,14,15]
# sum=0
# for i in num:
#     sum=sum+i
# print(sum)

#Greater Number among three
# a=50
# b=40
# c=30
# if a>b and a>c:
#     print(a,"is the greater number among three")
# elif b>a and b>c:
#     print(b,"is the greater number among three")
# else:
#     print(c,"is the greater number among three")  
# a=[10,20,30]
# max=a[0]
# for i in a:
#     if max<i:
#         max=i
# print(max)    

#Prime number or not  
# Python program to display all the prime numbers within an interval

# from re import I


# lower = 900
# upper = 1000

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
# lower=10
# upper = 20
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:        
#             print(num)
# a=[1,2,3,4,5,6,7,8,9,10]
# for num in a:
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)    

# a="Prashant Is Good"
# print(a.index("Goood"))

# a=[12,14,20,1,2,3,4,5,6,7,8,9,10]
# a.sort()
# print(a)
# print(a[::-1])
# a=[12,14,20,1,2,3,4,5,6,7,8,9,10,-1]
# b=a[0]
# for i in range(len(a)):
#     if 

# number = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34] 
 
# for i in range(len(number)): 
#     for j in range(i + 1, len(number)): 
 
#         if number[i] > number[j]: 
#            number[i], number[j] = number[j], number[i] 
 
# print (number) 

# number = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34] 
# for i in range (len(number)):
#     for j in range(i+1,len(number)):
#         if number[i]>number[j]:
#             number[i],number[j]=number[j],number[i]
# print(number) 
# number = 407 
# for i in intnumber:
#     if i>1:
#         for num in range(2,i):
#             if i%num==0:
#                 break
#         else:
#             print(i)   
# number = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34,-34]      
# min=number[0]  
# for i in range (len(number)):
#     if min>number[i]:
#         min=number[i]
# print(min)
# number = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34,-34]  
# for i in range (len(number)):
#     for j in range(i,len(number)):
#          if number[i]>number[j]:
#              number[i],number[j]=number[j],number[i]
# print(number)

# number = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34] 
# for i in number:
#     i>1
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# a=int(input("Enter the first number :"))
# b=int(input("Enter the second number :"))
# c=int(input("Enter the third number :"))
# d=int(input("Enter the fourth number :"))

# a=50
# b=40
# c=70
# d=60
# if a>b and a>c and a>d:
#     print(a,"is the greater number among three")
# elif b>a and b>c and b>d:
#     print(b,"is the greater number among three")
# elif c>a and c>b and b>d:
#     print(c,"is the greater number among three")    
# else:
#     print(d,"is the greater number among three") 

a=[12,14,20,1,2,3,4,5,6,7,8,9,10,-2]
# for i in a:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print("The",{i},"is Prime")
# min=a[0]
# for i in range(len(a)):
#     if min>a[i]:
#         min=a[i]
# print(min)    

