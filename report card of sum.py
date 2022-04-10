# These are the marks of any student for the last three years. You have to calculate total marks for all the three years.

marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# sum=0
# i=marks0
# while i<len(marks[0]):
#     sum=sum+marks[i]
#     j=0
#     while j<len(mark[1]):
#         sum
sum=0
for i in marks:
    for j in i:
        sum=sum+j
        print(sum)
    
    