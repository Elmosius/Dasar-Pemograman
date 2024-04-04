# File : PR011C_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang kosakata yang akan meminta user 
# untuk memasukan 10 buah huruf. 
## Definisi Fungsi ##

# Fungsi cariKata
# Kamus Lokal
# arrKata : var. array parameter(str)
# arrDigitAngka : var. array parameter(str)
# arrA : var. arrayA(str)
# i : var. parameter (int)
def cariKata(arrKata, arrDigitAngka):
    global Nmax,t
    
    arrA = Nmax * [None] 
    
    for i in range(0,t,1):
        arrA[i]= ""
        for j in arrDigitAngka[i]:
            arrA[i]+= arrKata[int(j)]
            
    return(arrA)

## Program Utama ##
# Kamus Lokal
# i : var. parameter(int)
# j : var.p parameter(int)
# arrK : var. array Kata (str)
# arrD : var. array DigitAngka (str)
# arrC : var. array Kata(str)

def main():
    global t
    
    # input 
    arrK = 10 * [None]

    for i in range(0,10,1):
        arrK[i] = str(input(""))
    
    arrD = Nmax * [None]
    arrD[t] = ""
    
    arrD[t] = str(input("5 digit angka: "))
    while (arrD[t] != '99999'):
        t += 1
        arrD[t] = str(input("5 digit angka: "))
    
    # output
    print("Kata yang telah dibuat:")
    arrC = cariKata(arrK, arrD)
    
    for j in range (0,t,1):
        if(j==0):
            print(arrC[j],end="")
        else:
            print(",",arrC[j],end="")
        
if __name__ == '__main__':
    # Global t, Nmax
    # t : var. total arrD(int)
    # Nmax : var. kapasitas array(int)
    Nmax = 100
    t = 0
    main()