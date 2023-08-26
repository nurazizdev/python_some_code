n,m=map(int,input().split())
A=[]
p=0
for i in range(n):
	a=list(map(str,input().split(None,m)[:m]))
	A.append(a)
for i in range(n):
	for j in range(m):
		if a[i][j]=="N":
			h=0
			for k in range(i):
				if a[k][j]!=".":
					h+=1
			if h>0:
				p+=1
			a[i][j]=="."
		if a[i][j]=="W":
			h=0
			for k in range(j):
				if a[i][k]!=".":
					h+=1
			if h>0:
				p+=1
			a[i][j]=="."
		if a[i][j]=="S":
			h=0
			for k in range(j+1,m):
				if a[k][j]!=".":
					h+=1
			if h>0:
				p+=1
			a[i][j]=="."
		if a[i][j]=="E":
			h=0
			for k in range(j):
				if a[i][k]!=".":
					h+=1
			if h>0:
				p+=1
			a[i][j]=="."
print(p)			
