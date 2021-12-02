print("Untuk memulai program masukkan (-1) untuk mulai")
a = int(input(": "))

prediksi = 0

def tebakangka():
	global prediksi
	print("Apakah 4?")
	print("Apakah tebakan sudah benar ?")
	print("lebih kecil (0)")
	print("lebih besar (1)")
	print("benar (2)")
	b = int(input(": "))
	prediksi += 1
	if b == 2:
		print("Jumlah tebakan : ", prediksi)
		print("Program Selesai !")
	elif b == 0:
		print("Apakah 2?")
		print("Apakah tebakan sudah benar ?")
		print("lebih kecil (0)")
		print("lebih besar (1)")
		print("benar (2)")
		c = int(input(": "))
		prediksi += 1
		if c == 0:
			print("Hasil Penjumlahannya Pasti 1 !")
			prediksi +=1
			print("Jumlah tebakan :", prediksi)
			print("Program Selesai !")
		elif c == 1:
			print("Hasil Penjumlahannya pasti 3 !")
			prediksi +=1
			print("Jumlah tebakan :", prediksi)
			print("Program Selesai !")
		elif c == 2:
			print("Jumlah tebakan :", prediksi)
			print("Program Selesai !")
	elif b == 1:
		print("Apakah 6?")
		print("Apakah tebakan sudah benar ?")
		print("lebih kecil (0)")
		print("lebih besar (1)")
		print("benar (2)")
		d = int(input(": "))
		prediksi += 1
		if d == 0:
			print("Hasil Penjumlahannya Pasti 5 !")
			prediksi +=1
			print("Jumlah tebakan :", prediksi)
			print("Program Selesai !")
		elif d == 1:
			print("Hasil Penjumlahannya Pasti 7 !")
			prediksi +=1
			print("Jumlah tebakan :", prediksi)
			print("Program Selesai !")
		elif d == 2:
			print("Jumlah tebakan :", prediksi)
			print("Program Selesai !")

if a == -1 : 
	tebakangka()
else : 
	print("Program tidak berhasil dijalankan")