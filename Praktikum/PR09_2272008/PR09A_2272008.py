# File : PR09A_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang menerima N bilangan 
# bulat lalu akan menampilkan bilangan kedua terkecil.5
## Definisi Fungsi ##

## Program Utama ##
# Kamus Lokal
# N : var. input banyaknya loop(int)
# a : var. array(int)
# i : var. parameter(int)
# m1 : var. isi array urutan 0(int)
# m2 : var. isi array urutan 1(int)

def main():
    # inisial
    N = int(input(""))
    a = N * [None]
    
    # proses
    for i in range(0,N,1):
        a[i] = int(input(""))
        
    m1= a[0]
    m2 = a[1]
    if(m1 > m2):
        m1 = a[1]
        m2 = a[0]
            
    for i in range(2,N,1):
        if(a[i] < m1):
            m2 = m1
            m1 = a[i]
        elif(a[i] < m2):
            m2 = a[i]
    
    # output
    print(m2)
    
if __name__ == '__main__':
    main()