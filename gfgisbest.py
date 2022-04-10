# Convert Character Matrix to single String;
# The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest

list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        print(list[i][j],end="")
        j+=1
    i+=1

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20] 
# length = len(students) 
# counter = 0
# while counter < length:
#     print(students[counter] + str(marks[counter]))
#     counter+=1

