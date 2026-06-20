# #multiplication table using for loop
# n=int(input("Enter a number: "))
# for i in range (1, 11):
#     print(i,"x",n,"=",i*n)


#multiplication table using while loop
# n=int(input("Enter a number: "))
#print even numbers from 0 to 20 using while loop

#factorial of a number using while loop
# n=int(input("enter :"))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1

# print(fact) 
# #
fruits = ["Apple", "Banana", "Mango"]

#without using enumerate
index=0
for  fruit in (fruits):
    print(index, fruit)
    index += 1
    #with using enumerate
for index, fruit in enumerate(fruits):
    print(index, fruit)