# File : TopDown.py
# Nama program : Program contoh untuk top down programming
## Definisi Fungsi ##

# fungsi menu
def menu():
    print("Selamat Datang")
    print("Selamat bergabung bersama kami")
    print("Silakan masukan sebuah bilangan positif !")
    return

# fungsi masukan dengan validasi 
# Kamus lokal
# x : var. input validasi(int)
def masukan():
    x = int(input("Nilai masukan : "))
    while(x < 0):
        x = int(input("Nilai masukan : "))
    return(x)

# fungsi keluaran
# Kamus lokal
# i : var. pengendali loop (int)
# x : var. parameter fungsi(int)

def keluaran(x): 
    for i in range(1,x,1):
        print(i,end=" ")
    for i in range(x,0,-1):
        print(i,end=" ")
    print()

## Program Utama ##
# Kamus lokal
# m : var. menyimpan input(int)

def main():
    menu()
    m = masukan()
    keluaran(m)
    
if __name__ == "__main__":
    main()