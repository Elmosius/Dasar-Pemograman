
# File : PR02C_2172028.py
# Penulis : Laurentius Gusti Ontoseno Panata Yudha
# Tujuan Program : Mengkonversi angka menjadi huruf
# Kamus Data :
# angka = var. input angka yang akan dikonversi (int)
# ratusan = var. menyimpan huruf untuk ratusan (str)
# puluhan = var. menyimpan huruf untuk puluhan (str)
# satuan = var. menyimpan huruf untuk satuan (str)
def main():
# Perintah Input
    angka = int(input("Massukan Angka : "))
# Perintah Proses
    if (angka>=100 and angka<200):
        ratusan="Seratus"
        kurang1=angka-100
    elif (angka>=200 and angka<300):
        ratusan="Duaratus"
        kurang1=angka-200
    elif (angka>=300 and angka<400):
        ratusan="Tigaratus"
        kurang1=angka-300
    elif (angka>=400 and angka<500):
        ratusan="Empatratus"
        kurang1=angka-400
    elif (angka>=500 and angka<600):
        ratusan="Limaratus"
        kurang1=angka-500
    elif (angka>=600 and angka<700):
        ratusan="Enamratus"
        kurang1=angka-600
    elif (angka>=700 and angka<800):
        ratusan="Tujuhratus"
        kurang1=angka-700
    elif (angka>=800 and angka<900):
        ratusan="Delapanratus"
        kurang1=angka-800
    elif (angka>=900 and angka<1000):
        ratusan="Sembilanratus"
        kurang1=angka-900
    if (kurang1>=10 and kurang1<20):
        puluhan="Se puluh"
        kurang2=kurang1-10
    elif (kurang1>=20 and kurang1<30):
        puluhan="Dua puluh"
        kurang2=kurang1-20
    elif (kurang1>=30 and kurang1<40):
        puluhan="Tiga puluh"
        kurang2=kurang1-30
    elif (kurang1>=40 and kurang1<50):
        puluhan="Empat puluh"
        kurang2=kurang1-40
    elif (kurang1>=50 and kurang1<60):
        puluhan="Lima puluh"
        kurang2=kurang1-50
    elif (kurang1>=60 and kurang1<70):
        puluhan="Enam puluh"
        kurang2=kurang1-60
    elif (kurang1>=70 and kurang1<80):
        puluhan="Tujuh puluh"
        kurang2=kurang1-70
    elif (kurang1>=80 and kurang1<90):
        puluhan="Delapan puluh"
        kurang2=kurang1-80
    elif (kurang1>=90 and kurang1<100):
        puluhan="Sembilan puluh"
        kurang2=kurang1-90
    if (kurang1==1 or kurang2==1):
        satuan="Satu"
    elif (kurang1==2 or kurang2==2):
        satuan="Dua"
    elif (kurang1==3 or kurang2==3):
        satuan="Tiga"
    elif (kurang1==4 or kurang2==4):
        satuan="Empat"
    elif (kurang1==5 or kurang2==5):
        satuan="Lima"
    elif (kurang1==6 or kurang2==6):
        satuan="Enam"
    elif (kurang1==7 or kurang2==7):
        satuan="Tujuh"
    elif (kurang1==8 or kurang2==8):
        satuan="Delapan"
    elif (kurang1==9 or kurang2==9):
        satuan="Sembilan"
    
# Perintah Output
    print("angka :", angka)
    print("Hasil Konversi :")
    print(ratusan, puluhan, satuan)
    return 0


if __name__ == '__main__':
    main()