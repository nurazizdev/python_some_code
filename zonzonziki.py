import random
san=str(input("Qaychi , Qog'oz , Quduq  :" ))
B=["Qaychi" , "Qog'oz" , "Quduq"]
comp=random.randint(0,2)
print(f'Kompyuter {B[comp]} qildi!')
print(f'Siz {san} qildingiz!')
if B.index(B[comp])==B.index(san):
	print("Durrang!!!?")
elif (B.index(B[comp]))%3<(B.index(san))%3:
	print("Yutqazdingiz???")
elif (B.index(B[comp]))%3>(B.index(san))%3:
	print("Yutdingiz!!! ura")



