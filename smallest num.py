# Write a Python program to get the smallest number from a list.
list=[23,12,43,28,45,67]
min=list[0]
i=0
while i<len(list):
    if list[i]<min:
        min=list[i]
    i+=1
print(min)