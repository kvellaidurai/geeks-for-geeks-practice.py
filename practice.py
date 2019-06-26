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
        
    
reverse a number without using modulo

#include<stdio.h>
#include<math.h>
int main(){
    int n,p=0,s;
    int pow=1;
    scanf("%d",&n);
    while(n>=pow){
        s=(n/pow)%10;
        p=p*10+s;
        n=n/10;
    }
    printf("%d",p);
}


remove the duplicates except space

s=input()
l=[]
m=[]
for i in s:
    l.append(i)
for j in l:
    if(j not in m and j!=" "):
        m.append(j)
    if(j==" "):
        m.append(j)
print(*m)


replace the digit with another digit without using string,lists,arrays

a=int(input())
r=int(input())
d=int(input())
p=1
v=0
while(a>=p):
    s=(a//p)%10
    if(s==r):
        s=d
    v=s*p+v
    p*=10
print(a,v)


swap alternate elements

a=int(input())
p=1
while(a>=p):
    s=(a//p)%100
    a=a-(s)*p+(((s%10)*10)+s//10)*p
    p*=100
print(a)



array[array[i]] program


a=list(map(int,input().split()))
for i in range(0,len(a)):
    a[i]=(a[a[i]]%len(a))*len(a)+a[i]
    print(a[i],end=" ")
    
    
    or
    
    
#include<stdio.h>
int main(){
    int n,a[100];
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(int i=0;i<n;i++)
        a[i]=(a[a[i]]%n)*n+a[i];
    for(int i=0;i<n;i++)
        printf("%d",a[i]/n);
    return 0;
}
