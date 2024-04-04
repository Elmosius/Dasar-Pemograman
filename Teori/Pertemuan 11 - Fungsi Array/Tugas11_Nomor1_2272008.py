# File : Tugas11_Nomor1_2272008.py
# Penulis : Elmosius Suli
# Tujuan : Program akan mencetak nama yang
# mendapat IPK tertinggi.
# Kamus Data 
# N : var. input N (int)
# arr_nama : var. array nama(str)
# arr_ipk : var. array ipk(float)
# ipk_tertinggi : var. menentukan ipk tertinggi(float)
# i : var. parameter(int)
# m : var. index ipk tertinggi (int)

def main():
    # input untuk N
    N = int(input("N = "))
    
    # deklarasi array nama dan ipk, pesan memori sebesar N
    arr_nama = N * [None]
    arr_ipk  = N * [None]
    
    # input data ke dalam array nama dan ipk (pakai for) 
    for i in range(0,N,1):
        arr_nama[i] = str(input("nama: "))
        arr_ipk[i] = float(input("ipk: "))
        
    print("-"*50)
    # tentukan ipk tertinggi dalam array ipk(pakai for) 
    ipk_tertinggi = arr_ipk[0]
    m = 0
    
    for i in range(1,N,1):
        if (arr_ipk[i] > ipk_tertinggi):
            ipk_tertinggi =  arr_ipk[i]
            m = i
    
    # print nama dan ipk tertinggi
    print()
    print("IPK tertinggi diraih oleh",arr_nama[m],": ", arr_ipk[m])
    print()
    print("-"*50)
    
    # print kelompok data untuk dengan pujian (cetak di dalam for)
    print("Predikat dengan pujian :", end=" ")
    for i in range(0,N,1):
        if (arr_ipk[i] > 3.5):
            print(arr_nama[i], end=" ")
    print()
    print()
    print("-"*50)

    # print kelompok data untuk sangat memuaskan (cetak di dalam for)
    print("Predikat sangat memuaskan :", end=" ")
    for i in range(0,N,1):
        if (arr_ipk[i] > 3.0 and arr_ipk[i] <= 3.5):
            print(arr_nama[i], end=" ")
    print()
    print()
    print("-"*50)
    
     # print kelompok data untuk memuaskan (cetak di dalam for)
    print("Predikat memuaskan :", end=" ")
    for i in range(0,N,1):
        if (arr_ipk[i] > 2.75 and arr_ipk[i] <= 3.0 ):
            print(arr_nama[i], end=" ")
    print()
    print()
    print("-"*50)
     
    
if __name__ == '__main__':
    main()
    
