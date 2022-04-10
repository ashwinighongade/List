# Write a Python program to select the odd items of a list.
list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
b=[]
i=0
while i<len(list):
    if list[i]%2!=0:
        b.append(list[i])
    i+=1
print(b)