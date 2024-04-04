# File: Tugas2_Nomor1_2272008.py
# Penulis : Elmosius Suli
# Program membaca 3 bilangan bulat a,b,c, diminta mencetak seperti dalam contoh.
# Kamus Data
# a, b , dan c (int)
# menggunakan operasi perbandingan (>, <) 
# menggunakan operasi boolean (and) 

def main ():
                
# Program Input

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

# Output
    if(a > b and b < c ):
        print("Nilai ", c, "di antara", a, "dan", b)
    elif(a < b and b > c):
        print("Nilai ", a, "di antara", b, "dan", c)
    else:   
        print("Nilai ", b, "di antara", a, "dan", c)      

if __name__ == '__main__':
    main()