# File : PR01B_2272008.py
# Program Balok
# Program akan menjalankan algoritma berikut:
# • Meng-input variabel panjang (p) dan meminta user untuk memberi masukan
# • Meng-input variabel lebar (l) dan meminta user untuk memberi masukan
# • Meng-input variabel tinggi (t) dan meminta user untuk memberi masukan
# • Menampilkan keliling dengan rumus: 4(p + l + t)
# • Menampilkan luas permukaan dengan rumus : 2(p x l + l5 x t + p x t)
# • Menampilkan volume dengan rumus: p x l x t

# ---- Kamus Data ----
# panjang, lebar, dan tinggi ialah variabel yang bertipe integer
# Menggunakan syntax print()

def main():
    #input
    panjang = int(input("panjang(cm) : "))
    lebar = int(input("lebar(cm) : "))
    tinggi = int(input("tinggi(cm) : "))

    #output
    print("keliling = ", 4*(panjang + lebar + tinggi), "cm")
    print("luas = ", 2*(panjang * lebar + lebar * tinggi + panjang * tinggi)," cm^2" )
    print("volume = ", panjang * lebar * tinggi, " cm^3")

if __name__ == '__main__':
    main() 

