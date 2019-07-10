a=input()
c=[]
for i in a:
    c.append(i)
d=[]
for i in c:
    n=0
    for j in c:
        if(j==i):
            n=n+1
    d.append(n)        
print(max(d))   
