# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

i=1
b=[]
while i<=30:
    b.append(i**2)
    i+=1
print(b[:5])
print(b[-5:])

# i=1
# b=[]
# while i<=30:
#     b.append(i**2)
#     i+=1
# print(b[1:25])
    