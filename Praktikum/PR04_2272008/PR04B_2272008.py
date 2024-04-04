# File : PR04B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menampilkan deret 
# fibbonaci sebanyak n
# Kamus Data :
# bk : var. input  (int)
# a : var. pertama (int)
# b : var. kedua (int)
# c : var. pertambahan (int)
# i : var. dalam for 

def main():

    # Inisialisasi
    a = 0
    b = 1
    
    # Input
    bk = int(input("n: "))

    # Proses dan output
    for i in range (bk):
        print(a, end=" ")
        c = a + b
        a = b 
        b = c

if __name__ == '__main__':
    main()