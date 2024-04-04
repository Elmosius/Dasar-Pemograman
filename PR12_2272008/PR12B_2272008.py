# File : PR12B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : pprogram yang akan menerima masukan dua 
# buah N*N buah bilangan lalu akan menampilkan 
# matriks baru yang setiap elemennya merupakan penjumlahan 
# nilai pada posisi yang sama dari kedua matriks awal.
## Definisi Fungsi ##

# Fungsi deklarasiMatriks
# Kamus Lokal
# i = var . pengendali for (int)
# arr = var . array menyimpan matriks (int)
# dimensi1 = var . jumlah baris (int)
# dimensi2 = var . jumlah kolom (int)
 
def deklarasiMatriks(dimensi1,dimensi2):
    arr = [None]*dimensi1
    for i in range(0,dimensi1,1):
                 arr[i] = [None]*dimensi2
 
    return arr

## Program Utama ##
# Kamus Lokal
# N : var. input(int)
# i : var. parameter(int)
# j : var. parameter(int)
# arrA : var.array A (int)
# arrB : var.array B (int)

def main():
    N=int(input("N = "))
    arrA= deklarasiMatriks(N,N)
    arrB= deklarasiMatriks(N,N)
    
    # input arrA
    for i in range (0,N,1):
        for j in range (0,N,1):
            print ("A[",i,",",j,"]:", end= " ")
            arrA[i][j]=int(input())

    # input arrB
    for i in range (0,N,1):
        for j in range (0,N,1):
            print ("A[",i,",",j,"]:", end= " ")
            arrB[i][j]=int(input())

    
    # proses dan output
    for i in range(0,N,1):
        for j in range(0,N,1):
            print(arrA[i][j] + arrB[i][j], end=" ")
        print()
        
if __name__ == '__main__':
    main()