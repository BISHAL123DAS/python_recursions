
#1.--------------factorial program recursions--------
# def rec(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*rec(n-1)
    
# n=int(input("enter your value:"))
# ans=rec(n)
# print(ans)

#----fibonaci series programe-------

# def fibonaci(n):
#     n1=0
#     n3=0
#     n2=1
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n3=n1+n2
# print(fibonaci(5))


# n=int(input("enter your value:"))
# n1=n3=0
# n2=1
# print(n2)
# for i in range(2,n+1):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3


# def fibonaci(n):
#     n1=n3=0
#     n2=1
#     print(n2)
#     for i in range(2,n+1):
#         n3=n1+n2
#         print(n3)
#         n1=n2
#         n2=n3
# fibonaci(5)      

# def fibonaci(n):

#     if(n==0 or n==1):
#         return 1
#     else:
#         return (fibonaci(n-1)+fibonaci(n-2))

# n=int(input("vaalue:"))   
# for i in range(n):
#     print(fibonaci(i))    

# def fact(n):
#     n3=0
#     n1=0
#     n1=1
#     if( n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)


# n=int(input("enter your value:"))
# ans=fact(n)
# print(ans)

def power(n,t):
    if(t==0):
        return 0
    elif(t==1):
        return n
    else:
        return n*power(n,(t-1))

n=2
t=5
ans=power(n,t)
print(ans)    



        
