# Wap the python program to add the two num.
a = 4
b = 6
print(a+b)
# user input
a = float(input("enter the num"))
b = float(input("enter the num"))
sum = a+b
print("the sum is",sum)

# wap a program to print the hello world
print("hello world")
str = "hello world"
print(str)

# wap a program to calculate the sr root of the given num
num = 64
ans = num**(1/2)
print("the sq root of the num is",ans)

# By using math Module
import math
num = 81
ans = math.sqrt(num)
print("the sq root of the num is",ans)

# Wap a program to calculate the area of the triangle 
b = 3
h = 2
area = (b*h)/2
print(area)

# Wap a program to swap the two values
x =4
y =3
print("before swapping")
print(x,y)
print("after swapping")
x = x+y
y = x-y
x = x-y
print(x,y)

# Wap the program to convert the kilometer into miles
# 1km = 0.621371
km = 10
miles = km*0.621371
print(miles)

# Wap a program to check the num is pos, neg and zero
num = int(input("enter the value"))
if num>0:
    print("num is positive")
elif num ==0:
    print("num is zero")
else:
    print("negative")    

# Wap a programe to check the number is even or odd

num1 = int(input("enter the number"))
if num1%2==0:
    print("even")
else:
    print("Odd") 

# Wap a program to check the largest among three number
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))
if num1>num2 and num1>num3:
    print(num1,"is the largest")
elif num2>num1 and num2>num3:
    print(num2,"is the largest")
else:
    print("num3 is the largest")    
      