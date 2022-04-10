# reverseed the list

list=[1,2,3,4,5,6,7]
# b=[]
# i=0
# while i<len(list):
#     b.append(list[-1-i])
#     i+=1
# print(b)

b=[]
i=1
while i<len(list)+1:
    b.append(list[-i])
    i+=1
print(b)
