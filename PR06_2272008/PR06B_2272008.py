# File : PR06B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program menginput n sebagai inputan bil. bulat   
# dan menampilkan deretan angka bil. prima 
# Kamus Data :
# angka : var. input(int)
# u : var. urutan(int)
# c : var. pengecheckan(Boolean)
# j : var. counter loop(int)
# i : var. parameter loop(int)

def main():
    # inisialisasi
    u = 0
    i = 2
        
    # input
    angka = int(input("Masukkan bilangan : "))

    # proses 
    print("===========================\n"
    "Bilangan prima yang didapat : ")
    while u < angka:
        c = True
        for j in range (2, i, 1):
            if i % j == 0:
                c = False
                break
    # output        
        if c:
            print(i, end=" ")
            u += 1
        i += 1
    
if __name__ == '__main__':
    main()