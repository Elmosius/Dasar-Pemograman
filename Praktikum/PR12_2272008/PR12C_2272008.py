# File : PR12C_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima map bom berukuran 
# N*N (0 menyatakan kosong dan 1 menyatakan bom) lalu akan
# menampilkan map baru dimana setiap posisi menandakan berapa 
# banyak jumlah bom yang ada di sekitarnya
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
# arrB = var.array B (int)

def main():
    N=int(input("N = "))
    arrA = deklarasiMatriks(N,N)
    arrB = deklarasiMatriks(N,N)
    
    # input arrA
    for i in range (0,N,1):
        for j in range (0,N,1):
            print ("A[",i,",",j,"]:", end= " ")
            arrA[i][j] = int(input())
            arrB[i][j] = 0

    # proses dan output
    for i in range(0,N,1):
        for j in range(0,N,1):
            if(j == 0):
                if(1 == arrA[i][j+1]):
                    arrB[i][j] += 1
                if(i < N-1):
                    if(1 == arrA[i+1][j]):
                        arrB[i][j] += 1
                    if(1 == arrA[i+1][j+1]):
                        arrB[i][j] += 1
                if(0 < i):
                    if(1 == arrA[i-1][j]):
                        arrB[i][j] += 1
                    if(1 == arrA[i-1][j+1]):
                        arrB[i][j] += 1
                    
            if(0 < j and j < N-1):
                if(1 == arrA[i][j-1]):
                    arrB[i][j] += 1
                if(1 == arrA[i][j+1]):
                    arrB[i][j] += 1
                if(i < N-1):
                    if(1 == arrA[i+1][j-1]):
                        arrB[i][j] += 1
                    if(1 == arrA[i+1][j]):
                        arrB[i][j] += 1
                    if(1 == arrA[i+1][j+1]):
                        arrB[i][j] += 1
                if(0 < i):
                    if(1 == arrA[i-1][j-1]):
                        arrB[i][j] += 1
                    if(1 == arrA[i-1][j]):
                        arrB[i][j] += 1
                    if(1 == arrA[i-1][j+1]):
                        arrB[i][j] += 1
            if(j == N-1):
                if(1 == arrA[i][j-1]):
                    arrB[i][j] += 1
                if(i < N-1):
                    if(1 == arrA[i+1][j]):
                        arrB[i][j] += 1
                    if(1 == arrA[i+1][j-1]):
                        arrB[i][j] += 1
                if(0 < i):
                    if(1 == arrA[i-1][j]):
                        arrB[i][j] += 1
                    if(1 == arrA[i-1][j-1]):
                        arrB[i][j] += 1
        print()
if __name__ == '__main__':
    main()