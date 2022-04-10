a = [[78, 76, 94, 86, 88,],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
sum=0
i=0
while i<len(a):
    if type(a[i])==list:
        for j in a[i]:
            sum=sum+j
            avg=sum/len(a[i])
    i=i+1
    print("sum",sum,"avg",avg)
    
# for i in a:
#     # if type(a[i])==list:
#         for j in i:
#             sum=sum+j
#             avg=sum/5
#         print("sum",sum,"avg",avg)

# find the length


# i=0
# while i<len(a):
#     # print(len(a[i]))
#     i+=1
# print(len(a[i]))

# for i in a:
#     print(len(a[i]))