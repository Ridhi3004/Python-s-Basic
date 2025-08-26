# Print the Fibonacci series up to n terms.
num=int(input("Enter number of terms:"))
a,b=0,1
print("Fibonacci Series")
for i in range (num):
    print(a)
    a,b=b,a+b