# File : PR010A_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang menerima tiga buah 
# array berukuran N lalu akan menampilkan 
# nilai terbesar dari setiap indeks yang ada
## Definisi Fungsi ##

## Program Utama ##
# Kamus Lokal
# N : var. input N(int)
# i : var. paramater(int)
# arrA : var. array pertama(int)
# arrB : var. array kedua(int)
# arrC : var. array ketiga(int)

def main():
    # input 
    N = int(input(""))
   
    arrA = N * [None]
    for i in range (0,N,1):
       arrA[i] = int(input(""))
       
    arrB = N * [None]   
    for i in range (0,N,1):
       arrB[i] = int(input(""))
       
    arrC = N * [None]
    for i in range (0,N,1):
       arrC[i] = int(input(""))
    
    # proses dan output
    for i in range (0,N,1):
        if(arrA[i] > arrB[i] ):
            if(arrA[i] > arrC[i]):
                print(arrA[i], end=" ")
            else:
                print(arrC[i], end=" ")
        else:
            if(arrB[i] > arrC[i]):
                print(arrB[i], end=" ")
            else:
                print(arrC[i], end=" ")
                
if __name__ == '__main__':
    main()