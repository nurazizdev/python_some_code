def isDivisibleBy2(num):
  s=str(num)
  if int(s[len(s)-1])%2==0:
    return True
  return False
def isDivisibleBy3(num):
  s=str(num)
  h=0
  for i in range(len(s)):
    h+=int(s[i])
  if h%3==0:
    return True
  return False
def isDivisibleBy4(num):
  s=str(num)
  if (10*int(s[len(s)-2])+int(s[len(s)-1]))%4==0:
    return True
  return False
def isDivisibleBy5(num):
  s=str(num)
  if int(s[len(s)-1])==0 or int(s[len(s)-1])==5:
    return True
  return False
def isDivisibleBy6(num):
  if isDivisibleBy2(num) and isDivisibleBy3(num):
    return True
  return False
def isDivisibleBy7(num) :
  if num < 0 :
    return isDivisibleBy7( -num )
  if( num == 0 or num == 7 ) :
    return True    
  if( num < 10 ) :
    return False
  return isDivisibleBy7( num // 10 - 2 * ( num - num // 10 * 10 ) )
def isDivisibleBy8(num):
  s=str(num)
  if len(s)>=3 and (100*int(s[len(s)-3])+10*int(s[len(s)-2])+int(s[len(s)-1]))%8==0:
    return True
  elif len(s)<3 and num%8==0:
    return True
  return False
def isDivisibleBy9(num):
  s=str(num)
  h=0
  for i in range(len(s)):
    h+=int(s[i])
  if h%9==0:
    return True
  return False
def isDivisibleBy10(num):
  if isDivisibleBy2(num) and isDivisibleBy5(num):
    return True
  return False
def isDivisibleBy11(num):
  s=str(num)
  h=0
  p=0
  for i in range(len(s)):
    if n%2==0:
      h+=int(s[i])
    else:
      p+=int(s[i])
  if p-h%11==0:
    return True
  return False
def isDivisibleBy12(num):
  if isDivisibleBy4(num) and isDivisibleBy3(num):
    return True
  return False
def isDivisibleBy13( num):
    length = len(num)
    if (length == 1 and num[0] == '0'):
        return True
 
    if (length % 3 == 1):
         
    
        num = str(num) + "00"
        length += 2
     
    elif (length % 3 == 2):
         
   
        num = str(num) + "0"
        length += 1

    sum = 0
    p = 1
    for i in range(length - 1, -1 , -1) :
         

        group = 0
        group += ord(num[i]) - ord('0')
        i -= 1
        group += (ord(num[i]) - ord('0')) * 10
        i -= 1
        group += (ord(num[i]) - ord('0')) * 100
 
        sum = sum + group * p

        p *= (-1)
    sum = abs(sum)
    return (sum % 13 == 0)
def isDivisibleBy14(num):
  if isDivisibleBy7(num) and isDivisibleBy2(num):
    return True
  return False
def isDivisibleBy12(num):
  if isDivisibleBy5(num) and isDivisibleBy3(num):
    return True
  return False
def isDivisibleBy16(num):
  s=str(num)
  if len(s)>=4 and (1000*int(s[len(s)-4])+100*int(s[len(s)-3])+10*int(s[len(s)-2])+int(s[len(s)-1]))%8==0:
    return True
  elif len(s)<4 and num%16==0:
    return True
  return False
def isDivisibleBy17(n) :
 
    while(n // 100) :
 
        d = n % 10
 
        n //= 10
 

        n -= d * 5

    return (n % 17 == 0)





t=int(input())
while t:
  t-=1
  l,r=map(int,input().split())
  