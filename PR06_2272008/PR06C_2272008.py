# File : PR06C_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima sebuah bil. bulat
# lalu menampilkan jajaran segitiga berukuran N sebanyak 2*N
# restoran yang disediakan. 
# Kamus Data :
# n : var. input untuk loop (int)
# i : var. counter loop buat baris(int)
# j : var. counter loop2 buat kolom(int)
# k : var. counter loop3 buat pola(int)


def main():
   
    # input
    n = int(input(""))

    # proses dan output
    for i in range (0,n,1):
        for j in range(0,n,1):
            if ((i % 2) == 0):
                for k in range(0,n,1):
                    print("*", end=" ")
            else:
                print("*", end=" ")
                for k in range(0,n-2,1):
                    print(" ", end=" ")
                print("*", end=" ")
            print(end=" ")
        print()
        
if __name__ == '__main__':
    main()