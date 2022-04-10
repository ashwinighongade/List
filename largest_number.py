# Write a Python program to get the largest number from a list.
list=[23,12,43,28,45,67]
max=0
i=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    i+=1
print(max)


