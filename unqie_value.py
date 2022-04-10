# Count unique values inside a list
n= [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.

new=[]
i=0
while i<len(n):
    if n[i] not in new:
        new.append(n[i])
    i+=1   
print(new)   

        
# m=[]
# for a in n:
#     if a not in m:
#         m.append(a)
# print(m)

# print(set(n))

# a = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# seen=set()
# unq=[]
# for x in a:
#     if x not in unq:
#         unq.append(x)
#         seen.add(x)
# print(unq)
# print(seen)
          
          
# b=[]
# i=0
# while i<len(a):
#     n=a[i]
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j] and i!=j:
#             c+=1
#         j+=1
#     if c==1:
#         if n not in b:
#             b.append(n)
#     i+=1
# print(b)
    
    
    