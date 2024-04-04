# File : HitungMatrix.py
# Program menghitung data dalam matriks
### Fungsi deklarasi matrik

# Kamus lokal
# arr : var. utk matriks (matriks of integer)
# i : var. indeks baris (integer)
# j : var. indeks kolom (integer)
# d1 : var. banyaknya baris (integer)
# d2 : var. banyaknya kolom (integer)
def matriks(d1,d2):
    arr = [None]*d1 
    for i in range(0,d1,1):
        arr[i] = [None]*d2
    return arr

###Program Utama
# Kamus lokal
# MM : var. utk matriks (matriks of integer)
# i : var. indeks baris (integer)
# j : var. indeks kolom (integer)
# n : var. banyaknya baris (integer)
# m : var. banyaknya kolom (integer)
# totB : var. total baris (integer)
# totK : var. total kolom (integer)
def main():
    n = int(input("Jumlah baris matriks :"))
    m = int(input("Jumlah kolom matriks :"))
    MM = matriks(n,m) #deklarasi matriks
    
    #Input M[i][j]
    for i in range (0,n,1):
        for j in range (0,m,1):
            print ("MM[",i,",",j,"]:", end = " ")
            MM[i][j] = int(input("Nilai :" ))

    #Print isi MM[i][j]
    print("Matriks hasil")
    for i in range (0,n,1):
        for j in range (0,m,1):
            print (MM[i][j], end = " ")
        print()
    
    #hitung total per baris
    for i in range (0,n,1):
        totB = 0
        for j in range (0,m,1):
            totB = totB + MM[i][j]
        print("Total Baris ",i,":",totB)
    
    #hitung total per kolom
    for j in range (0,m,1):
        totK = 0
        for i in range (0,n,1):
            totK = totK + MM[i][j]
        print("Total Kolom ",j,":",totK)
if __name__ == '__main__':
    main()