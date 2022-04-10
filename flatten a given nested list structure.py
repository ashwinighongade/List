# Write a Python program to flatten a given nested list structure. Go to the editor
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
list=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
new=[]
for i in list:
    if type(i)==int:
        new.append(i)
    
    else:
        # l=len[i]
        if i!=1:
            for j in i:
                new.append(j)
print(new)
