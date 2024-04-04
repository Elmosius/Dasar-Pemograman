# File : PR09B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program :  program yang menerima N bilangan bulat 
# menampilkan hasil penjumlahan setiap bilangan
## Definisi Fungsi ##

## Program Utama ##
# Kamus Lokal
# N : var. input banyaknya loop(int)
# a : var. array(int)
# i : var. parameter(int)

def main():
    # inisial
    N = int(input(""))
    a = N * [None]
    
    # proses dan output
    for i in range(0,N,1):
        a[i] = int(input(""))
    print(a[0],end=" ")
    
    for i in range(0,N-1,1):
        a[i] += a[i+1]
        print(a[i], end=" ")
    
if __name__ == '__main__':
    main()