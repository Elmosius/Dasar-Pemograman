import os.path
import glob

# File : PT4_2272008_2272020_2272030.py
# Penulis : Elmosius Suli, Joseph Adiwiguna, dan Samuel
# Tujuan Program :  Membuat toko Bakery
## Definisi Fungsi ##

# fungsi tampilan awal
# Kamus Lokal :
# i = integer (pengulangan for)
# login() = fungsi login


def tampilanawal():
    print("==================================")
    print()
    print("        ", end='')
    for i in range(0, 5, 1):
        print("*   ", end='')
    print()
    print("        ", end='')
    for i in range(0, 5, 1):
        print("|   ", end='')
    print()
    print("      *********************")
    for i in range(0, 2, 1):
        print("      *                   *")
    print("   ****************************")
    print("   *                          *")
    print("   *~~~~~~~ EJS BAKERY ~~~~~~~*")
    print("   *                          *")
    print("   ****************************")
    print()
    print("---------------------------------")
    print("    Welcome To EJS Bakery :D")
    print("---------------------------------")
    print()
    login()
# fungsi login
# Kamus Lokal :
#


def login():
    print("0. Sign In")
    print("1. Sign Up")
    print()
    print("Jika belum memiliki akun, ketikan 1 untuk membuat akun")
    pilihan = int(input("Pilihan Anda : "))

    while (pilihan != 0 and pilihan != 1):
        pilihan = int(input("Pilihan Anda : "))

    print()
    if (pilihan == 0):
        signin()
    elif (pilihan == 1):
        signup()

# fungsi singin
# Kamus Lokal :
#


def signin():
    global username, c

    print('\t', '='*25)
    print("\t\t| Sign In | ")
    print()
    file = open("register.txt", "r")
    username = str(input("\t Username : "))
    password = str(input("\t Password : "))

    ada = False

    for i in file:
        # Validasi login
        a, b, c, d = i.split(",")
        d = d.strip()
        if (a == username and b == password):
            ada = True
            roleFinal = d

    while (ada == False):
        print("| Salah Username atau email atau Password |")
        print()
        username = str(input("\t Username : "))
        password = str(input("\t Password : "))

        file = open("register.txt", "r")
        for i in file:
            # Validasi login
            a, b, c, d = i.split(",")
            d = d.strip()
            if (a == username and b == password):
                ada = True
                roleFinal = d

    # Login untuk Role penjual

    if (roleFinal == 'penjual'):
        print()
        tampilanPenjual()
    else:
        print()
        tampilanPembeli()

# fungsi singup
# Kamus Lokal :
#


def signup():
    global toko

    print('\t', '='*25)
    print("\t\t| Sign Up | ")
    print()
    username = str(input("\t Username\t: "))
    password = str(input("\t Password\t: "))
    email = str(input("\t Email\t:"))
    role = str(input("\t (penjual/pembeli): "))

    # Validasi username sudah dipakai atau belum
    file = open("register.txt", "r")
    for i in file:
        check = False
        while (check == False):
            a, b, c, d = i.split(",")
            d = d.strip()
            if (a != username):
                check = True
            else:
                print()
                print("\t Username sudah dipakai! Coba lagi")
                print()
                username = str(input("\t Username\t: "))
                password = str(input("\t Password\t: "))
                email = str(input("\t Email\t:"))
                role = str(input("\t (penjual/pembeli): "))
        file = open("register.txt", "r")

    # kalo rolenya penjual
    if (role == 'penjual'):
        print()
        print("\t Role")
        print('\t', "-"*25)
        toko = str(input("\t Nama toko : "))
        desc = str(input("\t Desc : "))

        # membuat file sesuai toko
        file = open(f"{username}_terjual.txt", "a")
        file = open(f"{username}_toko.txt", "a")
        file.write("\n"+toko+","+desc)
        file.close()

    # Membuat file di txt
    file = open("register.txt", "a")
    file.write("\n"+username+","+password+','+email+','+role)
    file.close()
    print()
    signin()


# fungsi tampilanPenjual
# Kamus Lokal :
#

def tampilanPenjual():
    print("="*60)
    print("EJS Store\t\t\t\t  Welcome!", username)
    print("="*60)

    # tampilan nama toko
    file = open(f"{username}_toko.txt", 'r')
    temp = file.readlines()[1]
    toko = temp.split(',')[-2]
    print(toko)
    file.close()

    # daftar menu penjual
    print("0. Masukan Produk Baru")
    print("1. List Produk yang sudah ditambahkan")
    print("2. Produk yang telah terjual")
    print("3. Back (Log Out)")

    pilihan = int(input("Pilihan yang anda ingin lakukan : "))
    while (pilihan < 0 and pilihan > 4):
        pilihan = int(input("Pilihan Anda : "))
    print()
    if (pilihan == 0):
        produkBaru()
    elif (pilihan == 1):
        listProduk()
    elif (pilihan == 2):
        produkTerjual()
    else:
        tampilanawal()


# Fungsi listProduk
#

def listProduk():
    # produk yang tersisa
    print("="*30)
    print("| List Produk yang Sudah Ditambahkan |")
    print()

    file = open(f'{username}_toko.txt', 'r')
    temp = file.readlines()[2:]
    i = 0
    for j in temp:
        a, b, c, d = j.split(",")
        print(i, '.', 'Nama Produk: ', a)
        print('Desc :', b)
        print('Harga : Rp.', c, ',00')
        print('Ukuran :', d)
        i += 1
    file.close()

    print()
    print("0. Back")
    pilihan = int(input("Pilihan Anda : "))
    while (pilihan != 0):
        pilihan = int(input("Pilihan Anda : "))

    if (pilihan == 0):
        print()
        tampilanPenjual()


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
    pilihan = int(input("Pilihan Anda : "))
    while (pilihan != 0 and pilihan != 1):
        pilihan = int(input("Pilihan Anda : "))
    print()
    if (pilihan == 0):
        produkStandar()
    elif (pilihan == 1):
        tampilanPenjual()

# fungsi produkStandar
# Kamus Lokal :
#


def produkStandar():
    # pilih produk standar
    print("="*30)
    print("| Produk Standar yang akan ditambahkan |")
    print()
    produk = str(input("Nama Produk : "))
    deskripsi = str(input("Deskripsi Produk :"))
    harga = str(input("Harga Produk :"))
    kategori = str(input("Ukuran (s/m/l) :"))
    file = open(f'{username}_toko.txt', 'a')
    file.write("\n"+produk+","+deskripsi+","+harga+","+kategori)
    file.close()
    print()
    produkBaru()


# fungsi produkTerjual
# Kamus Lokal :
#


def produkTerjual():
    # produk yang telah terjual
    print("="*30)
    print("| Produk yang telah terjual |")
    print()

    # ngeprint semua data
    file = open(f"{username}_terjual.txt", 'r')
    temp = file.readlines()[1:]

    i = 0
    for j in temp:
        a, b, c, d = j.split(",")
        print(i, '.', 'Nama Produk: ', a)
        print('Desc :', b)
        print('Harga : Rp.', c, ',00')
        print('Ukuran :', d)
        i += 1
    file.close()

    # total harga item
    total = 0
    file = open(f"{username}_terjual.txt", 'r')
    temp = file.readlines()[1:]
    for i in temp:
        harga = int(i.split(',')[-2])
        total += harga
    file.close()
    print("Total Harga Semua Item | Rp.", total, ',00 |')
    print()

    # kembali
    print()
    print("999. Back")
    pilihan = int(input("Pilihan yang anda ingin lakukan (Hanya Back) : "))
    while (pilihan != 999):
        pilihan = int(input("Pilihan Anda : "))
    print()
    tampilanPenjual()

# fungsi tampilanPembeli
# Kamus Lokal :
#


def tampilanPembeli():
    global username

    # check file
    check = os.path.isfile(f'{username}_Profile.txt')
    if not check:
        file = open(f'{username}_History.txt', 'a')
        file = open(f'{username}_Like.txt', 'a')
        file = open(f'{username}_Profile.txt', 'a')
        file.write('0')
        file.close()

    print("="*60)
    print("EJS Store\t\t\t\t   Welcome!", username)
    print("="*60)
    print("0. Profile")
    print("1. Shops")
    print("2. Cart")
    print("3. Like")
    print("4. Back (Log Out)")

    pilihan = int(input("Pilihan yang anda ingin lakukan : "))

    while (pilihan < 0 or pilihan > 5):
        pilihan = int(input("Pilihan Anda : "))
    print()

    if (pilihan == 0):
        profile()
    elif (pilihan == 1):
        shop()
    elif (pilihan == 2):
        cart()
    elif (pilihan == 3):
        tampilanLike()
    else:
        tampilanawal()


# fungsi tampilanLike()
#
def tampilanLike():
    print("Kue kesukaanmu :D")
    print(">"*25)
    file = open(f'{username}_Like.txt', 'r')
    temp = file.readlines()

    i = 0
    for j in temp:
        a, b, c, d = j.split(',')
        print(i, '.', a)
        print("Kategori :", d, end="")
        print("Harga : Rp.", c, ',00')
        print()
        i += 1
    file.close()
    print()
    print("0. Hapus")
    print("1. Back")

    pilihan = int(input("Pilihan yang anda ingin lakukan : "))
    while (pilihan < 0 or pilihan > 1):
        pilihan = int(input("Pilihan Anda : "))

    if (pilihan == 0):
        print()
        pilih = int(input("Nomor berapa yang ingin dihapus : "))

        # delete like line tertentu
        file = open(f"{username}_Like.txt", 'r+')
        lines = file.readlines()
        del lines[pilih]
        file.seek(0)
        file.truncate()
        file.writelines(lines)

        file.close()
        print()
        tampilanLike()

    else:
        print()
        tampilanPembeli()

# fungsi Profile
# Kamus Lokal :
#


def profile():
    global esp

    print("Profile")
    print(">"*25)
    print(username)
    print("-"*25)
    file = open(f'{username}_Profile.txt', 'r')
    temp = file.readlines()[0]
    esp = int(temp.split(',')[-1])

    print("ESP Pay | Rp."f"{esp},00 |")
    file.close()
    print("-"*25)
    print()
    print("0.History")
    print("_"*25)
    print("1.My Account")
    print("_"*25)
    print("2.My Isi ESP Pay")
    print("_"*25)
    print("3.Back")
    print("_"*25)

    pilihan = int(input("Pilihan yang anda ingin lakukan : "))
    while (pilihan < 0 or pilihan > 4):
        pilihan = int(input("Pilihan Anda : "))
    print()

    if (pilihan == 0):
        history()
    elif (pilihan == 1):
        myAccount()
    elif (pilihan == 2):
        isiEspPay()
    else:
        tampilanPembeli()

# fungsi history
# Kamus Lokal :
#


def history():
    print("History")
    print('-'*25)
    file = open(f"{username}_History.txt", 'r')
    temp = file.readlines()[1:]
    i = 1
    for j in temp:
        a, b, c, d = j.split(',')
        print(i, '.', a)
        print("Kategori :", d)
        print("Harga : Rp.", c, ',00')
        print()
        i += 1

    # total harga item
    total = 0
    file = open(f"{username}_History.txt", 'r')
    temp = file.readlines()[1:]
    for i in temp:
        harga = int(i.split(',')[-2])
        total += harga
    file.close()
    print("Total Harga Semua Item | Rp.", total, ',00 |')
    print()

    # kembali
    print()
    print("999. Back")
    pilihan = int(input("Pilihan yang anda ingin lakukan (Hanya Back) : "))
    while (pilihan != 999):
        pilihan = int(input("Pilihan Anda : "))

    print()
    profile()

# fungsi MyAccount
# Kamus Lokal :
#


def myAccount():
    print("My Account")
    print('-'*25)
    print("Nama :", username)
    print("Email :", c)
    print('-'*25)
    print("Untuk kembali ketikan 0")
    pilihan = int(input("Pilihan anda :"))
    while (pilihan > 0):
        pilihan = int(input("Pilihan anda :"))
    if (pilihan == 0):
        profile()

# fungsi My Voucher
# Kamus Lokal :
#


def myVoucher():
    print("My Voucher")
    print('-'*25)
    print("Untuk kembali ketikan 4")
    pilihan = int(input("Pilihan anda :"))

# fungsi Isi ESP Pay
# Kamus Lokal :
#


def isiEspPay():
    global esp

    print("Isi ESP Pay")
    print('-'*25)
    print("0. Top Up")
    print("1. Back")

    pilihan = int(input("Pilihan Anda : "))
    while (pilihan < 0 or pilihan > 1):
        pilihan = int(input("Pilihan Anda : "))
    print()

    if (pilihan == 0):
        topup = int(input("Rp. : "))
        file = open(f'{username}_Profile.txt', 'r+')
        esp += topup

        # ngewrite ke barisan pertama
        lines = file.readlines()
        lines[0] = lines[0].strip()+','+f'{esp}'+'\n'
        file.seek(0)
        file.writelines(lines)
        file.close()
        isiEspPay()
    else:
        profile()

# fungsi shops
# Kamus Lokal


def shop():
    print("Shops")
    print(">"*25)
    print("0. Produk Reguler")
    print("1. Back")

    pilihan = int(input("Pilihan Anda : "))
    while (pilihan < 0 or pilihan > 1):
        pilihan = int(input("Pilihan Anda : "))

    if (pilihan == 0):
        print()
        produkReguler()
    else:
        print()
        tampilanPembeli()

# fungsi produk reguler penjual
#


def produkReguler():

    files = glob.glob("*_toko.txt")
    j = 0

    for i in files:
        print()
        file = open(i, 'r')
        temp = file.readlines()[2]
        a, b, c, d = temp.split(',')
        print('\t', j, '.', a)
        print('\t Ukuran :', d, end="")
        print('\t Harga : Rp.', c, ',00')
        print('\t Desc :', b)
        print()
        file.close()
        j += 1

    print("\t 999. Back")
    pili = int(input("\t Pilihan Anda : "))

    # kalau pilihan back
    if (pili == 999):
        print()
        shop()
    else:
        print()
        print('\t 0. Masukkan keranjang')
        print('\t 1. Like')
        print('\t 2. Check Penjual')

        pilihan = int(input("\t Pilihan Anda : "))
        while (pilihan < 0 or pilihan > 2):
            pilihan = int(input("\t Pilihan Anda : "))

        if (pilihan == 0):
            masukkinKeranjangs(pili)
        elif (pilihan == 1):
            likes(pili)
        else:
            checkPenjual(pili)


# Fungsi Like untuk shop
#
def likes(x):
    files = glob.glob("*_toko.txt")
    file = open(files[x], 'r')
    temp = file.readlines()[2]
    a, b, c, d = temp.split(',')
    file.close()

    file = open(f"{username}_Like.txt", 'a')
    file.write(a+','+b+','+c+','+d)
    file.close()
    produkReguler()

# Fungsi Like untuk shop
#


def like(x, y):
    files = glob.glob("*_toko.txt")
    file = open(files[x], 'r')
    temp = file.readlines()[y+1]
    a, b, c, d = temp.split(',')
    file.close()

    file = open(f"{username}_Like.txt", 'a')
    file.write(a+','+b+','+c+','+d)
    file.close()
    checkPenjual(x)


# Fungsi masukkinKeranjang checkpenjual
#
def masukkinKeranjang(x, y):
    files = glob.glob("*_toko.txt")
    file = open(files[x], 'r')
    if ((y + 2) == len(file.readlines())):
        files = glob.glob("*_toko.txt")
        file = open(files[x], 'r')
        temp = file.readlines()[y+1]
    else:
        files = glob.glob("*_toko.txt")
        file = open(files[x], 'r')
        temp = file.readlines()[y+1][:-1]

    a, b, c, d = temp.split(',')
    file.close()

    file = open(f"{username}_Profile.txt", 'a')
    file.write('\n'+a+','+b+','+c+','+d+','+files[x][:-9])
    file.close()
    checkPenjual(x)


# Fungsi masukkinKeranjang Shops
#
def masukkinKeranjangs(x):
    files = glob.glob("*_toko.txt")
    file = open(files[x], 'r')
    temp = file.readlines()[2][:-1]

    a, b, c, d = temp.split(',')
    file.close()

    file = open(f"{username}_Profile.txt", 'a')
    file.write('\n'+a+','+b+','+c+','+d+','+files[x][:-9])
    file.close()
    produkReguler()

# fungsi checkPenjual
#


def checkPenjual(x):
    # nampilin nama toko
    files = glob.glob("*_toko.txt")
    file = open(files[x], 'r')

    temp = file.readlines()[1]
    a, b = temp.split(',')
    print()
    print(a)

    # nampilin deskripsi
    print(b, end="")
    print("-"*25)

    # nampilin semua list barang
    file = open(files[x], 'r')
    tem = file.readlines()[2:]

    i = 1
    for j in tem:
        c, d, e, f = j.split(',')
        print(i, '.', c)
        i += 1
    print("999. Back")
    pili = int(input("Pilihan Anda : "))

    if (pili == 999):
        produkReguler()
    # pilihan
    print()

    # detail barang
    file = open(files[x], 'r')
    temp = file.readlines()[pili+1]
    a, b, c, d = temp.split(',')
    print('\t', a)
    print('\t Ukuran :', d, end="")
    print('\t Harga : Rp.', c, ',00')
    print('\t Desc :', b)
    print()

    print('\t 0. Masukkan keranjang')
    print('\t 1. Like')
    print('\t 2. Back')

    pilihan = int(input("Pilihan Anda : "))
    while (pilihan < 0 or pilihan > 2):
        pilihan = int(input("Pilihan Anda : "))

    if (pilihan == 0):
        print()
        masukkinKeranjang(x, pili)

    elif (pilihan == 1):
        print()
        like(x, pili)
    else:
        print()
        checkPenjual(x)

    file.close()

# Fungsi Cart
#


def cart():
    print("Cart")
    print(">"*25)
    print()

    # munculin semua produk
    i = 1
    file = open(f'{username}_Profile.txt', 'r')
    temp = file.readlines()[1:]

    for j in temp:
        a, b, c, d, e = j.split(',')
        print(i, '.', a, ' Rp.', c, ',00', 'Ukuran', d)
        i += 1
    print()
    print("Total Item |", i-1, '|')

    # total harga item
    total = 0
    file = open(f"{username}_Profile.txt", 'r')
    temp = file.readlines()[1:]
    for i in temp:
        harga = int(i.split(',')[-3])
        total += harga
    file.close()

    print("Total Harga Semua Item | Rp.", total, ',00 |')
    print("-"*25)
    print("0. Bayar")
    print("1. Back")

    pilihan = int(input("Pilihan Anda : "))
    while (pilihan < 0 or pilihan > 1):
        pilihan = int(input("Pilihan Anda : "))

    if (pilihan == 0):
        print()
        pembayaran(total)
    else:
        print()
        tampilanPembeli()

# Fungsi Pembayaran
#


def pembayaran(x):
    print("Pembayaran")
    print(">"*25)
    print("0. Isi ESP Pay")
    print("1. Bayar pakai ESP Pay")

    pilihan = int(input("Pilihan Anda : "))
    while (pilihan < 0 or pilihan > 1):
        pilihan = int(input("Pilihan Anda : "))

    if (pilihan == 0):
        print()
        profile()
    else:
        print()
        # ambil uang saldo sekarang
        file = open(f"{username}_Profile.txt", 'r')
        temp = file.readlines()[0]
        saldo_sekarang = int(temp.split(',')[-1])

        # ambil total saldo dari yang dibelii
        if (x <= saldo_sekarang):
            saldo_sekarang -= x

            # Promo
            if (x >= 100000):
                print(
                    "Anda mendapatkan potongan sebesar 2% karena membeli di atas 100 ribu.")
                promo = saldo_sekarang*0.02
                saldo_sekarang -= promo
            elif (x >= 200000):
                print(
                    "Anda mendapatkan potongan sebesar 5% karena membeli di atas 200 ribu.")
                promo = saldo_sekarang*0.05
                saldo_sekarang -= promo
            elif (x >= 300000):
                print(
                    "Anda mendapatkan potongan sebesar 7% karena membeli di atas 300 ribu.")
                promo = saldo_sekarang*0.07
                saldo_sekarang -= promo

            # nambahin ke history
            file = open(f"{username}_Profile.txt", 'r')
            temp = file.readlines()[1:]
            for i in temp:
                a, b, c, d, e = i.split(",")
                file_history = open(f"{username}_History.txt", 'a')
                file_history.write('\n'+a+','+b+','+c+','+d)
            file.close()
            file_history.close()

            # masukkin semua item ke terjual
            file = open(f"{username}_Profile.txt", 'r')
            temp = file.readlines()[1:]

            for count, i in enumerate(temp):
                a, b, c, d, e = i.split(',')
                file = open(f"{username}_Profile.txt", 'r')
                temp = file.readlines()[1:]
                if (count == len(temp) - 1):
                    file = open(f'{e}_terjual.txt', 'a')
                else:
                    file = open(f'{e[:-1]}_terjual.txt', 'a')
                file.write('\n'+a+','+b+','+c+','+d)
            file.close()

           # reset
            file = open(f"{username}_Profile.txt", 'r+')
            lines = file.readlines()
            file.seek(0)
            file.write(lines[0][:-1])
            file.truncate()
            file.close()

            # ngewrite ke barisan pertama untuk saldo
            file = open(f"{username}_Profile.txt", 'r+')
            lines = file.readlines()
            file.seek(0)
            lines[0] = lines[0].strip()+','+f'{int(saldo_sekarang)}'
            file.writelines(lines[0])
            file.close()
            print("Terima kasih Sudah Membeli ditunggu Ya Pesanannya!")
            print()

        # kalau saldo kurang
        else:
            print()
            print("Maaf Dana ESP anda tidak cukup")
            print()
            profile()

        file.close()
    tampilanPembeli()


## Program Utama ##
# Kamus Lokal


def main():
    # tampilan awal
    tampilanawal()


if __name__ == '__main__':
    main()
