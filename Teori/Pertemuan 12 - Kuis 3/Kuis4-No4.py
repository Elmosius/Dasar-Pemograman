# File : Kuis3-No4.py
# Penulis : Elmosius Suli
# Tujuan :  program yang menerima N bilangan bulat lalu 
# akan menampilkan semua bilangan ganjil
## Definisi Fungsi ##

# fungsi sortDesc(arr)
# Kamus lokal

def sortDesc(arr):
    global arrA
    temp = 0
    
    for i in range(0,arr,1):
        for j in range(0,arr-1,1):
            if(arrA[j] < arrA[j+1]):
                temp = arrA[j]
                arrA[j] = arrA[j+1]
                arrA[j+1] = temp  
                
    for k in range(0,arr,1):
        print(arrA[k], end=" ")
        
def main():
    global arrA
    
    N = int(input("N: "))
    arrA = N * [None]
    
    for i in range(0,N,1):
        arrA[i] = int(input(""))
        
    sortDesc(N)

if __name__ == '__main__':
    main()
    
