# File : PR03C_2272008.py
# Program Cafe Code
# program yang akan memberikan struk dari pesanan yang diinput
# oleh user dari berbagai tempat minuman yang disediakan.
# berdasarkan masukan yang berikan oleh user.
# ---- Kamus Data ----
# nama : var. input nama (str)
# tempat : var. input tempat (int)
# menu : var. input menu (int)
# ukuran : var. input ukuran (int)
# pm : var. print menu (str)
# pu : var. print ukuran (str)
# ph : var. print harga (int)
# pkv : var. print kode voucher (int)

def main():
     
     # Perintah Input dan Tampilan Awal
     nama = input("Nama pemesan: ")
     print("=======================")
     print("1. Mixu")
     print("2. Moonbucks")
     print("=======================")

     tempat = int(input("Silahkan Pilih Tempat: "))

     # Proses Mixu
     if(tempat == 1):
        print("Selamat datang di Mixu")

        print("======== Menu =========")
        print("1. Creamy mango Boba")
        print("2. Boba Sundae")
        print("3. Fresh Squeezed Lemonade")
        menu = int(input("Silahkan pilih menu: "))

        print("======= Ukuran ======== ")
        if(menu == 1):
            pm = "Creamy mango Boba"
            print("1. Unyu - 20000")
            print("2. Medium - 22000")
            print("3. Large - 24000")
            
            ukuran = int(input("Mau ukuran apa: "))
            print("=======================")
            if(ukuran == 1):
                pu = "Unyu"
                ph = 20000
            elif(ukuran == 2):
                pu = "Medium"
                ph = 22000
            elif(ukuran == 3):
                pu = "Large"
                ph = 24000      

        elif(menu == 2):
            pm = "Boba Sundae"
            print("1. Unyu - 14000")
            print("2. Medium - 16000")
            print("3. Large - 18000")

            ukuran = int(input("Mau ukuran apa: "))
            print("=======================")

            if(ukuran == 1):
                pu = "Unyu"
                ph = 14000
            elif(ukuran == 2):
                pu = "Medium"
                ph = 16000
            elif(ukuran == 3):
                pu = "Large"
                ph = 18000

        elif(menu == 3):
            pm = "Fresh Squeezed Lemonade"
            print("1. Unyu - 8000")
            print("2. Medium - 10000")
            print("3. Large - 12000")

            ukuran = int(input("Mau ukuran apa: "))
            print("=======================")

            if(ukuran == 1):
                pu = "Unyu"
                ph = 8000
            elif(ukuran == 2):
                pu = "Medium"
                ph = 10000
            elif(ukuran == 3):
                pu = "Large"
                ph = 12000

        kv = input("Masukkan kode voucher: ")
        if(kv == "ILOVEMIXU"):
            print("Kode voucher benar !!")
            pkv = 5000
        else:
            print("Kode voucher salah !!")
            pkv = 0

        print("===== Pesanan Mixu =====")
        print("Nama: ", nama)
        print("Pesanan: ", pm)
        print("Ukuran: ", pu)
        print("Harga: ", ph)
        print("PPN: ", int(0.1*ph) )
        print("Potongan: ", pkv)
        print("Total: ", int(ph+(0.1*ph)-pkv))
        print("=======================")
        

    # Proses Moonbucks
     if(tempat == 2):
        print("Selamat datang di Moonbucks")

        print("======== Menu =========")
        print("1. Asian Dolce Latte")
        print("2. Caramel Java Chip")
        print("3. Mango Passion Fruit")
        menu = int(input("Silahkan pilih menu: "))

        print("======= Ukuran ======== ")
        if(menu == 1):
            pm = "Asian Dolce Latte"
            print("1. Tall - 53000")
            print("2. Grande - 58000")
            print("3. Venti - 60000")
            
            ukuran = int(input("Mau ukuran apa: "))
            print("=======================")
            if(ukuran == 1):
                pu = "Tall"
                ph = 53000
            elif(ukuran == 2):
                pu = "Grande"
                ph = 58000
            elif(ukuran == 3):
                pu = "Venti"
                ph = 60000      

        elif(menu == 2):
            pm = "Caramel Java Chip"
            print("1. Tall - 58000")
            print("2. Grande - 63000")
            print("3. Venti - 67000")

            ukuran = int(input("Mau ukuran apa: "))
            print("=======================")

            if(ukuran == 1):
                pu = "Tall"
                ph = 58000
            elif(ukuran == 2):
                pu = "Grande"
                ph = 63000
            elif(ukuran == 3):
                pu = "Venti"
                ph = 67000

        elif(menu == 3):
            pm = "Mango Passion Fruit"
            print("1. Tall - 45000")
            print("2. Grande - 49000")
            print("3. Venti - 52000")

            ukuran = int(input("Mau ukuran apa: "))
            print("=======================")

            if(ukuran == 1):
                pu = "Tall"
                ph = 45000
            elif(ukuran == 2):
                pu = "Grande"
                ph = 49000
            elif(ukuran == 3):
                pu = "Venti"
                ph = 52000

        kv = input("Masukkan kode voucher: ")
        if(kv == "MOONBUCKSUWU"):
            print("Kode voucher benar !!")
            pkv = 20000
        else:
            print("Kode voucher salah !!")
            pkv = 0

        print("===== Pesanan Moonbucks =====")            
        print("Nama: ", nama)
        print("Pesanan: ", pm)
        print("Ukuran: ", pu)
        print("Harga: ", ph)
        print("PPN: ", int(0.1*ph) )
        print("Potongan: ", pkv)
        print("Total: ", int(ph+(0.1*ph)-pkv))
        print("=======================")      

if __name__ == '__main__':
    main() 