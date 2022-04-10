# Write a Python program to convert a list of characters into a string. 

list1=['python','java','convert']
list2=[]
for i in list1:
    a=list(i)
    print(a)
    a="".join(a)
    list2.append(a)
print(list2)

