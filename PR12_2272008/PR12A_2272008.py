# File : PR012A_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima masukan N*N 
# buah bilangan lalu akan menampilkan bilangan 
# matriks setelah dirotasi ke kanan 90 derajat
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

def main():
    N=int(input("N = "))
    arrA=deklarasiMatriks(N,N)
    for i in range (0,N,1):
        for j in range (0,N,1):
            print ("A[",i,",",j,"]:", end= " ")
            arrA[i][j]=int(input())

    for i in range(0,N,1):
        for j in range(N-1,-1,-1):
            print(arrA[j][i], end=" ")
        print()
        
if __name__ == '__main__':
    main()