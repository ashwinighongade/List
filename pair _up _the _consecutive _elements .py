# Write a Python program to pair up the consecutive elements of a given list.
# Original lists:
# [1, 2, 3, 4, 5, 6]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# Original lists:
# [1, 2, 3, 4, 5]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5]]

list=[1, 2, 3, 4, 5, 6]
i=1
c=[]
s=0
while i<len(list):
    j=0
    k=2
    b=[]
    while j<k and s<=len(list):
        b.append(list[s])
        s+=1
        j+=1

    c.append(b)
    if s==len(list):
        break

    i+=1
print(c)

