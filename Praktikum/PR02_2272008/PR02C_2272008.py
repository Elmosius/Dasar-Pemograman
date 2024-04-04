# File : PR02C_2272008.py
# Code Clothing
# Program untuk membantu penjualan di sebuah toko Code Clothing
# ---- Kamus Data ----
# jenis_pakaian, pilihan_pakaian, ukuran_pakaian (str)
# harga_pakaian, uang_dibayarkan (int)
# menggunakan operasi Boolean (and) 
# menggunakan operasi Perbandingan (==) 
# menggunakan kondisi (if, elif)

def main():

    # program awal jenis pakaian 
    print("="*50)
    jenis_pakaian = str(input("Jenis Pakaian(kaos/kemeja/jaket) : "))

    if(jenis_pakaian == "jaket"):
        bahan_pakaian = "berbahan "
        pilihan_pakaian = str(input("Bahan jaket(b. baby terry, d. denim, t. Taslan): "))

    elif(jenis_pakaian == "kemeja"):
        bahan_pakaian = "bermotif "
        pilihan_pakaian = str(input("Motif kemeja(k. kotak-kotak, p. Polos): "))
        
    elif(jenis_pakaian == "kaos"):
        bahan_pakaian = "bewarna "
        pilihan_pakaian = str(input("Warna kaos(m. maroon, n. navy, dan l. lilac): "))

    ukuran_pakaian = str(input("Ukuran Pakaian(s/m/l): "))

    print("="*50)
    # program barang yang dibeli
    print("Barang yang dibeli: ")
    print("1", jenis_pakaian, bahan_pakaian, end="")

    # program pilihan warna motif bahan
    if(pilihan_pakaian == "b"):
        print("baby terry berukuran", ukuran_pakaian)
    elif(pilihan_pakaian == "d"):
        print("denim berukuran", ukuran_pakaian)
    elif(pilihan_pakaian == "t"):
        print("taslan berukuran", ukuran_pakaian)   
    elif(pilihan_pakaian == "k"):
        print("kotak-kotak berukuran", ukuran_pakaian)
    elif(pilihan_pakaian == "p"):
        print("polos berukuran", ukuran_pakaian)
    elif(pilihan_pakaian == "m"):
        print("maroon berukuran", ukuran_pakaian)
    elif(pilihan_pakaian == "n"):
        print("navy berukuran", ukuran_pakaian)
    elif(pilihan_pakaian == "l"):
        print("lilac berukuran", ukuran_pakaian)
    
    # program harga
    if(jenis_pakaian == "kaos" and ukuran_pakaian == "s"):
        harga_pakaian = (70000)
    elif(jenis_pakaian == "kaos" and ukuran_pakaian == "m"):
        harga_pakaian = (70000)*0.2 + 70000
    if(jenis_pakaian == "kaos" and ukuran_pakaian == "l"):
        harga_pakaian = (70000)*0.4 + 70000
    elif(jenis_pakaian == "kemeja" and ukuran_pakaian == "s"):
        harga_pakaian = (100000)
    elif(jenis_pakaian == "kemeja" and ukuran_pakaian == "m"):
        harga_pakaian = (100000)*0.2 + 100000
    elif(jenis_pakaian == "kemeja" and ukuran_pakaian == "l"):
        harga_pakaian = (100000)*0.4 + 100000
    elif(jenis_pakaian == "jaket" and ukuran_pakaian == "s"):
        harga_pakaian = (150000)
    elif(jenis_pakaian == "jaket" and ukuran_pakaian == "m"):
        harga_pakaian = (150000)*0.2 + 150000
    elif(jenis_pakaian == "jaket" and ukuran_pakaian == "l"):
        harga_pakaian = (150000)*0.4 + 150000     
 
    print("Harga: Rp.", int(harga_pakaian))

    # program kasir
    print("="*50)
    uang_dibayarkan = int(input("Uang yang dibayarkan: Rp. "))
    print("Kembalian: Rp. ",int(uang_dibayarkan - harga_pakaian))
    print("="*50)

if __name__ == '__main__':
    main()         