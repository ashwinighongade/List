# Write a Python program to find the list in a list of lists whose sum of elements is the highest. Go to the editor
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
list=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# max=0
# for q in list:
#     a=sum(q)
#     if a>max:
#         max=a
#         n=q
# print(n)

max=0
for q in list:
    # n=q
    sum=0
    for j in q:
        sum=sum+j
        if sum>max:
            max=sum
            n=q
print(n)
        