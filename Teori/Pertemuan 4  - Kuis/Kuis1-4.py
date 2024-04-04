# File : Soal1-4.py
# Penulis : Elmosius Suli
# Tujuan Program : program untuk menghitung gaji yang diterima seorang pegawai.
# Kamus Data : 
# nip : var. input (int)
# nama : var. input (str)
# status_nikah : var. input (str)
# golongan : var. input (int)
# jumlah_anak : var. input (int)
# hg : var. harga golongan (int)
# tunjangan : var. menghitung tunjangan (int)
# pot_pajak : var. potongan pajak (int)
# pajak : var. total pajak dari gaji (int)

def main():
    # input 
    nip = int(input("NIP : "))
    nama = str(input("Nama : "))
    status_nikah = str(input("Status Nikah :"))
    if(status_nikah == "Y" ) or (status_nikah == "y"):
        jumlah_anak = int(input("Jumlah Anak :"))
    golongan = int(input("Golongan :"))

    # proses
    if(golongan == 1):
        hg = 6000000
    elif(golongan == 2):
        hg = 5000000
    else:
        hg = 4000000
   
    if(status_nikah == "Y" ) or (status_nikah == "y"):
        if(jumlah_anak == 0):
            tunjangan = (hg*0.15)
        elif(jumlah_anak == 1):
            tunjangan = (hg*0.15) + (hg*0.03)
        elif(jumlah_anak == 2):    
            tunjangan = (hg*0.15) + (hg*0.06)
        else:
            tunjangan = (hg*0.15) + (hg*0.06)
        gaji_total = (hg + tunjangan)    
        pot_pajak = gaji_total*0.1
    else:
        tunjangan = (hg*0.07)
        gaji_total = (hg + tunjangan)
        pot_pajak = 0

    if(gaji_total <= 4000000):
        persen_pajak = "(5%)"
        pajak = (gaji_total - pot_pajak)*0.05 
    elif(gaji_total <= 7000000):
        persen_pajak = "(7%)"
        pajak = (gaji_total - pot_pajak)*0.07 
    elif(gaji_total >= 7000000):
        persen_pajak = "(10%)"
        pajak = (gaji_total - pot_pajak)*0.1    
        
    # output
    print(" ")
    print(nama,"-",nip)
    print("Golongan :", golongan)
    print("=================================")
    print("Gaji Pokok : Rp.", hg)
    print("Tunjangan : Rp.", int(tunjangan))
    print("Total Gaji : Rp.", int(gaji_total))
    print("---------------------------------")
    print("Pot.tidak kena pajar : Rp.", int(pot_pajak))
    print("Pajak", persen_pajak, ": Rp.", int(pajak))
    print("=================================")
    print("Gaji yg diterima : Rp.", int(gaji_total - pajak))

if __name__ == '__main__':
    main()