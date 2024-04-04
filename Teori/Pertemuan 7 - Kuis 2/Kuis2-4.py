# File : Kuis2-4.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menginput data NRP dan 
# IPK calon lulusan yang diakhiri dengan 9999 untuk NRP
# Kamus Data
# ipk_rendah : var. ipk terkecil (float)
# ipk_tinggi : var. ipk terbesar (float)
# jumlah_orang : var. banyaknya orang (int)
# pujian : var. predikat sangat tinggi (int)
# sangat_memuaskan : var. predikat tinggi (int)
# memuaskan : var. predikat menengah (int)
# total_ipk : var. total seluruh ipk (float)
# nrp : var. input NRP (int)


def main ():
    
    # inisialisasi
    ipk_rendah = 3.5
    ipk_tinggi = 0
    jumlah_orang = 0
    pujian = 0
    sangat_memuaskan = 0
    memuaskan = 0
    total_ipk = 0
    
    # input
    nrp = int(input("NRP : "))
        
    # proses 
    while (nrp != 9999):
        ipk = float(input("IPK : "))
        total_ipk += ipk
        
        # proses ipk rendah dan tertinggi
        if(ipk >= ipk_tinggi):
            ipk_tinggi = ipk
        if(ipk <= ipk_rendah):
            ipk_rendah = ipk

        # proses predikat
        if(ipk >= 3.5):
            pujian += 1
        elif(ipk >= 2.0 and ipk < 2.75):
            memuaskan += 1
        else:
            sangat_memuaskan += 1

        jumlah_orang += 1
        nrp = int(input("NRP : "))
        
    # output
    print("Dengan pujian    \t :",pujian,'(',int(pujian/jumlah_orang*100),'% )')
    print("Sangat memuaskan \t :",sangat_memuaskan,'(',int(sangat_memuaskan/jumlah_orang*100),'% )')
    print("Memuaskan        \t :",memuaskan,'(',int(memuaskan/jumlah_orang*100),'% )')
    print("IPK terbesar     \t :", ipk_tinggi)
    print("IPK terbesar     \t :", ipk_rendah)
    print("rata-rata        \t :",round(total_ipk/jumlah_orang,2))
  
        
if __name__ == "__main__":
    main()
