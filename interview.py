# list=[6, 5, 4, 3, 2, 1]
# i=0
# while i<len(list):
#     print(i,list[i])
#     i+=1
    
# list.remove("a")
# print(list)

# list.reverse()
# print(list)

# list.append(20)
# print(list)

# list.insert(4, 9)
# print(list)

# list.sort()
# print(list)

# list.pop()
# print(list)

# list1=list[:3]
# print(list1)

# list1=[1,2,[3,7],[8,9,10],[4,6]]
# b=[]
# i=0
# while i<len(list):
#     j=0
# for i in list:
#     if type (i)==list:  
#         for j in i:
#             if j==4:
#                 b.append(j)
# print(b)

# print(list1[4][0])

# list=[4,5,6,7]
# sum=0
# i=0
# while i<len(list):
#     sum=sum+list[i]
#     i+=1
# print(sum)
    
# list=["ran","rani", "madhu"]
# for i in list:
#     print(i)
    
# list=["ram","shyam","rani"]
# list1=[1,2,3]
# list2=[]
# i=0
# while i<len(list):
#     a=list+list1
#     i+=1
# list2.append(a)
    
# print(list2)
    
# list=["ram","shyam","rani"]
# list1=["we","u","know"]
# b=[]
# i=0
# k=0
# while i<len(list):
#     j=0
#     while j<len(list1):
#         b.append(list[k],list1[j])
#         j+=1
#         k+=1
#     i+=1
# print(b)

# k=0   
# for i in list:
#     for x in list1:
#         k+=1
#         print(list[k],x)
# # b=[]
# # list1=[1,2,3]  
# for i in list:
#     for j in range(3):
#         b.append(i+str(j))
# print(b)
list1=["ram","shyam","rani"]
list2=["we","u","know"]
b=[]
i=0
k=0
while i<len(list1):
    j=0
    while j<len(list2):
        a=list1[k],list1[i]
        j+=1
        k+=1
    b.append(a)
    # k+=1
    i+=1
print(b)
#     while j<len(list):
#         x=0
#         while x<len(list1):
#             m=0
#             while m<len(list1):
#                 b.append(list[j],list[m])
#                 m+=1
#         x+=1
#         j+=1
#     i+=1
# print(b)
        
          