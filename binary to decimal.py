# # binary to decima

# bin=list(input("Enter the binary number :"))
# value=0
# for i in range(len(b_num)):
#     digit=b_num.pop()
#     if digit=="1":
#         value= value+(i**2)
#         print(value)
    
# binary=[1,0,0,1,1,0,1,1]

# sum=0
# i=0
# while i<len(binary):
#     a=binary[-i-1]*(2**i)
#     sum=sum+a
#     i=i+1
# print(sum)

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 34

convertToBinary(dec)
print()

