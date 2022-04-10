# Write a Python program to split a given list into specified sized chunks. 
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the said list into equal size 3
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 4
# [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 5
# [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]


# a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# b=[]
# i=0
# k=1
# j=2
# while i<len(a):
#     b.append([a[i],a[k],a[j]])
#     i+=3
#     k+=3
#     j+=3
# print(b)
    
a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29,83,88,96]
b=[]
i = 0
k = 0
while i < len(a):
    j = 0
    c = []
    while j < 4 and k != len(a):
        c.append(a[k])
        j+=1
        k+=1
    b.append(c)
    if k == len(a):
        break
    i+=1
print(b)
