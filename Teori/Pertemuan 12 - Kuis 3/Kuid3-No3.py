# File : Kuis3-No3.py
# Penulis : Elmosius Suli
# Tujuan :  program yang menerima N bilangan bulat lalu 
# akan menampilkan semua bilangan ganjil
## Definisi Fungsi ##

def main():
    N = int(input("N: "))
    arrA = N * [None]
    
    for i in range(0,N,1):
        arrA[i] = int(input(""))
        
    for j in range(0,N,1):
        if ((arrA[j] % 2) == 1):
            print(arrA[j],end=" ")
             
if __name__ == '__main__':
    main()
    
