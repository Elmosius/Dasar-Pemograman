# File: Tugas5_Nomor1_2272008.py
# Penulis : Elmosius Suli
# Tujuan : program yang menerima input sebuah bilangan N dan akan membentuk
# segitiga bintang sebanyak N baris yang sisi tegaknya merapat ke kanan
# Kamus Data
# angka : var. input N (int)
# i : var. counter untuk for pertama (int)
# j : var. counter untuk for kedua (int)
# k : var. counter untuk for ketiga (int)
# bintang : var. membuat bintang (int)
# spasi : var. membuat spasi (int) 

def main ():
   
    # input
    angka = int(input("N : "))
    
    # proses dan output
    bintang = 1
    spasi = angka-1
    for i in range (0,angka,1):
        for j in range (0,spasi,1):
            print(" ", end=" ")
        for k in range (0,bintang,1):
            print('*', end=" ")
        bintang += 1
        spasi -= 1    
        print()   
        
if __name__ == '__main__':
    main()