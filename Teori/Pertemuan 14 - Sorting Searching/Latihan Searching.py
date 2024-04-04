## Definisi Fungsi SeqSearch utk pencarian data dalam array
# Kamus lokal 
# N : parameter utk ukuran array (integer)
# X : parameter utk nilai yg akan dicari (integer)
# i : var. counter utk indeks array (integer)
# Found : var.utk catat kondisi pencarian (boolean)
# ix : var. nilai kembalian utk indeks dimana A[ix]=X (integer)
def SeqSearch(N,X):
    global A 
    Found = False
    i = 0
    while (i < N and Found==False):
        if ( A[i]==X):
            Found = True #X sdh ditemukan
        else:
            i = i+1 #siapkan i utk periksa elemen A berikutnya
    if (Found==True):
        ix = i # A[ix] = X (data ditemukan)
    else:
        ix = -1 # ix = -1 : data tidak ditemukan
        
    return ix

# Fungsi IsiArray()
## Definisi Fungsi Isi Array dari input data
# Kamus lokal
# N : var. utk ukuran array (integer)
# i : var. counter utk pengendali for (integer)
# fungsi mengirimkan nilai N
def IsiArray():
    global A
    
    N = int(input("N:"))
    for i in range (0,N,1):
        A[i] = int(input("Nilai :"))
    return N


# Fungsi PrintArray(N)
## Definisi Fungsi utk cetak data dalam array ke layar
# Kamus lokal
# N : parameter utk ukuran array (integer)
# i : var. counter utk pengendali for (integer)
def PrintArray(N):
    global A
    for i in range (0,N,1):
        print ('A[',i,'] = ',A[i])
    return

def BinSearch(N,X):
    global A
    Found = False
    atas = 0
    bawah = N-1
    ix = -1
    
    while (atas <= bawah and not Found):
        tengah = (atas + bawah)//2
        if ( A[tengah]==X):
            Found = True #data ditemukan
            ix = tengah
        elif (X < A[tengah]):
            bawah = tengah - 1 #bawah digeser
        else:
            atas = tengah + 1 #atas digeser
    return ix

## Program Utama
#N : banyaknya data dalam array A (int)
#X : nilai yang akan dicari (int)
#IN : indeks posisi dimana A[IN] = X (int)
def main():
    N = IsiArray()
    PrintArray(N)
    X = int(input("Nilai yang dicari (X):"))
    while (X!=9999):
        IN = SeqSearch(N,X)
        if (IN >= 0):
            print("Data",X," ada di A[",IN,"]")
        else:
            print("Data",X," tidak ada dalam A")
        X = int(input("Nilai yang dicari (X):"))
    
if __name__ == '__main__':
    Nmax = 100
    A = Nmax *[None] #deklarasi array A var.global
    main()