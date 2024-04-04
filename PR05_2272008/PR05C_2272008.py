# File : PR05C_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan memberikan struk
# dari pesanan yang diinput oleh user dari 2 
# restoran yang disediakan. 
# Kamus Data :
# nama : var. input nama (str)
# tempat : var. input tempat (int)
# pilih : var. input pesan/ cetak (int)
# menu : var. input menu (int)
# pm : var. keranjang menyimpan menu (str)
# h : var. menyimpan harga (int)
# p : var. menyimpan menu (str)
# v : var. nama voucher (str)
# pv : var. potongan voucher (int)


def main():
    
    # inisialisasi
    pm = ''
    h = 0
    
    # input
    nama = str(input("Nama pemesan: "))
    print('=======================\n'
    '1. Solario\n2. Tobarob')
    tempat = int(input('Silahkan Pilih Tempat: '))
    print('=======================')
    
    # proses solaria
    if(tempat == 1):
        print('Selamat datang di Solario\n'
        '1. Pesan\n2. Cetak struk')
        pilih = int(input('Pilihan: '))
        while (pilih != 2):
            
            # menu solaria
            if(pilih == 1):
                print('======== Menu =========')
                print('1. Nasi goreng seafood\n' 
                '2. Bihun siram ayam\n'
                '3. Es Teh Manis')
                
                menu = int(input("Silahkan pilih menu: "))
                if (menu == 1):
                    p= 'Nasi goreng seafood'
                    h += 40000
                elif(menu == 2):
                    p= 'Bihun siram ayam'
                    h += 37000
                else:
                    p='Es teh manis'
                    h += 9000 
                    
                pm += p                       
                print("Menu ditambahkan")
                print('1. Pesan\n2. Cetak struk')
                pilih = int(input('Pilihan: '))
                if(pilih != 2):
                    pm += ', '
        
        # struk
        print('=======================')
        v = str(input("Masukkan kode voucher:\n"))      

        if (v == "JAYAJAYA"):
            pv = 8000
            print('Kode voucher benar !!')
        else:   
            pv = 0 
            print('Kode voucher salah !!')
      
    # proses Tobarob 
    if(tempat == 2):
        print('Selamat datang di Tobarob\n'
        '1. Pesan\n2. Cetak struk')
        pilih = int(input('Pilihan: '))
        while (pilih != 2):
            
            # menu tobarob
            if(pilih == 1):
                print('======== Menu =========')
                print('1. Ayam panggan itali\n' 
                '2. Dori sambal matah\n'
                '3. Iced rock coffee')
                
                menu = int(input("Silahkan pilih menu: "))
                if (menu == 1):
                    p= 'Ayam panggan itali'
                    h += 32000
                elif(menu == 2):
                    p= 'Dori sambal matah'
                    h += 30000
                else:
                    p='Iced rock coffee'
                    h += 25000
                    
                pm += p                    
                print("Menu ditambahkan")
                print('1. Pesan\n2. Cetak struk')
                pilih = int(input('Pilihan: '))
                if(pilih != 2):
                    pm += ', '
        
        # struk
        print('=======================')
        v = str(input("Masukkan kode voucher:\n"))      

        if (v == "FOLLOWYUK"):
            pv = 8000
            print('Kode voucher benar !!')
        else:   
            pv = 0 
            print('Kode voucher salah !!')
            
    # output
    if (tempat == 1):
        print('Nama: ',nama)
        print('Pesanan:',pm) 
        print('Harga: ', h)
        print('PPN: ', int(h*0.15))
        print('Potongan: ',pv)
        print('Total: ', int(h + (h*0.15)-pv))
    else:
        print('Nama: ',nama)
        print('Pesanan:',pm) 
        print('Harga: ', h)
        print('PPN: ', int(h*0.15))
        print('Potongan: ',pv)
        print('Total: ', int(h + (h*0.15)-pv))
    print('=======================')
 
if __name__ == '__main__':
    main()