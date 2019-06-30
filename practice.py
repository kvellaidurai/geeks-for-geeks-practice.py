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


employee and manager

n=int(input())
emp=list(map(int,input().split()))
man=list(map(int,input().split()))
for i in range(n):
    for i in emp:
        if i not in man:
            print(i,"->not a manager")
        else:
            print(i,"->",end="")
            for j in range(len(man)):
                if(i==man[j] and emp[j]!=man[j]):
                    print(emp[j],"directly manages",end=" ")
            print()
	

find the occurence of an element(encode)

#include<stdio.h>
int main(){
    char str[1000];
    int count=0,i=0;
    scanf("%s",str);
    while(str[i]){
        count++;
        if(str[i]!=str[i+1]){
            printf("%d%c",count,str[i]);
            count=0;}
            i++;
        }
    }


fibonacci and prime sequence

#include<stdio.h>
int main(){
    int count=0,val=4;
    if(n==1)return 2;
    if(n==2)return 3;
    for(count=2;count<n;val++){
        if(val%2){
            int s=(int)sqrt(val);
            int flag=0;
            for(int fact=3;fact<=s;fact+=2)
            if(val%fact==0){
                flag=1;
                break;}
                if(flag==0) count++;}}
                return val-1;
}
int func1(int n){
    if(n<=2) return 1;
    return func1(n-1)+func2(n-2);
}
int main(){
    int num=0;
    scanf("%d",&num);
    printf("%d",num%2?func1((num+1)/2):func2(num/2);
    return 0;
}
            
	   
	   
	   
whos the closest
	   
	from itertools import permutations 
a=int(input())
b=int(input())
l1=[]
c=[int(d) for d in str(a)]
d=[int(d) for d in str(b)]
d2="".join(str(x) for x in d)
perm = permutations(c)
for i in list(perm):
    e=list(i)
    g="".join(str(x) for x in e)
    if(g>=d2):
        f=int(g)-int(d2)
        mini=10000000
        l=[]
        if(f<mini):
            mini=f
            l.append(g)
        l1.append(l)
if len(l1)>0:
    print(*l1[0])
else:
    print("-1")
            


print diamond like pattern with strings
	   
	   
#include <stdio.h>

int main() {
char str[100];
int i,len;
scanf("%s",str);
len=strlen(str);
for(i=0;i<len;i++)
printf("%-*.*s%*s\n",len,len-i,str,len,str+i);
for(i=0;i<len;i++)
printf("%-*.*s%*s\n",len,i+1,str,len,str+len-i-1);
	return 0;
}
