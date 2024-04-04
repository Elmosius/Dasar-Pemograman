# File : Kuis3-no1.py
# Penulis : Elmosius Suli

def printGanjil(arr):
    for i in range(0,N,1):
        if(arr[i] % 2 != 0):
            print(arr[i], end=" ")
    print()
    

def getGenap(arr):
    arrGenap = N * [None]
    for i in range(0,N,1):
        if(arr[i] % 2 == 0):
            arrGenap[i] = arr[i]
            
    return(arrGenap)
    
def sum(arr):
    total = 0
    for i in range(0,N,1):
        total += arr[i]
        
    return(total)
    
def sumPrint(arr):
    total = 0
    for i in range(0,N,1):
        total += arr[i]
        
    print("Fungsi sumPrint :", total)
    
def main():
    # input
    for i in range (0,N,1):
        arr[i] = int(input())
        
    print("Ganjil")
    printGanjil(arr)  
    
    print("Genap")
    arrGenap = getGenap(arr)
    for i in range(0,N,1):
        if(arrGenap[i] != None):
            print(arrGenap[i], end=" ")
            
    
    print("Sum arr")
    print(sum(arr))
    sumPrint(arr)
    
if __name__ == '__main__':
    global N,arr
    N = int(input("N : "))
    arr = N * [None]
    
    main()
