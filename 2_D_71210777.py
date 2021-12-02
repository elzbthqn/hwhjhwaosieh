kt=input("Masukkan sebuah kata/kalimat: ")
kr=input("Masukkan karakter yang ingin disisipkan: ")

def sisipHuruf(kt,kr):
    cap=kt.upper()
    print(kr.join(list(cap)))
def sisipKata(kt,kr):
    cap=kt.title()
    print(kr.join(cap.split()))

sisipHuruf(kt,kr)
sisipKata(kt,kr)