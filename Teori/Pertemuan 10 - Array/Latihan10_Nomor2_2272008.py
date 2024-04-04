# File : Latihan10_Nomor2_2272008.py
# Penulis : Elmosius Suli
## Definisi Fungsi ##

def main():
    # --- proses mengisi array
    N = 10
    A = N * [None] 
    for i in range (0,N,1):
        A[i] = int(input("Nilai x :"))
    
    # --- proses menampilkan isi array
    for i in range (N-1,-1,-1):
        print (A[i],end=" ")
    
if __name__ == '__main__':
    main()
    
# input : 1,2,3,4,5,6,7,8,9,10
# output : 
# 10 9 8 7 6 5 4 3 2 1