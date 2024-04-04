# File : PR03B_2272008.py
# Program Kalender
# program yang akan mengubah format tanggal 
# berdasarkan masukan yang berikan oleh user.
# ---- Kamus Data ----
# tanggal : var. input tanggal (int)
# bulan : var. input bulan (int)
# tahun : var. input tahun (int)

def main():

    # Perintah Input
    tanggal = int(input("Tanggal :"))
    bulan = int(input("Bulan :"))
    tahun = int(input("Tahun :"))

    # Perintah Proses dan Output
    print("=====================")
    
    if(tahun % 4 != 0):
        if( 1 <= bulan <= 12 ):
            if(bulan == 1):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Januari",tahun)
                else:
                    print("Masukan salah, Tidak ada ",)  
            elif(bulan == 2):
                if(1 <= tanggal <= 28):
                    print(tanggal,"Febuari",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 3):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Maret",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)                     
            elif(bulan == 4):
                if(1 <= tanggal <= 30):
                    print(tanggal,"April",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)                
            elif(bulan == 5):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Mei",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 6):
                if(1 <= tanggal <= 30):
                    print(tanggal,"Juni",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)        
            elif(bulan == 7):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Juli",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 8):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Agustus",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 9):
                if(1 <= tanggal <= 30):
                    print(tanggal,"September",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)                           
            elif(bulan == 10):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Oktober",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 11):
                if(1 <= tanggal <= 30):
                    print(tanggal,"November",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)               
            elif(bulan == 12):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Desember",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)        
        else:
            print  ("Masukan salah, Tidak ada bulan",bulan,".")
    else:
        if( 1 <= bulan <= 12 ):
            if(bulan == 1):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Januari",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)  
            elif(bulan == 2):
                if(1 <= tanggal <= 29):
                    print(tanggal,"Febuari",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 3):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Maret",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)                     
            elif(bulan == 4):
                if(1 <= tanggal <= 30):
                    print(tanggal,"April",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)                
            elif(bulan == 5):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Mei",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 6):
                if(1 <= tanggal <= 30):
                    print(tanggal,"Juni",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)        
            elif(bulan == 7):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Juli",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 8):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Agustus",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 9):
                if(1 <= tanggal <= 30):
                    print(tanggal,"September",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)                           
            elif(bulan == 10):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Oktober",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)     
            elif(bulan == 11):
                if(1 <= tanggal <= 30):
                    print(tanggal,"November",tahun) 
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)               
            elif(bulan == 12):
                if(1 <= tanggal <= 31):
                    print(tanggal,"Desember",tahun)
                else:
                    print("Masukan salah, Tidak ada tanggal",tanggal)        
        else:
            print  ("Masukan salah, Tidak ada bulan",bulan,".")

    return 0
        
if __name__ == '__main__':
    main() 