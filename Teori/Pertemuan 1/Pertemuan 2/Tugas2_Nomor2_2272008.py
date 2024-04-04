# File: Tugas2_Nomor2_2272008.py
# Penulis : Elmosius Suli
# Program membaca nama dan data tanggal, bulan, tahun kadaluwarsa dari suatu makanan instan.
# Kamus Data
# nama_barang (str)
# Tanggal, Bulan, Tahun, tanggal_hari_ini, bulan_ini, dan tahun_ini (int)
# menggunakan operasi perbandingan (==, !=) 
# menggunakan operasi boolean (and dan or)  

def main ():
                
# Program

    # kadaluarsa
    nama_barang = str(input("Nama barang: "))
    tanggal = int(input("Tanggal: "))
    bulan = int(input("Bulan: "))
    tahun = int(input("Tahun: "))

    print("-"*30)
    
    # tanggal hari ini
    print("Tanggal hari ini:")
    tanggal_hari_ini = int(input("Tanggal: "))
    bulan_ini = int(input("Bulan: "))
    tahun_ini = int(input("Tahun: "))

    # perhitungan hari bulan tahun
    
    if((bulan_ini == bulan) and (tahun == tahun_ini)):
        print(nama_barang, "akan kadaluwarsa", (tanggal- tanggal_hari_ini), "hari lagi.")

    elif(tahun >= tahun_ini):
            
            if(bulan == 2):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 1), "hari lagi.")
            elif((bulan == 3) and (bulan_ini == 2)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 +(bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal - 2), "hari lagi.")  
            elif((bulan == 3) and (bulan_ini == 1)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal - 1), "hari lagi.")  

            elif((bulan == 4 or bulan == 5) and (bulan_ini == 3)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 1), "hari lagi.")
            elif((bulan == 4 or bulan == 5) and (bulan_ini == 2)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal - 1), "hari lagi.") 
            elif((bulan == 4 or bulan == 5) and (bulan_ini == (1 or 4))):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal), "hari lagi.")            

            elif((bulan == 6 or bulan == 7) and (bulan_ini == (5 or 4))):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 1), "hari lagi.")
            elif((bulan == 6 or bulan == 7) and (bulan_ini == 3)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 2), "hari lagi.") 
            elif((bulan == 6 or bulan == 7) and (bulan_ini == 2)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal), "hari lagi.")
            elif((bulan == 6 or bulan == 7) and (bulan_ini == 1)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 1 ), "hari lagi.")                   

            elif((bulan == 8) and (bulan_ini == (7 or 6))):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 1 ), "hari lagi.")
            elif((bulan == 8) and (bulan_ini == (5 or 4))):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 2), "hari lagi.") 
            elif((bulan == 8) and (bulan_ini == 3)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 3), "hari lagi.")
            elif((bulan == 8) and (bulan_ini == 2)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 1), "hari lagi.")  
            elif((bulan == 8) and (bulan_ini == 1)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 2), "hari lagi.")                      

            elif((bulan == 9 or bulan == 10) and (bulan_ini == (7 or 6))):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 2 ), "hari lagi.")
            elif((bulan == 9 or bulan == 10) and (bulan_ini == (5 or 4))):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 3), "hari lagi.") 
            elif((bulan == 9 or bulan == 10) and (bulan_ini == 3)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 4), "hari lagi.")
            elif((bulan == 9 or bulan == 10) and (bulan_ini == 2)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 2), "hari lagi.")  
            elif((bulan == 9 or bulan == 10) and (bulan_ini == 1)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 3), "hari lagi.") 
            elif((bulan == 9 or bulan == 10) and (bulan_ini == 8)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 1), "hari lagi.")                          

            elif((bulan == 11 or bulan == 12) and (bulan_ini == (10 or 9))):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 1 ), "hari lagi.")
            elif((bulan == 11 or bulan == 12) and (bulan_ini == (7 or 6 ))):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 3), "hari lagi.") 
            elif((bulan == 11 or bulan == 12) and (bulan_ini == (5 or 4 ))):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 4), "hari lagi.")            
            elif((bulan == 11 or bulan == 12) and (bulan_ini == 3)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 5), "hari lagi.")  
            elif((bulan == 11 or bulan == 12) and (bulan_ini == 2)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 3), "hari lagi.")               
            elif((bulan == 11 or bulan == 12) and (bulan_ini == 8)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 2), "hari lagi.")
            elif((bulan == 11 or bulan == 12) and (bulan_ini == 1)):
                print(nama_barang, "akan kadaluwarsa",((tahun-tahun_ini)*365 + (bulan-bulan_ini)*30 - tanggal_hari_ini + tanggal + 4), "hari lagi.") 

    else:
        print(nama_barang,"barang sudah lewat kaluwarsa.")

      

    print("-"*30)

    
if __name__ == '__main__':
    main()