# File : PR09B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program :  program yang akan menerima masukan 
# N buah judul buku dan sebuah kata lalu akan
# menampilkan semua judul buku dengan kata terkait
## Definisi Fungsi ##

## Program Utama ##
# Kamus Lokal
# N : var. input banyaknya loop(int)
# a : var. array(str)
# i : var. parameter(int)
# j : var. parameter(int)
# cari : var. input(str)
# n : var. jumlah bnyk karakter(int)
# m : var. jumlah bnyk karakter(int)
# kal : var. kalimat(str)

def main():
    # inisial
    N = int(input(""))
    a = N * [None]
    
    # input
    for i in range(0,N,1):
        a[i] = str(input(""))
  
    cari = str(input("cari: "))
    
    # proses dan output
    print("judul yang mengandung kata ",cari,":",sep="")
    for i in range(0,N,1):
        n = len(a[i])
        m = len(cari)
        kal=a[i]
        for k in range(0,n-m+1,1):
            j = 0
            while(j<m) and (cari[j] == kal[k+j]):
                j+= 1
            if(j == m):
                print(a[i])
   
if __name__ == '__main__':
    main()
