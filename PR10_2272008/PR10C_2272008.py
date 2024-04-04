# File : PR010C_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program :  program yang akan menerima
# masukan  N buah bilangan dan M buah bilangan 
# lalu akan menampilkan gabungan dari kedua
# himpunan bilangan tersebut.
## Definisi Fungsi ##

## Program Utama ##
# Kamus Lokal
# N : var. input N(int)
# M : var. input M (int)
# i : var. parameter (int)
# arrA : var. array pertama(int)
# arrB : var. array kedua(int)
# arrC : var. array menyimpan union(int)
# Nmax : var. kapasitas arrC (int)
# c : var. index(int)

def main():
    # inisialisasi
    N = int(input(""))
    
    arrA = N * [None]
    for i in range(0,N,1):
        arrA[i] = int(input(""))
    
    M = int(input(""))
    arrB = M * [None]

    for i in range(0,M,1):
        arrB[i] = int(input(""))
    
    Nmax = 100
    arrC = Nmax * [None]
    arrC[0] = arrA[0]
    
    # proses dan output 
    c = 1
    
    for i in range (1,N,1):
        if arrA[i] not in arrC:
            arrC[c] = arrA[i]
            c += 1
    for i in range (0,M,1):
        if arrB[i] not in arrC:
            arrC[c] = arrB[i]
            c += 1     
    for i in range (0,c,1):
        print(arrC[i], end=" ")
    
           
if __name__ == '__main__':
    main()
