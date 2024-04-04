# File : Matrix1.py
# Program mengubah isi matriks 
# Kamus Data
# A : var. utk matriks (matriks of integer)
# i : var. indeks baris (integer); j : var. indeks kolom (integer)
# N : konstanta ukuran matriks (integer)
def matriks(d1,d2):
    arr = [None]*d1 
    for i in range(0,d1,1):
        arr[i] = [None]*d2
    return arr
def main():
    N = 3
    A = matriks(N,N) #deklarasi matriks A
    
    # input matriks A
    for i in range (0,N,1):
        for j in range (0,N,1):
            print ("A[",i,",",j,"]:", end = " ")
            A[i][j] = int(input("Nilai :" ))
    
    for i in range (0,N,1):
        for j in range (0,N,1):
            print(A[i][j],end=" ")
        print()
    
    # Ubah isi matriks A
    for i in range (0,N,1):
        for j in range (0,N,1):
            if (i == j):
                A[i][j] = A[i][j]+1
    
    # print matriks A
    print("Matriks berubah jadi:")
    for i in range (0,N,1):
        for j in range (0,N,1):
            print(A[i][j],end=" ")
        print()
if __name__ == '__main__':
    main()

# Matriks berubah jadi:    
# 2 2 3
# 4 6 6
# 7 8 10