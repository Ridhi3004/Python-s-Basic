# # 1. Write a Python program to take an integer, float, and string input from the user and print them using f-string
# str=input("Enter a string")
# int=int(input("Enter a integer"))
# f=float(input("Enter a float"))
# print(f"{str} is str")
# print(f"{int} is integer")
# print(f"{f} is float")

# # 2. Write a program to check the type of variables: integer, float, string, list, tuple, dictionary.
# n=input("Enter a variable to check its type")
# print(type(n))

# # 3. Write a program that takes two numbers as input and prints their sum, difference, product, and division
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# sum=a+b
# difference=a-b
# product=a*b
# divison=a//b
# print(f"The sum is {sum} ")
# print(f"The difference is {difference} ")
# print(f"The product is {product} ")
# print(f"The divison is {divison} ")

# # 4. Write a program that converts Celsius to Fahrenheit
# Temp=int(input("Enter temperature in Celcius "))
# Fahrenheit= (Temp*5/9)+32
# print(f"Temperature in Farnehit is {Fahrenheit}")

# #5 Write a program that takes your name and age as input and prints: 'My name is X and I am Y years old.
# def hello(x,y):
#     print(f"My name is {x} and I am {y} years old")
# hello("Ridhi",18)

# 6. Write a program to swap two variables using input from the user
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# print(f"a before swap {a} and b before swap {b}")
# print(f"a after swap {b} and b after swap {a}")

#7. write a program to check whether a variable is mutable or immutable in pyhton 
# #y = 10
# #print('before',y)
# #y = 86
# #print('after',y) # variable can be mutable

# #y = 43
# #x = 61
# #z = y+x
# #print('the sum is',z) # variable can't be immutable


# 8. Write a program to perform all arithmetic operations on two numbers.
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# sum=a+b
# difference=a-b
# product=a*b
# divison=a/b
# floordivison=a//b
# exponentiation=a**b
# modulus=a%b
# print(f"The sum is {sum} ")
# print(f"The difference is {difference} ")
# print(f"The product is {product} ")
# print(f"The divison is {divison} ")
# print(f"The floordivison is {floordivison} ")
# print(f"The exponentiation is {exponentiation} ")
# print(f"The modulus is {modulus} ")

# 9. Write a program to check whether two numbers are equal using comparison operators.
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# if a==b:
#     print(f"{a} is equal to {b}")
# else:
#      print(f"{a} is not equal to {b}")


# #  11. Write a program to check whether a number lies between 10 and 50 using logical operators.
# n=int(input("Enter a number"))
# if n >= 10 and n <= 50:
#     print(f"{n} lies between 10 and 50.")
# else:
#     print(f"{n} does not lie between 10 and 50.")

# # 12. Write a program to check membership of an element in a list using 'in' and 'not in'.
# list = [5, 10, 15, 20, 25]
# a = int(input("Enter the element to check: "))
# if a in list:
#     print(f"{a} is present in the list.")
# else:
#     print(f"{a} is not present in the list.")
# if a not in list:
#     print(f"{a} is not in the list.")
# else:
#     print(f"{a} is in the list.")


# 13. Write a program to compare two objects using 'is' and 'is not'.
# s using 'is' and 'is not'
# s = [6,9,11]
# m = s         
# n = [6,9,11]  

# print(s is m)      
# print(s is n)      
# print(s is not n) 


#  14. Write a program to check whether a number is positive, negative, or zero.
# n=int(input("Enter a number"))
# if n < 0:
#     print(f"{n} is negative")
# elif n > 0:
#     print(f"{n} is Positive")
# elif n==0:
#     print(f"{n} is Zero")
# else:
#     print("Invalid")


#15. #even odd number
# num = int(input('Enter a number :'))
# if num % 2 == 0:
#     print('the number is even')
# elif num  % 2 != 0:
#     print('the number is odd ')
# else:
#     print('not exist!')

#16.largest of three numbers using nested if-else
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#c = int(input("Enter third number: "))

#if a >= b:
    #print("Largest is:", a)
    #print("Largest is:", c)
#if b >= c:
        #else:
        #print("Largest is:", c)

# #17. write a program to print all numbers from 1 to 20 using loop
# #for i in range(1,21):
#     #print("Numbers :", i)



#18. Multiplicatiob table using while loop
#num = int(input("Enter a number: "))
#i = 1
#print(num, "x", i, "=", num * i)
    #i += 1

# # 19. Write a program to search an element in a list using for-else.
# num = [10, 20, 30, 40, 50]
# i = int(input("Enter the element to search: "))
# for num in num:
#     if num == i:
#         print(f"Element {i} found in the list.")
#         break
# else:
#     print(f"Element {i} not found in the list.")
    


#20. prime numbers using while-else 
#num = int(input("Enter a number: "))
#if num > 1:
    #i = 2
    #while i < num:
        #if num % i == 0:
            #print(num, "is not prime")
            #break
       #i += 1
    #else:
        #print(num, "is prime")
#else:
    #print(num, "is not prime")

# #21. Print numbers from 1 to 10 but skip 5 using continue
# #for i in range(1, 11):
#     #if i == 5:
#         #continue
#     #print(i)

#  22. Write a program that prints numbers from 1 to 10 but stops when it reaches 7 using break.
# for i in range(1,11):
#     if i==7:
#         i+=1
#     else:
#         print(i)
# print("_")
# for n in range(1,11):
#     while n==7:
#         break
#     else:
#         print(n)


# # 23. Write a program that prints 'Hello' five times but does nothing when the loop counter is 3 (use
# for i in range(1,6):
#     if i==3:
#         pass
#     else:
#         print(f"{i}-Hello")


#24.Write a program to create an iterator for a list and print all elements using next() 

# #my_list = [1, 2, 3, 4, 5]
# #my_iter = iter(my_list)
# #print(next(my_iter))  
# #print(next(my_iter))  
# #print(next(my_iter))  
# #print(next(my_iter))  
# #print(next(my_iter))  

# 25. write a program to print square of numberes using loop 
# #for i in range(1,11):
#     #print(f"{i}-{i*i}")

