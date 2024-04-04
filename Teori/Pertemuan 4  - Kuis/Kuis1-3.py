# File : Soal1-3.py
# Penulis : Elmosius Suli
# Tujuan Program : program untuk menghitung dan mencetak ekivalensi berat dalam satuan kg atau pon atau ons.
# Kamus Data : 
# nama : var. input (str)
# berat : var. input (int)
# kg : var. proses perhitungan gram ke kg (int)
# pon : var. proses perhitungan kg ke pon (int)
# ons : var. proses perhitungan  pon ke ons (int)

def main():
   
    # input
    nama = input("Nama : ")
    berat = int(input("Berat (gram) : "))

    # proses
    kg = berat / 1000
    pon = kg / 0.454
    ons = pon / 0.2

    # output
    if (berat >= 0):
        print("Berat badan",nama,"adalah",kg, \
        "kg atau",round(pon,2), \
        "pon atau",round(ons,2),"ons.")
    else:
        print("Berat badan < 0 silahkan masukkan angka >= 0")
    

    # print("Berat badan",nama,"adalah {:.1f} kg atau {:.2f} pon atau {:.2f} ons".format(kg,pon,ons))
if __name__ == '__main__':
    main()