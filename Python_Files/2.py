arr1=[]
arr2=[]
b=0
c=0
for i in range(4):
    a=input()
    arr1.append(a)
    #print(arr1[i])
for i in range(4):
    a=input()
    arr2.append(a)
    #print(arr2[i])
for i in range(4):
    if arr1[i]>arr2[i]:
     b+=1
    elif arr1[i]<arr2[i]:
     c+=1
    else:
     c=0
     b=0
print(b)
print(c)    
