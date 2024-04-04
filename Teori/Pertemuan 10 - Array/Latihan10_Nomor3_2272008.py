# File : Latihan10_Nomor3_2272008.py
# Penulis : Elmosius Suli
## Definisi Fungsi ##

def main():
    #K berisi string
    #string adalah suatu array
    #len : fungsi utk hitung banyaknya karakter dlm string
    K = str(input("Kalimat :"))
    N = len(K)
    a = 0
    for i in range (0,N,1):
        if (K[i] == 'a'):
            a = a + 1
    print("kemunculan huruf a :",a)
    
if __name__ == '__main__':
    main()
    
# input : aku cinta kaka
# output : 
# kemunculan huruf a : 4