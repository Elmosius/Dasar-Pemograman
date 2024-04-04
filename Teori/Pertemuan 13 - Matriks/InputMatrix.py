# File : InputMatrix.py
# Program mengisi matriks
# Kamus Data
# MM : var. utk matriks (matriks of integer)
# i : var. indeks baris (integer)
# j : var. indeks kolom (integer)
# n : var. banyaknya baris (integer)
# m : var. banyaknya kolom (integer)
def main():
    n = int(input("Jumlah baris matriks :"))
    m = int(input("Jumlah kolom matriks :"))
    
    #deklarasi matriks
    MM = n*[None] 
    for i in range(0,n,1):
        MM[i] = m*[None]
    
    #Input MM[i][j]
    for i in range (0,n,1): 
        for j in range (0,m,1):
            print ("MM[",i,",",j,"]:", end = " ")
            MM[i][j] = int(input())
    
    #Print isi MM[i][j]
    print("Matriks hasil")
    for i in range (0,n,1):
        for j in range (0,m,1):
            print (MM[i][j], end = " ")
        print()
        
if __name__ == '__main__':
    main()