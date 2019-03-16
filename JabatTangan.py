orang = int(input("Masukkan jumlah orang : "))

def hitungJabatTangan(orang):
    count = 1
    jabat_tangan = 1

    while count < orang - 1:
        count = count + 1
        jabat_tangan = jabat_tangan + count
    print("Terdapat " + str(jabat_tangan) + " jabat tangan")

if orang < 2:
    print("Tidak terjadi jabat tangan")
else:
    hitungJabatTangan(orang)