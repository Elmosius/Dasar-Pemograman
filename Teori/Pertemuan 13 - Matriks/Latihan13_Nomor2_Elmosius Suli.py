# File : Matrix2.py
# Program mengubah isi matriks 
# Kamus Data
# A,B : var. utk matriks (matriks of integer)
# i : var. indeks baris (integer); j : var. indeks kolom (integer)
# N : konstanta ukuran matriks (integer)
def matriks(d1,d2):
    arr = [None]*d1 
    for i in range(0,d1,1):
        arr[i] = [None]*d2
    return arr

def main():
    N = 3
    A = matriks(N,N)
    B = matriks(N,N)
    
    # input matriks A
    for i in range (0,N,1):
        for j in range (0,N,1):
            print ("A[",i,",",j,"]:", end = " ")
            A[i][j] = int(input("Nilai :" ))
    
    print("Matriks A:")
    for i in range (0,N,1):
        for j in range (0,N,1):
            print(A[i][j],end=" ")
        print()
        
    # isi matriks B
    for j in range (0,N,1):
        k = 0
        for i in range (0,N,1):
            B[i][j] = A[j][k]
            k = k + 1
    
    # print matriks B
    print("Matriks B:")
    for i in range (0,N,1):
        for j in range (0,N,1):
            print(B[i][j],end=" ")
        print()
        
if __name__ == '__main__':
    main() 
    
# Matriks B:
# 1 4 7
# 2 5 8
# 3 6 9

