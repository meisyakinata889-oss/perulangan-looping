# Perulangan for dengan range
#for i in range(5):
    #print("Perulangan ke-", i)

# Perulangan while
#angka = 0
#while angka < 5:
    #print("Angka sekarang", angka)
    #angka += 1  # menambah nilai agar tidak infinite loop

# Cetak bilangan genap dari 1 sampai 10
#for i in range(1, 11):
    #if i % 2 == 0:
        #print(i)

# Program tebak angka sederhana
#rahasia = 7
#tebakan = 0

#while tebakan != rahasia:
    #tebakan = int(input("Tebak angka antara 1 sampai 10: "))
    #if tebakan < rahasia:
        #print("Terlalu rendah!")
    #elif tebakan > rahasia:
        #print("Terlalu tinggi!")
    #else:
        #print("Selamat! Tebakanmu benar.")

angkaA = [2, 4, 6, 7, 8]
angkaB = []

for angka in angkaA:
    angkaB.append(angka * 2)

print(angkaA)
print(angkaB)








