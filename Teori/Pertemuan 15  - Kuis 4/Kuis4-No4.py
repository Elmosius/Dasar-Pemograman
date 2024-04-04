# File : Kuis3-No4.py
# Penulis : Elmosius Suli

def matriks(d1,d2):
    arr = [None]*d1 
    for i in range(0,d1,1):
        arr[i] = [None]*d2
    
    return arr

def main():
    n = int(input("n : "))
    m = int(input("m :"))
    
    arrNM = matriks(n,m)

    
    for i in range (0,n,1):
        for j in range (0,m,1):
            print ("A[",i,",",j,"]:", end = " ")
            arrNM[i][j] = int(input("Nilai :" ))
            
    # matrik seblum putar
    for i in range(0,n,1):
        for j in range(0,m,1):
            print(arrNM[i][j], end=" ")
        print()
    print()
    
    # matrik sesudah putar
    for i in range(0,m,1):
        for j in range(n-1,-1,-1):
            print(arrNM[j][i], end=" ")
        print()
    
    
   
       
        
   

if __name__ == '__main__':
   
    
    main()
    
