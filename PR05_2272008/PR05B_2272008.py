# File : PR05B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima sebuah bilangan 
# bulat N lalu akan menampilkan N simbol Nintendo
# Kamus Data :
# i : var. pertambahan awal (int)
# angka : var. input berapa pola (int)

def main():
    # inisialisasi
    i = 0
    
    # input
    angka = int(input(""))

    # proses dan output
    while(i != angka): 
        i += 1
        if(i % 4 == 1):
            print('  *  ')
            print('* * *')
            print()
        elif(i % 4 == 2):
            print(' *  ')
            print(' * *')
            print(' *  ')
            print()
        elif(i % 4 == 3):
            print('  * ')
            print('* * ')
            print('  * ')
            print()
        elif(i % 4 == 0):
            print('* * *')
            print('  *  ')
            print()
            
if __name__ == '__main__':
    main()