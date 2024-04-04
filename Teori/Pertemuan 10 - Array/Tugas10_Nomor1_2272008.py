# File : Latihan10_Nomor3_2272008.py
# Penulis : Elmosius Suli
# Tujuan : program yang menginput data sembarang ke dalam 
# array yang diakhiri dengan 999
## Definisi Fungsi ##

## Program Utama ##
# Kamus Lokal 
# i : var. paramater (int)
# jumlah : var. jumlah pada array(int)
# Nmax : var. banyaknya data dalam array(int)
# data : var. input(int)
# A : var. array(int)
# N : var. menghitung banyaknya data (int)
# m : var. data pada urutan 0(int)
# nilai_terbesar : var. nilai terbesar pada array(int)
# nilai_terkecil : var. nilai terkecil pada array(int)
# rata_rata : var. nilai rata-rata (float)

def main():
    # inisial
    i = 0
    jumlah = 0
    
    # input
    Nmax = 100
    A = Nmax * [None]
    data = int(input("data: "))
    
    # input data ke dalam array (pakai while)
    while(data != 999):
        A[i] = data
        i+= 1
        data = int(input("data: "))
    
    # hitung jumlah data & banyaknya data yang ada dalam array (pakai for)  
    N = i 
    for i in range (0,N,1):
        jumlah+= A[i]
    
    # hitung rata-rata (pakai rumus)
    rata_rata = jumlah/N
    
    # tentukan nilai terbesar dan nilai terkecil (pakai for)
    m = A[0]
    for i in range(1,N,1):
        if A[i] > m:
            nilai_terbesar = A[i]
        if A[i] < m:
            nilai_terkecil = A[i]
            
    # print nilai rata-rata, terbesar dan terkecil      
    print('Nilai rata-rata :', rata_rata)
    print('Nilai terbesar :',nilai_terbesar)
    print('Nilai terkecil :',nilai_terkecil)
    
    # print data < rata-rata (cetak di dalam for)
    print("Kelompok data <",rata_rata,':',end=" ")
    for i in range(0,N,1):
        if(A[i] < rata_rata):
            print(A[i], end=" ")
    print()
    
    # print data > rata-rata (cetak di dalam for)
    print("Kelompok data >",rata_rata,':',end=" ")
    for i in range(0,N,1):
        if(A[i] > rata_rata):
            print(A[i], end=" ")
    print()
if __name__ == '__main__':
    main()
