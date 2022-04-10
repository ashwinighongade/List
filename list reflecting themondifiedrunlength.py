# Write a Python program to create a list reflecting the modified run-length encoding from 
# a given list of integers or a given list of characters. 
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# b=aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# # [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

b=[1, 1, 2, 3, 4, 4, 5, 1]
a=[]
i=0
while i<len(b):
    j=0
    count=0
    d=[]
    while j<len(b):
        # if b[i] in b:
        if b[i]==b[j]:
            count+=1
        j+=1
    d.append(b[i])
    d.append(count)
    print(d)
    if d not in a:
        a.append(d)
    i+=1
print(a)



# word="aaabbbcccccsafffg"
# ch=word[0]
# # a=""
# a=[]
# count=0
# # word=word+""
# for x in word:
#     # print(x)
#     if x==ch:
#        count+=1
#     else:
#         # a=a+str(count)+str(ch)
#         a.append([count,ch])
#         ch=x
#         count=1
# print(a)

        
                
