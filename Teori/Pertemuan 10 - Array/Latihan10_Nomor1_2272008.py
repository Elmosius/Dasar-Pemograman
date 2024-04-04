# File : Latihan10_Nomor1_2272008.py
# Penulis : Elmosius Suli
## Definisi Fungsi ##

def main():
    # --- proses mengisi array
    N = 5
    A = N* [None] # deklarasi array
    for i in range (0,N,1):
        A[i] = int(input("Nilai x :"))
    
    # --- proses 
    temp = A[0]
    for i in range (0,N-1,1):
        A[i] = A[i+1]
    A[N-1] = temp
    
    # --- proses menampilkan isi array
    for i in range (0,N,1):
        print ("A[",i,"] = ", A[i])
    
if __name__ == '__main__':
    main()
    
# input 3,4,5,6,7
# output 
# A[ 0 ] =  4
# A[ 1 ] =  5
# A[ 2 ] =  6
# A[ 3 ] =  7
# A[ 4 ] =  3