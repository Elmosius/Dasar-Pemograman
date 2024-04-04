# File : PR01C_2272008.py
# Program Exchange
# Program akan menerima masukan nominal uang, lalu akan menampilkan jumlah lebaran paling sedikit yang merpresentasikan nominal tersebut dalam satuan rupiah.
# Algoritma yang dipakai dalam program tersebut :
# Jumlah setiap lembar uang dicari dengan menggunakan bagi integer dan modulo
# • Pertama carilah jumlah lembar dari nominal uang terbesar menggunakan bagi integer
# • Kemudian hitunglah uang yang belum termaksud dalam jumlah lembar tersebut menggunakan modulo.
# • Lakukan proses kedua dan ketiga berulang dimulai dari nominal terbesar 100.000,- hingga nominal terkecil yaitu 50,-
# ---- Kamus Data ----
# nominal, sisa_1 , sisa_2 , dan seterusnya ialah variabel bertipe integer


def main():
    #input
    nominal = int(input("nominal = "))
    seratus_ribu = int(nominal // 100000)

    sisa_1 = int(nominal % 100000)
    limapuluh_ribu = sisa_1 // 50000

    sisa_2 = int(sisa_1% 50000)
    duapuluh_ribu = sisa_2 // 20000

    sisa_3 = int(sisa_2 % 20000)
    sepuluh_ribu = sisa_3 // 10000

    sisa_4 = int(sisa_3 % 10000)
    lima_ribu = sisa_4 // 5000

    sisa_5 = int(sisa_4 % 5000)
    dua_ribu = sisa_5 // 2000

    sisa_6 = int(sisa_5 % 2000)
    seribu = sisa_6 // 1000

    sisa_7 = int(sisa_6 % 1000)
    lima_ratus = sisa_7 // 500

    sisa_8 = int(sisa_7 % 500)
    dua_ratus = sisa_8 // 200

    sisa_9 = int(sisa_8 % 200)
    seratus = sisa_9 // 100

    sisa_10 = int(sisa_9 % 100)
    lima_puluh = sisa_10 // 50

    #output
    print("menjadi pecahan : ")
    print(seratus_ribu, " lembar uang serartus ribu")
    print(limapuluh_ribu, " lembar uang lima puluh ribu")
    print(duapuluh_ribu, " lembar uang dua puluh ribu")
    print(sepuluh_ribu, " lembar uang sepuluh ribu")
    print(lima_ribu, " lembar uang lima ribu")
    print(dua_ribu, " lembar uang dua ribu")
    print(seribu, " lembar uang seribu")
    print(lima_ratus, " lembar uang lima ratus")
    print(dua_ratus, " lembar uang dua ratus")
    print(seratus, " lembar uang seratus")
    print(lima_puluh, " lembar uang lima puluh")


if __name__ == '__main__':
    main() 


