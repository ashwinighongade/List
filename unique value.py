list=[11,12,13,14,15,16,17,18,19,12,13,14,17,18]

new=[]
i=0
while i<len(list):
    if list[i] not in new:
        new.append(list[i])
    i+=1
print(new)