# File : PR13B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima masukan N 
# buah bilangan dan string mode lalu akan 
# menampilkan N bilangan tersebut secara terurut menaik 
# atau menurun berdasarkan mode tersebut.
## Definisi Fungsi ##

## Program Utama ##
# Kamus Lokal
# N : var. input(int)
# i : var. parameter(int)
# j : var. parameter(int)
# arrA : var.array A (int)
# mode : var. menentukan menaik atau menurun(str)
# tem : var. untuk pertukaran data(int)
# imax : var. indeks dimana A[imax] berisi nilai trbsar(intx)

def main():
    N = int(input(""))
    arrA= N * [None]
    
    for i in range(0,N,1):
        arrA[i] = int(input())
    
    mode= str(input(""))
    
    if (mode == "menurun" or mode == "Menurun"):
        
        for i in range(0,N-1,1):
            imax = i
            for j in range(i+1,N,1):
                if(arrA[j] > arrA[imax]):
                    imax = j
            tem = arrA[i]
            arrA[i] = arrA[imax]
            arrA[imax] = tem
    else:
        for i in range(0,N-1,1):
            imax = i
            for j in range(i+1,N,1):
                if(arrA[j] < arrA[imax]):
                    imax = j
            tem = arrA[i]
            arrA[i] = arrA[imax]
            arrA[imax] = tem
        
    for i in range(0,N,1):
        print(arrA[i], end=" ")

if __name__ == '__main__':
    main()