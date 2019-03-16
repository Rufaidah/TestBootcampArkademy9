side = int(input("MAsukkan sisi persegi : "))

def drawImage(side):
    if side % 2 == 0:
        return False
    else:
        # row
        for i in range(side):
            # column
            for j in range(side):
                if (i == (side - 1) / 2) or (j == (side - 1) / 2) \
                        or (i | j == 0) or (i == 0 and j == side - 1) \
                        or (i == side - 1 and j == 0) or (i == side - 1 and j == side - 1):
                    print("*", end='')
                else:
                    print("=", end='')
            print()
        return True

if drawImage(side) == True:
    print()
else:
    print("Panjang sisi harus ganjil")