# File : PR010B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program :  sebuah program yang menerima N 
# nama mahasiswa beserta umurnya lalu akan 
# menampilkan semua mahasiswa berumur tidak 
# lebih kecil dari 17 dan namanya diawali huruf vocal
## Definisi Fungsi ##

## Program Utama ##
# Kamus Lokal
# N : var. input n(int)
# i : var. paramter(int)
# huruf : var. array huruf(int)
# arrNama : var. array nama(str)
# arrUmur : var. array umur(int)

def main():
    # inisial
    N = int(input(""))
    arrNama = N * [None]
    arrUmur = N * [None]
    huruf = ''

    # input
    for i in range (0,N,1):
        arrNama[i] = str(input(""))
        arrUmur[i] = int(input(""))
    print()
    
    # proses dan output
    for i in range(0,N,1):
        if(arrUmur[i] >= 17):
            a = len(arrNama[i]) 
            huruf = a * [None]
            huruf = arrNama[i]
    
            if(huruf[0] == 'a'):
                print(arrNama[i])
            elif(huruf[0] == 'i'):
                print(arrNama[i])
            elif(huruf[0] == 'u'):
                print(arrNama[i])
            elif(huruf[0] == 'e'):
                print(arrNama[i])
            elif(huruf[0] == 'o'):
                print(arrNama[i])
    
if __name__ == '__main__':
    main()