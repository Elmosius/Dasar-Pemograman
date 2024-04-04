# File : PR011B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima input satu 
# bilangan decimal kemudian program akan
# menampilkan biner dari decimal tersebut.
## Definisi Fungsi ##

# Fungsi printBinary
# Kamus Lokal
# j : var. index(int)
# hasil : var. simpan hasil biner(int)
# X : var. parameter(int)
# i : var. parameter(int)

def printBinary(X):
    arrA = 9 * [None]
    j = 0
    
    for i in range(8,-1,-1):
        hasil = 2**i
        if (hasil > X):
            arrA[j] = 0
        else:
            X-= hasil
            arrA[j] = 1
        j+=1
   
    for i in range(0,9,1):
        print(arrA[i], end=" ")
        
def main():
    # input 
    X = int(input(""))    
    printBinary(X)
    
  
if __name__ == '__main__':
    main()