a=[32,34,67,76,75,43,89,24]

b=[]
i = 0
k = 0
while i < len(a):
    j = 0
    c = []
    while j < 2 and k != len(a):
        c.append(a[k])
        j+=1
        k+=1
    b.append(c)
    if k == len(a):
        break
    i+=1
print(b)

