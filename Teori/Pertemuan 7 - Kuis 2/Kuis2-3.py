# File : Kuis2-3.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima sebuah bilangan bulat A
# lalu akan menampilkan tulisan O berukuran A seperti pada contoh
# Kamus Data
# n : var. input A (int)
# i : var. counter loop dan menentukan baris (int)
# j : var. counter loop2 dan menentukan kolom (int)
# x : var. pengurangan di diagonal (int)
def main ():
   
    # input
    n = int(input("A : "))
    x = n
    # proses dan output
    
    for i in range(1,n+1,1):
        for j in range (1, n+1, 1):
            if(i == 1):
                if(n % 2 == 0):
                    if((j % 2 == 0)):
                        print(n , end=" ")
                    else:
                        print("@ ", end=" ")
                else: 
                    if(j % 2 != 0):
                        print(n , end=" ")
                    else:
                        print(" @ ", end=" ")        
            elif(i == n):
                if(n % 2 == 0):
                    if(j % 2 == 0):
                        print((n*0)+1 ,  end=" ")
                    else:
                        print("@ ", end=" ")
                else: 
                    if(j % 2 != 0):
                        print((n*0)+1 ,  end=" ")
                    else:
                        print(" @ ", end=" ")
                    
            else:
                if(n % 2 == 0):
                    if(j == 1):
                        print("@ ", end=" ")
                    elif(j == n):
                        print(" @ ", end=" ")
                    elif(i == j):
                        print(x-1, end=" ")
                        x-=1    
                    else:
                        print(" ", end=" ")
                else:
                    if(j == 1):
                        print("@ ", end=" ")
                    elif(j == n):
                        print(" @ ", end=" ")
                    elif(i == j):
                        print(x-1 , end=" ")
                        x-=1    
                    else:
                        print("  ", end=" ")
                
        print()
if __name__ == "__main__":
    main()
