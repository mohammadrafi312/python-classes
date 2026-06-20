# #function without parameter and without return type
# def hello():#def is a keyword to define a function
#     print("Hello World")

# hello()#calling function
# #function with parameters
# def sum(a,b):
#     c=a+b
#     print(c)

# sum(10,20)
# #function with return type
# def sum(a,b):
#     c=a+b
#     return c #return sum but not print sum
#print elements of list using function
list1=[1,2,3,4,5,6,7,8]
def print_list(list):
    print(list)
print_list(list1)
#factoprial of a number using function

def factor(n):
    fact =1
    i=1
    while i<=n:
        fact=fact*i
        i+=1
    print(fact)
factor(6)

