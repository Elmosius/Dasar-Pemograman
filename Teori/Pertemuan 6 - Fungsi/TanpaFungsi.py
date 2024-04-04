# File : TanpaFungsi.py
# Penulis : Elmosius Suli
# Tujuan  : program membuat kotak dengan inputan
# bertipe string dan juga integer.
## Definisi Fungsi ##

# fungsi menu
def menu():
    print("Program membuat kotak")
    print("Selamat mencoba")
    print("Silakan masukan karakter dan integer !")
    return

# fungsi input karakter
# Kamus lokal
# c : var.input (str)
def inputKar ():
    c = str(input("masukan satu karakter :"))
    return (c)

# fungsi input integer
# Kamus lokal
# n : var. input (int)
def inputInt():
    n = int(input("masukan nilai integer :"))
    while(n <= 0): 
        n = int(input("masukan nilai integer : "))
    return (n)

# fungsi keluaran
# Kamus lokal
# i : var. pendendali loop (int)
# j : var. pengendali loop2 (int)
# c : var. simpanan fungsi input sblmnya(str)
# n : var. parameter fungsi(int)

def keluaran(c,n):
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            if(i==1)or(j==1)or(i==n)or(j==n):
                print(c,end=" ")
            else:
                print(" ",end=" ")
        print()
    return

## Program utama ##
# Kamus lokal
# x : var. menyimpan input (str)
# y : var. menyimpan input (int)
def main():
    menu()
    x = inputKar()
    y = inputInt()
    keluaran(x,y)  
    
if __name__ == '__main__':
    main()