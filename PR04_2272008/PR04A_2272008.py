# File : PR04A_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menampilkan deret m 
# angka dimulai dari n dengan kelipatan x.
# Kamus Data :
# awal : var. input n (int)
# jmlh : var. input m (int)
# x : var. input kelipatan (int)
# total : var. menyimpan slruh deret (int)
# i : var. dalam for 

def main():
    # Inisialisasi
    total = 0

    # Input
    awal = int(input("n: "))
    jmlh = int(input("m: "))
    x = int(input("x: "))

    # Proses dan Output
    print("Deret",jmlh,"angka, dimulai dari", 
    awal, "dengan kelipatan", x)
   
    for i in range (jmlh): 
        if(i == jmlh-1):
            print(awal)
        else:
            print(f"{awal},",end=" ")
        total += awal    
        awal += x
         
    print("Total seluruh deret adalah",total)
    print("Rata-rata deret adalah", (total//jmlh))

if __name__ == '__main__':
    main()