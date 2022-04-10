list=[2,1,3,8,5,7]
# i=0
# product=1
# while i<len(list):
#     product=product*list[i]
#     i+=1
# print(avg)

sum=0
count=0
i=0
while i<len(list):
    sum=sum+list[i]
    count+=1
    avg=sum/count
    i+=1
print(sum)
print(avg)
print(count)
