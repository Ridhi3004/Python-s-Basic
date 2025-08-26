# Looping
for i in range(1,1001):
    print("Numbers:",i)

Fruits=["Apple","Mango","Cherry","Melon"]
for x in Fruits:
    print("I Like:",x)


#WHILE LOOP
i=1
while i <=5:
    print("Number:",i)
    i+=1

#FOR LOOP (Printing first 10 natural numbers)
for i in range(1,11):
    print(i)
print("-----------")


#WHILE LOOP
i=1
while i<=10:
    print(i)
    i+=1
print("-----------")


#TABLE OF 5
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
print("-----------")


i=1
while i<=10:
        print(f"5 x {i} = {5*i}")
        i+=1
print("-----------")

#Print numbers from 1 to 100
for i in range(1,101):
    print("Numbers:",i)
print("-----------")

i=1
while i<=100:
     print(i)
     i+=1
print("-----------")

# The square of numbers from 1 to 10.
for i in range(1,11):
     print(f"{i}- {i*i}")

i=1
while i<=10:
     print(f"{i}-{i*i}")
     i+=1
print("-----------")

# Find the factorial of a number using for loop
num=int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
     fact=fact*i
print("Factorial of num is:",fact)
print("-----------")



# Print the Fibonacci series up to n terms.
num=int(input("Enter number of terms:"))
a,b=0,1
print("Fibonacci Series")
for i in range (num):
    print(a)
    a,b=b,a+b
print("-----------")



# Print the sum of the first n natural numbers.
num=int(input("Enter number of terms:"))
s=0
for x in range(1,num+1):
    s+=x
print(s)
print("-----------")



