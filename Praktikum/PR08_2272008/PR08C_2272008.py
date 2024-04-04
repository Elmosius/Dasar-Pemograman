# File : PR08C_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program untuk menghitung gaji
# seorang pegawai

# fungsi hitungGajiKotor
# Kamus Lokal 
# gajiPokok : var. parameter (int)
# tunjanganKeluarga : var. parameter(float)
# tunjanganKesehatan : var. parameter(int)
def hitungGajiKotor(gajiPokok, tunjanganKeluarga, tunjanganKesehatan):
    hgk = gajiPokok + tunjanganKeluarga + tunjanganKesehatan
    return hgk
 
# fungsi hitungPajak
# Kamus Lokal 
# gajiKotor : var. parameter(float)
# pajak : var. meghitung pajak(float)
def hitungPajak(gajiKotor):
    if(gajiKotor > 3000000):
        pajak = gajiKotor*0.05
    else:
        pajak = 0
    return pajak
    
# fungsi hitungGajiBersih
# Kamus Lokal 
# gajiKotor : var. parameter(float)
# pajak : var. parameter(float)
# gb : var. gaji bersih(float)
def hitungGajiBersih(gajiKotor, pajak):
    gb = gajiKotor - pajak
    return gb
    
# fungsi cetakSlipgaji
# Kamus Lokal 
# nama : var. parameter(str)
# gajiPokok : var. parameter (int)
# tunjanganKeluarga : var. parameter(float)
# gajiKotor : var. parameter(float)
# pajak : var. parameter(float)
# gajiBersih : var. parameter(float)

def cetakSlipgaji(nama, gajiPokok, tunjanganKeluarga, tunjanganKesehatan, gajiKotor, pajak, gajiBersih):
    print("========================================")
    print("Nama:",nama)
    print("Gaji Pokok:",gajiPokok)
    print("Tunjangan Kesehatan:",tunjanganKesehatan)
    print("Tunjangan Keluarga:",tunjanganKeluarga)
    print("========================================")

    print("Gaji Kotor:", gajiKotor)
    print("Pajak:",pajak)
    print("Gaji Bersih:",gajiBersih)
    print("========================================")
        
## Program Utama ##
# Kamus Lokal 
# angka : var. input (int)
# golongan : var. input golongan(str)
# sn : var. status nikah(str)
# gp : var. gaji pokok(int)
# tk : var. tunjangan kesehatan(int)
# tkl : var. tunjangan keluarga(float)
# gk : var. gaji kotor(float)
# pajak : var. pajak(float)
# gb : var. gaji bersih(float)

def main():
    # input
    nama = input("Nama: ")
    golongan = int(input("Golongan: "))
    sn = input("Status Nikah : ")
    
    # golongan
    if (golongan == 1):
        gp = 3500000
        tk = 750000
    elif(golongan == 2):
        gp = 3000000
        tk = 500000
    elif(golongan == 3):
        gp = 2500000
        tk = 400000
    else:
        gp = 2000000
        tk = 300000
        
    # status menikah
    if (sn == "k"):
        tkl = (0.1 * gp)
    else:
        tkl = 0
        
    # gaji kotor
    gk = hitungGajiKotor(gp,tkl,tk)
    
    # pajak
    pajak = hitungPajak(gk)
    
    # gaji bersih
    gb = hitungGajiBersih(gk,pajak)
    
    # output
    cetakSlipgaji(nama,gp,tkl,tk,gk,pajak,gb)
         
if __name__ == '__main__':
    main()