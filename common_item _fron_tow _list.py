# Write a Python program to find common items from two list.
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
color3=[]
for i in color1:
    if i in color2:
        # if i  not in color3:
            color3.append(i)
print(color3)            
