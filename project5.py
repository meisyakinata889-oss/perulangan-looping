menu_makanan = ["Nasi Goreng", "Mie Goreng", "Sate Ayam", "Bakso", "Ayam Bakar"]

pesanan = []
total_harga = 0

print("Halo, berikut daftar menu makanan kami:")

for i, makanan in enumerate(menu_makanan):
    print(str(i) + ". " + makanan)

lanjut_pesan = True

while lanjut_pesan:
    jawaban = input("Apakah anda ingin memesan? (ya/tidak): ")

    if jawaban.lower() == "ya":
        pilihan = int(input("Mau pesan makanan nomor berapa? "))

        pesanan.append(menu_makanan[pilihan])

        print("Menambahkan " + menu_makanan[pilihan] + " ke pesanan anda.")

        total_harga += 20000

    else:
        lanjut_pesan = False

print("Anda telah memesan:")
print(pesanan)
print("Total harga: Rp" + str(total_harga))

valid_tip = False

while not valid_tip:
    tip = float(input("Berapa persen tip yang ingin anda berikan (0-25%)? "))

    if (tip >= 0) and (tip <= 25):
        valid_tip = True
    else:
        print("Masukkan angka antara 0 sampai 25.")

total_harga += total_harga * tip / 100

print("Terima kasih! Total harga sekarang Rp" + str(int(total_harga)) + ". Pesanan sedang diproses.")