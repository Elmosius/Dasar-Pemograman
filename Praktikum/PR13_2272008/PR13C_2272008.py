# File : PR13C_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang memiliki 2 buah array. 
# Array 1 untuk menampung nama siswa, 
# sedangkan Array 2 untuk menampung nilai siswa. 
# Program akan meminta user untuk memasukan 
# jumlah siswa, nama, serta nilai masing-masing siswa
## Definisi Fungsi ##

## Program Utama ##
# Kamus Lokal
# N : var. input(int)
# i : var. parameter(int)
# j : var. parameter(int)
# arrA : var.array A (str)
# arrB : var.array A (int)
# tem : var. untuk pertukaran data(int)
# imax : var. indeks dimana berisi nilai terbsar(int)
# total : var. total nilai(int)

def main():
    # input
    total = 0
    N = int(input("Jumlah Siswa : "))
    arrA= N * [None]
    arrB = N * [None]
    print("=====================")
    
    for i in range(0,N,1):
        arrA[i] = str(input("Nama : "))
        arrB[i] = int(input("Nilai: "))
        total += arrB[i]
        print("=====================")
        
        
    # proses
    for i in range(0,N-1,1):
        imax = i
        for j in range(i+1,N,1):
            if(arrB[j] > arrB[imax]):
                imax = j
        tem = arrB[i],arrA[i]
        arrB[i],arrA[i] = arrB[imax],arrA[imax]
        arrB[imax],arrA[imax] = tem
        
    # output
    for i in range(0,N,1):
        print(arrA[i],'\t',arrB[i])
        
    print("Nilai terbesar diperoleh", arrB[0])
    print("Nilai rata-rata:", round((total/N),1))
if __name__ == '__main__':
    main()