list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
b=[]
i=0
while i<len(list):
    b.append(list[i])
    i+=3
    j=1
    c=[]
    while j<len(list):
        c.append(list[j])
        j+=3
        d=[]
        k=2
        while k<len(list):
            d.append(list[k])
            k+=3
print([b,c,d])
            
        
