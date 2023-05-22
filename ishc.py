n=int(input())
h=0
while n!=0:
    h+=1
    A=[]
    for i in range(len(str(n))):
        A.append(int(str(n)[i]))
    n-=max(A)
print(h)
    