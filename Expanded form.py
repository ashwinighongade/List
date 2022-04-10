# You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12  # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304  # Should return '70000 + 300 + 4'

num=input("enter the Number :")
i=0
add=" "
while i<len(num):
    add+=num[i]
    j=1
    while j<=len(num)-(i+1):
        add+="0"
        j+=1
    if i==(len(num)-1):
        break
    else:
        add+="+"
    i+=1
print(add)




# num=input("Enter the number :")
# x=list(num)
# print(x)

