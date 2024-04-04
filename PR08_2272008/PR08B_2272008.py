# File : PR08B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program memberitahu user apakah berat
# badannya sudah ideal atau belum.

# fungsi hitungBMI
# Kamus Lokal
# beratBadan : var. parameter(int)
# tinggiBadan: var. parameter(int)
# hasil : var. hasil bmi(float)
def hitungBMI(beratBadan, tinggiBadan):
    hasil = beratBadan/((tinggiBadan/100)**2)
    return hasil

# fungsi cekStatus
# Kamus Lokal
# BMI : var. parameter(int)
# check : var. mengecheck kriteria dari bmi(str)
def cekStatus(BMI):
    if(BMI < 18.5):
        check = "Underweight atau berat badan kurang."
    elif(BMI < 22.9):
        check = "Berat badan ideal, sangat bagus."
    elif(BMI < 24.9):
        check = "Kategori ideal warning,jaga pola makan dan olahraga."
    elif(BMI < 29.9):
        check = "Kondisi berat badan memasuki batas obesitas, segera mulai program diet."
    else:
        check = "Anda sudah termasuk kategori obesitas."
    return check
    
## Program Utama ##
# Kamus Lokal
# bb : var. input berat badan(int)
# tb : var. input tinggi badan(int)
# hbmi : var. hasil bmi (float)

def main():
    # input
    bb = int(input("Berat Badan(kg): "))
    tb = int(input("Tinggi Badan(cm): "))
    
    # output
    hbmi = hitungBMI(bb,tb)
    print("BMI:",round(hbmi,5))
    print(cekStatus(hbmi))
    print("========================================")
  
if __name__ == '__main__':
    main()