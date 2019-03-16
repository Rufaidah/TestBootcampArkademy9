belanja = int(input("Masukkan total belanja : Rp"))
bayar = int(input("Masukkan total uang yang dimasukkan : Rp"))
kembalian = [50000, 20000, 10000, 5000, 2000, 1000, 500]

def hitungKembalian(belanja, bayar):
    total_kembalian = bayar - belanja
    print("Total kembalian adalah : Rp" + str(total_kembalian) + "\nDengan pecahan : ")

    for x in range (0, 7):
        i = 0
        while total_kembalian >= kembalian[x]:
            total_kembalian = total_kembalian - kembalian[x]
            i = i + 1
            if i > 0:
                print(str(i) + " x Rp" + str(kembalian[x]))
            else:
                break

hitungKembalian(belanja, bayar)