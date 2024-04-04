# File : PR02B_2272008.py
# Toko Buah
# Program yang akan menghitung total buah serta total harga buah berdasarkan input user
# ---- Kamus Data ----
# buah (str)
# jumlah_alpukat, jumlah_apel, dan jumlah_jeruk (int)
# menggunakan operasi perbandingan (==)
# menggunakan kondisi (if, elif)

def main():
    #inisialisasi
    apel = 0 
    alpukat = 0
    jeruk = 0

    # program proses pertama
    buah = str((input("Buah (Alpukat/Apel/Jeruk) :")))
    
    if(buah == "Alpukat"):
        jumlah_alpukat = int((input("Jumlah Alpukat (kg) :")))
        alpukat = alpukat + jumlah_alpukat
    elif(buah == "Apel"):
        jumlah_apel = int((input("Jumlah Apel (kg) :")))
        apel += jumlah_apel    
    elif(buah == "Jeruk"):
        jumlah_jeruk = int((input("Jumlah Jeruk (kg) :")))
        jeruk += jumlah_jeruk
    print("="*35)

    # program proses kedua
    buah = str((input("Buah (Alpukat/Apel/Jeruk) :")))
    
    if(buah == "Alpukat"):
        jumlah_alpukat = int((input("Jumlah Alpukat (kg) :")))
        alpukat = alpukat + jumlah_alpukat
    elif(buah == "Apel"):
        jumlah_apel = int((input("Jumlah Apel (kg) :")))
        apel += jumlah_apel    
    elif(buah == "Jeruk"):
        jumlah_jeruk = int((input("Jumlah Jeruk (kg) :")))
        jeruk += jumlah_jeruk
    print("="*35)

    # program proses ketiga
    buah = str((input("Buah (Alpukat/Apel/Jeruk) :")))
    
    if(buah == "Alpukat"):
        jumlah_alpukat = int((input("Jumlah Alpukat (kg) :")))
        alpukat = alpukat + jumlah_alpukat
    elif(buah == "Apel"):
        jumlah_apel = int((input("Jumlah Apel (kg) :")))
        apel += jumlah_apel    
    elif(buah == "Jeruk"):
        jumlah_jeruk = int((input("Jumlah Jeruk (kg) :")))
        jeruk += jumlah_jeruk
    print("="*35)

    # jumlah total akhir
    print("Jumlah Buah Alpukat : ", alpukat,"kg")
    print("Jumlah Buah Apel : ", apel,"kg")
    print("Jumlah Buah Jeruk : ", jeruk,"kg")
    print("Total Jumlah Buah yaitu", (apel+jeruk+alpukat),"kg")
    print("Total Harga Buah Rp", (apel)*35000 + (jeruk)*20000 + (alpukat)*40000)

if __name__ == '__main__':
    main()         