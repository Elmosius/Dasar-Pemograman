# File: Tugas1_Nomor1_2272008.py
# Penulis : Elmosius Suli
# Program membaca suatu bilangan integer yang menyatakan jumlah hari
# Kamus Data
# JH, B, M, T ialah variabel bertipe integer
# round(x, (berapa anggka dibelakang koma yang ingin diambil))


def main ():
        JH = int(input("Jumlah hari : "));
        B = JH // 30
        M =  JH // 7
        T = round(JH /  365, 3)

        print(JH, " hari adalah sama dengan", B, "bulan atau", M, "minggu atau", T, "tahun.")
        

if __name__ == '__main__':
    main()