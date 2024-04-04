# File: Tugas1_Nomor2_2272008.py
#Penulis : Elmosius Suli
# Program membaca nama seorang anak dan usianya pada tahun ini.
# Kamus Data
# nama (str)
# usia_sekarang, tahun, tahun_nanti, dan usia_nanti (int)
    
def main ():
        nama = str(input("Nama: "))
        usia_sekarang = int(input("Usia: "))
        tahun = int(input("Tahun: "))
        tahun_nanti = tahun - 2023
        usia_nanti = usia_sekarang + tahun_nanti
       
        print("=================================")
        print(nama, "sekarang berumur", usia_sekarang,"tahun")
        print("---------------------------------")
        print("Tahun", tahun,", dia berumur", usia_nanti,"tahun")
        print("=================================")
        
    
if __name__ == '__main__':
    main()
