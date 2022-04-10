# given two array


list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
x=len(list1)
y=len(list2)
for i in range(x):
    for j in range(y):
        if list1[i]==list2[j]:
            break
    if j==y-1:
        print(list1[i])