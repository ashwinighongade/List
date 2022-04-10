# Write a Python program to print the numbers of a specified list after removing even numbers from it.
list=[12,33,11,45,9,7,6,42,28,34]
i=0
b=[]
while i<len(list):
    if list[i]%2==0:
        b.append(list[i])
    i+=1
print(b)
        
        