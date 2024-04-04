# File : Tugas11_Nomor2_2272008.py
# Penulis : Elmosius Suli
## Definisi Fungsi ##

# Fungsi IsiArray()
## Definisi Fungsi Isi Array dari input data
# Kamus lokal 
# N : var. input,banyak data dalam array (int)
# fungsi mengirimkan nilai N

def IsiArray():
    global arr_ipk, arr_nama
    N = int(input("N = ")) 
    
# variabel Global
# arr_nama : var. global array nama(str)
# arr_ipk : var. global arrau ipk(float)

    arr_nama = N * [None]
    arr_ipk  = N * [None]
    
    for i in range(0,N,1):
        arr_nama[i] = str(input("nama: "))
        arr_ipk[i] = float(input("ipk: "))
        
    return(N)

# Fungsi IPKMax(N)
## Definisi Fungsi IPKMax dari data dalam array ipk
# Kamus lokal
# N : var. banyak data dalam array (int)
# m : var. index ipk tertinggi (int)
# fungsi mengirimkan posisi indeks m, dimana ipk[m] tertinggi
def IPKMax(N):
    global arr_ipk
    
    m = 0
    ipk_tertinggi = arr_ipk[0]
    for i in range(1,N,1):
        if (arr_ipk[i] > ipk_tertinggi):
            ipk_tertinggi =  arr_ipk[i]
            m = i
    return(m)

# Fungsi PrintDP(N)
## Definisi Fungsi PrintSM dari data dalam array nama
# Kamus lokal 
# N : var. banyak data dalam array (int)
# fungsi mencetak nama dengan ipk > 3.5
def PrintDP(N):
    print("Predikat dengan pujian :", end=" ")
    for i in range(0,N,1):
        if (arr_ipk[i] > 3.5):
            print(arr_nama[i], end=" ")
    
# Fungsi PrintSM(N)
## Definisi Fungsi PrintSM dari data dalam array nama
# Kamus lokal 
# N : var. banyak data dalam array (int)
# fungsi mencetak nama dengan ipk <= 3.5 dan ipk > 3.0
def PrintSM (N):
    print("Predikat sangat memuaskan :", end=" ")
    for i in range(0,N,1):
        if (arr_ipk[i] > 3.0 and arr_ipk[i] <= 3.5):
            print(arr_nama[i], end=" ")

# Fungsi PrintM(N)
## Definisi Fungsi PrintM dari data dalam array nama
# Kamus lokal 
# N : var. banyak data dalam array (int)
# fungsi mencetak nama dengan ipk <= 3.0 dan ipk > 2.75
def PrintM (N):
    print("Predikat memuaskan :", end=" ")
    for i in range(0,N,1):
        if (arr_ipk[i] > 2.75 and arr_ipk[i] <= 3.0 ):
            print(arr_nama[i], end=" ")
            
# Fungsi printPredikat
# Kamus Lokal
# N : var. banyak data dalam array (int)
# batas1 : var. batas ipk pertama(float)
# batas2 : var. batas ipk kedua(float)
# fungsi mencetak nama dengan ipk yang ditentukan batas1 dan batas2
def printPredikat(N,batas1,batas2):
    global arr_ipk, arr_nama
    
    if (batas1 >= 3.5 and batas2 <= 4.0):
         print("Predikat dengan pujian :", end=" ")
         
    elif(batas1 >= 3.0 and batas2 <= 3.5):
        print("Predikat sangat memuaskan :", end=" ")
    else:
        print("Predikat memuaskan :", end=" ")
        
    for i in range(0,N,1):
        if (arr_ipk[i] > batas1 and arr_ipk[i] <= batas2):
            print(arr_nama[i], end=" ")

## Program Utama ##
# Kamus Lokal
# N : var. menyimpan dari fungsi IsiArray() (int)
# max : var. menyimpan dari fungsi IPKMax(N) (int)

def main():
    # Panggil fungsi IsiArray(), simpan nilai N
    N = IsiArray()
    
    # panggil fungsi IPKMax(N), simpan index max
    max = IPKMax(N)
    
    # print nama[max] dan ipk[max]
    print()
    print("IPK tertinggi diraih oleh", arr_nama[max],": ", arr_ipk[max])
    print()
    print("-"*50)
    
    # Panggil fungsi printPredikat(N,batas1,batas2)
    # untuk predikat dengan pujian
    printPredikat(N,3.5,4.0) 
    print()
    print()
    print("-"*50)
    
    #  untuk predikat sangat memuaskan  
    printPredikat(N,3.0,3.5)
    print()
    print()
    print("-"*50)

    # untuk predikat memuaskan
    printPredikat(N,2.75,3.0)
    print()
    print()
    print("-"*50)
    
if __name__ == '__main__':
    #Tuliskan deklarasi array barang dan array harga sebagai var.global
    global arr_ipk, arr_nama
    main()
    
    
    
