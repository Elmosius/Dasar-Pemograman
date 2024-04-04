# File : PR04C_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program aplikasi Go-Now 
# Kamus Data :
# jumlah_penumpang : var. menentukan pengulangan (int)
# p : var. input jarak (str)
# tj : var. titik jauh (float)
# jp : var. jarak pendek (float)
# jj : var. jarak jauh (float)
# i : var. dalam for 

def main():
    # Inisialisasi
    p = "|  "
    tj = 0
    jp = 0
    jj = 0
    np = " "
    nj = " "

    # Input
    jumlah_penumpang = int(input("Jumlah Penumpang : "))
    
    # Proses dan output
    print("====================================")
    nama = str(input("Nama : "))
    tujuan = str(input("Tujuan : "))
    jarak = float(input("Jarak tempuh (km) : "))
    print("====================================")
    jp = jarak
    jj = jarak
    np = tujuan
    nj = tujuan
    tj += jarak
    p += tujuan + "  |  "

    for i in range (jumlah_penumpang -1):
        nama = str(input("Nama : "))
        tujuan = str(input("Tujuan : "))
        jarak = float(input("Jarak tempuh (km) : "))
        print("====================================")
        p += tujuan + "  |  "
       
        tj += jarak
        
        if(jarak < jp ):
            jp = jarak
            np = tujuan
        elif(jarak > jj): 
            jj = jarak   
            nj = tujuan      

    ## Summary
    print(" ")
    print("==========================")
    print("SUMMARY HARI INI")
    print("==========================")
    print("Total Customer : ", jumlah_penumpang)

    ## Rute
    print(" ")
    print("Rute Hari ini : ")
    print(p)
    print("============================")
    print("Total jarak perjalanan hari ini :{:.2f}".format(tj))
    print("Perjalanan dengan jarak terdekat : ", 
    jp ,"menuju",np)
    print("Perjalanan dengan jarak terjauh :", 
    jj, "menuju",nj)
    
if __name__ == '__main__':
    main()