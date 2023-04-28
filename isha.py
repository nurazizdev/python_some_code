b=input()
f=input()
b=b.split(":")
f=f.split(":")
y=int(b[0])*3600+int(b[1])*60+int(b[2])-(int(f[0])*3600+int(f[1])*60+int(f[2]))

x=abs(int(b[0])*3600+int(b[1])*60+int(b[2])-(int(f[0])*3600+int(f[1])*60+int(f[2])))
if y>=0:
    x=24*3600-x
s1=x//3600
s2=(x-s1*3600)//60
s3=x-s1*3600-s2*60
if s1<10 and s2>=10 and s3>=10:
    print(f'0{s1}:{s2}:{s3}')
elif s1<10 and s2<10 and s3>10:
    print(f'0{s1}:0{s2}:{s3}')
elif s1<10 and s2<10 and s3<10:
    print(f'0{s1}:0{s2}:0{s3}')
elif s1<10 and s2>=10 and s3<10:
    print(f'0{s1}:{s2}:0{s3}')
elif s1>=10 and s2<10 and s3<10:
    print(f'{s1}:0{s2}:0{s3}')
elif s1>=10 and s2>=10 and s3<10:
    print(f'{s1}:{s2}:0{s3}')
elif s1>=10 and s2<10 and s3>=10:
    print(f'{s1}:0{s2}:{s3}')
elif s1>=10 and s2>=10 and s3>=10:
    print(f'{s1}:{s2}:{s3}')