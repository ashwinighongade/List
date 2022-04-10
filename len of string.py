list=['python','jyoti','mahi','krina','ashwini']
i=0
max=0
while i<len(list):
    b=list[i]
    if len(b)>max:
        max=len(b)
    i=i+1
    print(len(b))
print(b,max)
    