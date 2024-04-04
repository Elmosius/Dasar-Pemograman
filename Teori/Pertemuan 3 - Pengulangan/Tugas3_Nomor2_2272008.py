# File: Tugas3_Nomor2_2272008.py
# Penulis : Elmosius Suli
# Program membaca sederetan data nilai yang diakhiri dengan 9999.
# Program menghitung rata-rata seluruh nilai yang diinput.
# Kamus Data
# x : var. input nilai x (int)
# i : var.counter while (int)
# n : var. nilai jumlh (int)

def main ():

    # inisialisasi
    x = int(input("Nilai x : "))
    i = 0
    n = 0

    # proses pengulangan
    while(x != 9999):
        n += 1
        i += x
        x = int(input("Nilai x : "))

    # output    
    print(round((i/n),2))       

if __name__ == '__main__':
    main()