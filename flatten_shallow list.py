list1=[[2,4,3],[1,5,6], [9], [7,9,0]]
# i=0
# b=[]
# while i<len(list1):
#     j=0
#     # a=list[i]
#     while j<len(list1[i]):
#         b.append(list1[i][j])
#         j+=1
#     i+=1
# print(b)

b=[]
for i in list1:
    for j in i:
        b.append(j)
print(b)
