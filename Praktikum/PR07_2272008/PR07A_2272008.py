# File : PR07A_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menampilkan urutan abjad 
# hingga huruf e, dan mengulang lagi dari a sesuai
# dengan bilangan yang kita input secara berulang

# fungsi alphabet count
# Kamus Lokal
# a : var. print a (str)
# b : var. print b (str)
# c : var. print c (str)
# d : var. print d (str)
# e : var. print e (str)
# n : var. menentukan abjad (int)
# i : var. counter loop (int)
# x : var. parameter (int)

def alphabetCount(x):
    # inisialisasi
    n = 1
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    
    # proses
    for i in range(1,x+1,1):
        if(n == 1):
            print(a,end=" ")
        elif(n == 2):
            print(b,end=" ")
        elif(n == 3):
            print(c,end=" ")
        elif(n == 4):
            print(d,end=" ")
        else:
            print(e,end=" ")
        if (n == 5):
            n = 0    
        n+= 1
    print()

## Program Utama ##
# Kamus Lokal
# angka : var. input N (int)

def main():
    # input
    angka = int(input("N: "))
    
    # proses output
    while (angka!= 0):
        alphabetCount(angka)
        angka = int(input("N: "))
    print("Program selesai")

if __name__ == '__main__':
    main()