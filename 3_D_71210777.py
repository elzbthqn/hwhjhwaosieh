import random 
type = input("Masukkan tipe yang ingin anda coba : ")


n_x1 = random.randint(1,20)
a = n_x1
n_x2 = random.randint(1,20)
b = n_x2
n_x3 = random.randint(1,20)
c = n_x3
n_x4 = random.randint(1,20)
d = n_x4
pilihan = ["<",">","=="]
n_o = random.randint(0,2)
pick = pilihan[n_o]

def generatesoal():
	print("(benar/salah) jika", end=" ")

	if type.lower()=="pengurangan":
		print(n_x1,"-",n_x2,pick,n_x3,"-",n_x4, sep='')
	elif type.lower()=="penjumlahan":
		print(n_x1,"+",n_x2,pick,n_x3,"+",n_x4, sep='')
	else:
		print("hanya ada tipe pengurangan/penjumlahan")

generatesoal()
hasil = input("Masukkan Jawaban Anda: ")


def cekHasil():
	if pick == "==" and type.lower() == "penjumlahan":
		if ((a+b)==(c+d)) == True:
			if hasil.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")	
		else: 
			if hasil.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")	
	elif pick == "==" and type.lower() == "pengurangan":	
		if ((a-b)==(c-d)) == True:
			if hasil.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if hasil.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
	elif pick == ">" and type.lower() == "penjumlahan":
		if ((a+b)>(c+d)) == True:
			if hasil.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if hasil.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah!")
	elif pick == ">" and type.lower() == "pengurangan":
		if ((a-b)>(c-d)) == True:
			if hasil.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if hasil.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")	
	elif pick == "<" and type.lower() == "penjumlahan":
		if ((a+b)<(c+d)) == True:
			if hasil.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if hasil.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
	elif pick == "<" and type.lower() == "pengurangan":
		if ((a-b)<(c-d)) == True:
			if hasil.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if hasil.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")

cekHasil()