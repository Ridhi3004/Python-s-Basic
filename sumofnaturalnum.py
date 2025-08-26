# Print the sum of the first n natural numbers.
num=int(input("Enter number of terms:"))
s=0
for x in range(1,num+1):
    s+=x
print(s)