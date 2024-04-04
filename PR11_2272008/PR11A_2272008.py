# File : PR011A_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima 
# masukan N buah bilangan lalu akan menampilkan bilangan yang 
# memiliki kelipatan 3, kelipatan 5, kelipatan 7, dan 
# kelipatan 11.
## Definisi Fungsi ##

# Fungsi printKelipatan3
# Kamus Lokal
# arr : var. parameter(int)
# arrA : var. array A (int)
# j : var. jumlah total kelipatan(int)
# i : var. parameter(int)

def printKelipatan3(arr):
    global N
    arrA = N * [None]
    j = 0
    for i in range(0,N,1):
        if(arr[i] % 3 == 0):
            arrA[j] = arr[i]
            j += 1               
    
    for i in range(0,j,1):
        if(arrA[i] != None):
            print(arrA[i], end=" ")
            if (j > 1):
                if (j > 2) and (i <= j-2):
                    print(",", end=" ")
                if (i == j-2):
                    print("dan", end=" ")
    print()
# Fungsi printKelipatan5
# Kamus Lokal
# arr : var. parameter(int)
# arrA : var. array A (int)
# j : var. jumlah total kelipatan(int)
# i : var. parameter(int)

def printKelipatan5(arr):
    global N
    arrA = N * [None]
    j = 0       
    for i in range(0,N,1):
        if(arr[i] % 5 == 0):
            arrA[j] = arr[i]
            j += 1

    for i in range(0,j,1):
        if(arrA[i] != None):
            print(arrA[i], end=" ")
            if (j > 1):
                if (j > 2) and (i <= j-2):
                    print(",", end=" ")
                if (i == j-2):
                    print("dan", end=" ")
    print()

# Fungsi printKelipatan7
# Kamus Lokal
# arr : var. parameter(int)
# arrA : var. array A (int)
# j : var. jumlah total kelipatan(int)
# i : var. parameter(int)

def printKelipatan7(arr):
    global N
    arrA = N * [None]
    j = 0   
    for i in range(0,N,1):
        if(arr[i] % 7 == 0):
            arrA[j] = arr[i]
            j += 1
            
    for i in range(0,j,1):
        if(arrA[i] != None):
            print(arrA[i], end=" ")
            if (j > 1):
                if (j > 2) and (i <= j-2):
                    print(",", end=" ")
                if (i == j-2):
                    print("dan", end=" ")
    print()
    
# Fungsi printKelipatan11
# Kamus Lokal
# arr : var. parameter(int)
# arrA : var. array A (int)
# j : var. jumlah total kelipatan(int)
# i : var. parameter(int)

def printKelipatan11(arr):
    global N
    arrA = N * [None]
    j = 0
    for i in range(0,N,1):
        if(arr[i] % 11 == 0):
            arrA[j] = arr[i]
            j += 1

    for i in range(0,j,1):
        if(arrA[i] != None):
            print(arrA[i], end=" ")
            if (j > 1):
                if (j > 2) and (i <= j-2):
                    print(",", end=" ")
                if (i == j-2):
                    print("dan", end=" ")
    print()
    
## Program Utama ##
# Kamus Lokal
# arrA : var. array(int)
# i : var. parameter(int)

def main():
    # input 
    arrA = N * [None]
    
    for i in range(0,N,1):
        arrA[i] = int(input(""))
    
    # output
    print("Kelipatan 3 itu ada", end=" ")
    printKelipatan3(arrA)
    
    print("Kelipatan 5 itu ada", end=" ")
    printKelipatan5(arrA)
    
    print("Kelipatan 7 itu ada", end=" ")
    printKelipatan7(arrA)
    
    print("Kelipatan 11 itu ada", end=" ")
    printKelipatan11(arrA)
   
                
if __name__ == '__main__':
    # Global N
    # N : var. input kapasitas array(int)
    N = int(input(""))
    
    main()