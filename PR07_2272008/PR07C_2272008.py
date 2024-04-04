# File : PR07C_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yg akan meminta input bilangan
# dimana program akn mengecek apakah bilangan palindrom, 
# bil. kdrat, dan knversi ke angka biner. Ketiga printh tadi 
# akan diletakkan ke dalam fungsi seperti pda tabel di bawah

# fungsi palindrome
# Kamus Lokal
# x : var. parameter (int)
# a1 : var. angka urutan pertama (int)
# a2 : var. angka urutan ketiga (int)
# p : var. mengechek (boolean)

def isPalindrome(x):
    p = True
    
    if (x >= 100):
        a1 = x // 100
        a2 = x % 10
    
        if ((a1 != a2)):
            p = False
        
    elif(x >= 10):
        if(x % 11 != 0):
            p = False   
    if p:
        print(x,"adalah bilangan palindrom")
    else:
        print(x,"bukan merupakan bilangan palindrom")

# fungsi square
# Kamus Lokal
# x : var. parameter & yang ingin dibagi(int)
# i : var. counter loop & menentukan akar(int)

def isSquare(x):
    for i in range (1,x+1,1):
        if (x  / i == i):
            print(x,"adalah bilangan kuadrat", 
            "dengan akarnya adalah",i)
            break
    else:
        print(x,"bukan bilangan kuadrat")
        
# fungsi biner
# Kamus Lokal
# x : var. parameter(int)
# n : var. paramater loop (int)
# biner : var. perkalian untuk biner (int)
# hasil : var. hasil perpangkatan biner (int)

def convertBinary(x):
    n = 0
    biner = 2
   
    for i in range(7,n-1,-1):
        hasil = biner**i
        if (hasil > x):
            print ('0', end=" ")
        else:
            x-= hasil
            print ('1', end=" ")  
    print()    
        
## Program Utama ##
# Kamus Lokal 
# angka : var. input (int)
def main():
    # input
    
    angka = int(input("N: "))
   
    while(angka != 999):
        while(not (angka > 0 and angka < 129)):
            print("Angka harus 0 < x < 129")
            angka = int(input("N: "))
        
        isPalindrome(angka)
        isSquare(angka)
        print('Angka biner dari',angka,':')
        convertBinary(angka)
        print("="*50)
        angka = int(input("N: ")) 
    print("Program selesai")    
         
if __name__ == '__main__':
    main()