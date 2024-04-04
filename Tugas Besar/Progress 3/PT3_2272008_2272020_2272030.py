# File : PT3_2272008_2272020_2272030.py
# Penulis : Elmosius Suli, Joseph Adiwiguna, dan Samuel 
# Tujuan Program :  Membuat toko Bakery
## Definisi Fungsi ##

# fungsi tampilan awal
# Kamus Lokal :
# i = int (pengulangan for)
def tampilanawal():
        print("==================================")
        print()
        print("        ",end='')
        for i in range(0,5,1):
            print("*   ",end='')
        print()
        print("        ",end='')
        for i in range(0,5,1):
            print("|   ",end='')
        print()
        print("      *********************")
        for i in range (0,2,1):
            print("      *                   *")
        print("   ****************************")
        print("   *                          *")
        print("   *~~~~~~~ EJS BAKERY ~~~~~~~*")
        print("   *                          *")
        print("   ****************************")
        print("---------------------------------")
        print()
        


# fungsi login
# Kamus Lokal :
#

def login():
    print("0. Sign In")
    print("1. Sign Up")
    print()
    print("Jika belum memiliki akun, ketikan 1 untuk membuat akun")
    pilihan = int(input("Pilihan Anda : "))
    
    while (pilihan!= 0 and pilihan!= 1):
        pilihan = int(input("Pilihan Anda : "))
    
    print()
    if (pilihan == 0):
        signin()
    elif(pilihan == 1):
        signup()
## fungsi singin
# Kamus Lokal :
#
def signin():
    print('\t','='*25)
    print("\t\t| Sign In | ")
    print()
    username = str(input("\t Username/email : "))
    password = str(input("\t Password : "))
    
## fungsi singup
# Kamus Lokal :
#
def signup():
    print('\t','='*25)
    print("\t\t| Sign Up | ")
    print()
    username = str(input("\t Username/email\t: "))
    password = str(input("\t Password\t: "))
    email = str(input("Email\t:"))
    role = str(input("(penjual/pembeli) :"))
    
             
# fungsi tampilanPenjual
# Kamus Lokal :
#           

def tampilanPenjual():
    print("="*60)
    print("EJS Store\t\t\t\tWelcome! (Nama User)")
    print("="*60)
    
    print("Nama toko")
    print("0. Pemesanan")
    print("="*30)
    print("1. Produk yang tersisa")
    print("2. Masukan Produk Baru")
    print("3. Produk yang telah terjual :")
    print("4. Back (Log Out)")
    
    pilihan = int(input("Pilihan yang anda ingin lakukan : "))
    while (pilihan >= 0 and pilihan <= 4):
        pilihan = int(input("Pilihan Anda : "))
    print()
    if(pilihan == 0 ):
            profile()

# fungsi pemesananPenjual
# Kamus Lokal :
#    
def pemesananPenjual():
    # pemesanan
    print("="*30)
    print("| Pesanan yang anda terima |")
    print()
    print("Nama Pembeli :")
    print("Nama Produk :")
    print("Kategori (A/B/C/D/E) :")
    print("Ukuran :")
    print("Harga :")

# fungsi produkTersisa
# Kamus Lokal :
#   
def produkTersisa():
    # produk yang tersisa
    print("="*30)
    print("| Produk yang tersisa |")
    print()
    print("Nama Produk :")
    print("Kategori (A/B/C/D/E) :")
    print("Jumlah Produk :")


# fungsi produkBaru
# Kamus Lokal :
#   
def produkBaru():
    # masukan produk baru
    print("="*30)
    print("| Produk yang akan ditambahkan |")
    print()
    print("0. Produk Standar")
    print("1. Back")
    print("Masukan Pilihan Anda :")

# fungsi produkStandar
# Kamus Lokal :
#   
def produkStandar():
    # pilih produk standar
    print("="*30)
    print("| Produk Standar yang akan ditambahkan |")
    print()
    produk=str(input("Nama Produk : "))
    deskripsi=str(input("Deskripsi Produk :"))
    harga=int(input("Harga Produk :"))
    kategori=str(input("Kategori (A/B/C/D/E) :"))
    jumlah=int(input("Jumlah Barang :"))
    
# fungsi produkTerjual
# Kamus Lokal :
#   
def produkTerjual():
    # produk yang telah terjual
    print("="*30)
    print("| Produk yang telah terjual |")
    print()
    print("Nama Pembeli :")
    print("Nama Produk :")
    print("Kategori (A/B/C/D/E) :")
    print("Harga :")
            
                 
# fungsi tampilanPembeli
# Kamus Lokal :
#

def tampilanPembeli():
    print("="*60)
    print("EJS Store\t\t\t\tWelcome! (Nama User)")
    print("="*60)
    print("0. Profile")
    print("1. Home")
    print("2. Shops")
    print("3. Category")
    print("4. Cart")
    print("5. Back")
    
    pilihan = int(input("Pilihan yang anda ingin lakukan : "))
    
    while (pilihan >= 0 and pilihan <= 5):
        pilihan = int(input("Pilihan Anda : "))
    print()
    if(pilihan == 0 ):
        profile()
        
        
## fungsi Profile
# Kamus Lokal :
#
def profile():
    print("Profile")
    print(">"*25)
    print("(Nama User)")
    print("-"*25)
    print("ESP Pay | Rp.x,00 |")
    print("-"*25)
    print()
    print("0.History")
    print("_"*25)
    print("1.My Account")
    print("_"*25)
    print("2.My Voucher")
    print("_"*25)
    print("3.My Isi ESP Pay")
    print("_"*25)
    print("4.Back")
    print("_"*25)
    
    pilihan =  int(input("Pilihan yang anda ingin lakukan : "))
        
    while (pilihan >= 0 and pilihan <= 4):  
        pilihan = int(input("Pilihan Anda : "))
    print()
    
    if (pilihan == 0):
        history()
    elif(pilihan == 1):
        myAccount()
    elif(pilihan == 2):
        myVoucher()
    elif(pilihan == 3):
        isiEspPay()
    elif(pilihan == 4):
        tampilanPembeli() 
            
### fungsi history
# Kamus Lokal :
#

def history():
    print("History")
    print('-'*25)

### fungsi MyAccount
# Kamus Lokal :
#

def myAccount():
    print("My Account")
    print('-'*25)
    print("Nama :")
    print("Email :")
    print('-'*25)
    print("Untuk kembali ketikan 0")
    pilihan=int(input("Pilihan anda :"))
    

### fungsi My Voucher
# Kamus Lokal :
#

def myVoucher():
    print("My Voucher")
    print('-'*25)
    print("Untuk kembali ketikan 4")
    pilihan=int(input("Pilihan anda :"))

### fungsi Isi ESP Pay
# Kamus Lokal :
#

def isiEspPay():
    print("Isi ESP Pay")
    print('-'*25)

## Program Utama ##
# Kamus Lokal

def main():
    # tampilan awal
    tampilanawal()
    
    # tampilan login
    login()

    
if __name__ == '__main__':
    main()

    # print voucher dari array