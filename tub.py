a=int(input())
def IsPrime(a):
  k=int(pow(a,1/2))
  for i in range(2,k+1):
    if a%i==0:
      return False
  return True
print(IsPrime(a))