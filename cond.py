# Wap a program to find the largest among three num.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a>b and a>c :
    print("a is largest no")
elif b>a and b>c :
    print("b is largest no")
else:
    print("c is the largest")