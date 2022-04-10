# Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


a=['p', 'q']
# n=int(input("enter: "))
b=[]
for i in range(1,6):
    for j in a:
        b.append(j+str(i))
print(b)   

# list=[1,2,3,4] 
# var="emp"
# b=[]
# for i in list:
#     b.append(var+str(i))
# print(b)


# color = ['red', 'white', 'black']
# for i in num:
#     for x in color:
#         print(i,x)


    
    
        