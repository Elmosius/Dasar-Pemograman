# File : PR08A_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima masukan lima 
# buah bilangan dan akan menampilkan bilangan
# kedua terkecil dari kelima bilangan tersebut

# fungsi keduakecil
# Kamus Lokal
# a : var. parameter(int)
# b : var. parameter(int)
# c : var. parameter(int)
# d : var. parameter(int)
# e : var. parameter(int)
# kk1 : var. kedua kecil pertama(int)
# kk2 : var. kedua kecil kedua(int)

def keduakecil(a,b,c,d,e):
    kk1 = a
    kk2 = b
    
    if (a > b):
        kk1 = b
        kk2 = a
    if(c < kk1):
        kk2 = kk1
        kk1 = c
    elif(c < kk2):
        kk2 = c
    
    if(d < kk1):
        kk2 = kk1
        kk1 = d
    elif(d < kk2):
        kk2 = d
        
    if(e < kk1):
        kk2 = kk1
        kk1 = e
    elif(e < kk2):
        kk2 = e
        
    return kk2
    

## Program Utama ##
# Kamus Lokal
# a : var. input angka pertama(int)
# b : var. input angka kedua(int)
# c : var. input angka ketiga(int)
# d : var. input angka keempat(int)
# e : var. input angka kelima(int)

def main():
    # input
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))
    d = int(input(""))
    e = int(input(""))
    
    # output
    print("Kedua terkecil: ",keduakecil(a,b,c,d,e))
    
if __name__ == '__main__':
    main()