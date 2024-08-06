
# def fact(n):
#     fact=1
#     i=0
#     while i<=n:
#         print(fact*i)
#         i+=1
#         print(fact)

#     fact(5)

def fact(n):
    fact=1
    for i in range(1,n+1):
         fact *= i
         print(fact)
    
    fact(5)
    

    

    
    