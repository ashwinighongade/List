A = [1,"f",2,"b",3,4,"h","j",6,9,0,"k"]
num=[]
char=[]
i=0
while i<len(A):
    if type(A[i])==int:
        num.append(A[i])
    else:
        char.append(A[i])
    i+=1
print(num)
print(char)

