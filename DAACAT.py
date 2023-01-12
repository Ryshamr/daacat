import numpy as np
num=0
e=0
f=0
a=['A','G','C','T','A','B','B','C','A']
b=['A','C','T','A','G','C','T','A','B']
arr = np.zeros([10, 10], dtype = int) 

def fill(arr,j,num):
#     print(j)
    for i in range(len(a)):
#         print(i)
        if(a[i]==b[j]):
            max=arr[i][j]
            if(max+5>num): 
                num=5+max
                c=i+1
                d=j+1
            arr[i+1][j+1]=max+5
        elif(a[i]!=b[j]):
            max=arr[i][j];
            if(arr[i][j+1]>max): 
                max=arr[i][j+1]
            if(arr[i+1][j]>max): 
                max=arr[i+1][j]
            if(max-1>num):
                num=max-4
                c=i+1
                d=j+1
            arr[i+1][j+1]=max-4
    if(j==len(a)-1):
        return c,d
    else:
        j+=1
        return fill(arr,j,num)
    
j=0
e,f=fill(arr,j,num)
print(arr)

