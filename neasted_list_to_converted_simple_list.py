# a=[[1,2],[4,5,6],[7,8,9]]
# i=0
# b=[]
# # c=a[i]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)

# a=[[1,2],[4,5,6],[7,8,9]]
# b=[]
# for i in a:
#     for j in i:
#         b.append(j)
# print(b)

a=[1,2,[4,5,6],[7,8,9]]
b=[]
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
print(b)
        
    