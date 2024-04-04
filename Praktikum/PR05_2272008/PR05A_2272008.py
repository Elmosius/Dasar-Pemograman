# File : PR05A_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan membentuk 
# sebuah kalimat dari karakter yang diinput.
# Kamus Data :
# a : var. menyimpan huruf a (int)
# i : var. menyimpan huruf i (int)
# u : var. menyimpan huruf u (int)
# e : var. menyimpan huruf e (int)
# o : var. menyimpan huruf o (int)
# p : var. menyimpan semua huruf (str)
# h : var. input huruf (str)

def main():
    # inisialisasi
    a = 0
    i = 0
    u = 0
    e = 0
    o = 0
    p = ''
    
    # input
    h = str(input(""))
    
    # proses
    while (h != '.'):
        if(h == 'a'):
            a+= 1
        if(h == 'i'):
            i+= 1
        if(h == 'u'):
            u+= 1
        if(h == 'e'):
            e+= 1
        if(h == 'o'):
            o+= 1
        p += h
        h = str(input(""))
    
    # output
    print("Hasil Kalimat:")
    print(p,'.',sep="")   
    print("Huruf a = ",a)
    print("Huruf i = ",i)
    print("Huruf u = ",u)
    print("Huruf e = ",e)
    print("Huruf o = ",o) 

if __name__ == '__main__':
    main()