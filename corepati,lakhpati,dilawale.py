# Write a program that tells in the above list that how many people are there in the above list who are :

# 1 - `Crorepati`
# 2 - `Lakhpati`
# 3 - `Dilwale`
# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]


money=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
count=0
count1=0
count2=0
i=0
while i<len(money):
    if money[i]>=10000000:
        count+=1
        i+=1
        # print(count,":","cropati")
    elif money[i]>=100000 and money[i]<10000000:
        count1+=1
        i+=1
        # print(count1,":","Lakhpati")
    # elif money[i]<100000:
        # count2+=1
        # print(count2,":","Dilwale")
    else:
        count2+=1
        # print()
        i+=1
print(count,":","cropati")
print(count1,":","Lakhpati")
print(count2,":","Dilwale")
    # i+=1



