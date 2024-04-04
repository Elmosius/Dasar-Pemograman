# File : PR06A_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program untuk membuat gambar hati 
# dengan panjang dan lebar sebnayak 2*n yang diinput
# Kamus Data :
# n : var. input(int)
# i : var. counter loop utama(int)
# j : var. counter loop2 spasi(int)
# k : var. counter loop3 bintang(int)
# l : var. counter loop4 pengulangan(int)

def main():
 
    # input
    n = int(input(""))
    
    # proses dan output
    ## segitiga pertama dan kedua
    if (n % 2 == 0):
        for i in range (0,(n)//2,1):
            for l in range (0,2,1):
                for j in range (0,((n)//2)-i-1,1):
                    print(' ', end=" ")
                for k in range (0,2*i+2,1):
                    print('💚', end="")
                for j in range (0,((n)//2)-i-1,1):
                    print(' ', end=" ")
            print()        
    else:
        for i in range (0,(n+1)//2,1):
            for l in range(0,2,1):
                for j in range (0,((n+1)//2)-i-1,1):
                    print(' ', end=" ")
                for k in range (0,2*i+1,1):
                    print('💚', end="")
                for j in range (0,((n+1)//2)-i-1,1):
                    print(' ', end=" ")
            print()
        
    ## segitiga ketiga 
    for i in range (0,n,1):
        for j in range (0,i,1):
            print(' ', end=" ")
        for k in range (0,(n-i)*2,1):
            print('💚', end="")
        print()
        
if __name__ == '__main__':
    main()