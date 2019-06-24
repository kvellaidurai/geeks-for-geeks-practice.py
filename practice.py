convert all the numbers in the list equal

a=list(map(int,input().split()))
count=0
while True:
    b=a.index(max(a))
    for i in range(len(a)):
        if(i!=b):
            a[i]+=1
    count+=1
    if(len(set(a))==1):
        print(count)
        break
        
       
bubble sort

a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print(*a)
        
    
