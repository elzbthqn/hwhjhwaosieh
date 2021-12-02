str = input("Masukkan string : ")

def cekString():
	if str.replace(".","").isnumeric() == True:
		if float(str)%2 == 0:
			print(format(float(str)/2, ".0f"))
		else :
			print(format((round(float(str))+5)/2, ".0f"))
	else:
		print(str[::-1])

cekString()