# File: Tugas3_Nomor1_2272008.py
# Penulis : Elmosius Suli
# Program mencetak tabel konversi dari Celcius ke Reaumur dan Fahrenheit
# Program membaca tiga bilangan integer untuk awal, akhir, dan inkremen
# Kamus Data
# awal, akhir, dan inkremen : var. input (int)
# R : var. rumus menentukan Reaumur (int) 
# F : var. rumus menentukan Fahrenheit (int)

def main ():
    # input
    awal = int(input("awal = "))
    akhir = int(input("akhir = "))
    inkremen = int(input("inkremen = "))

    # proses pengulangan
    print ('C \t R\t F')
    while (awal <= akhir):
        R = int(4/5*awal)
        F = int(9/5*awal +32)
        
        # output
        print(awal,'\t',R,'\t',F)
        awal += inkremen
        
if __name__ == '__main__':
    main()