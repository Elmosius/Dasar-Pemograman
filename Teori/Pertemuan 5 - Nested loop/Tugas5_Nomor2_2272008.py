# File: Tugas5_Nomor1_2272008.py
# Penulis : Elmosius Suli
# Tujuan : program untuk menggambar beberapa bentuk bangun datar
## Definisi Fungsi ##
   
# fungsi memu tampilan awal
def menu():
    print("Pilih Gambar")
    print ("1. Segitiga")
    print ("2. Persegi Panjang")
    print ("3. Jajaran Genjang")
    print ("4. Selesai")
    print("--------------------")
    return

# fungsi input pilihan integer
# Kamus lokal
# pilih : var. input pilihan (int)
def masukan(): 
    pilih = int(input("pilihan:")) 
    return(pilih)

# fungsi proses dan output
# Kamus lokal 
# sisi : var. input sisi pilihan 1 (int)
# panjang : var. input panjang pilihan 2 dan 3 (int)
# lebar : var. input lebar pilihan 2 dan 3 (int)
# i : var. counter untuk for pertama (int)
# j : var. counter untuk for kedua (int)
# k : var. counter untuk for ketiga (int)
# spasi : var. membuat spasi di pilihan 3 (int) 
def keluaran(pilih):
    while (pilih!= 4):
        if(pilih == 1):
            sisi = int(input("sisi:"))
            for i in range (0,sisi+1,1):
                for j in range (i):
                    print('*', end=" ")
                print()
                
        elif(pilih == 2):
            panjang = int(input("panjang:"))
            lebar = int(input("lebar:"))
            for i in range (0,panjang,1):
                for j in range (0,lebar,1):
                    print('*', end=" ")
                print()   
                
        elif(pilih == 3):
            panjang = int(input("panjang:"))
            lebar = int(input("lebar:"))
            for i in range (0,panjang,1):
                for j in range (0,i,1):
                    print(' ', end=" ")
                for k in range (0,lebar,1):
                    print('*', end=" ")
                print()
                      
        pilih = int(input("pilihan:"))     
        
## Program Utama ## 
# Kamus lokal
# x : var. menyimpan input (int)
def main ():    
    menu()
    x = masukan()
    keluaran(x)
    
if __name__ == '__main__':
    main()