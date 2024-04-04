# File : PR07B_2272008.py
# Penulis : Elmosius Suli
# Tujuan Program : program yang akan menerima masukan bilangan a, bilangan b
# dan operator (+,-,*,/,%,**) c.

# fungsi operator Tambah
# Kamus Lokal
# a : var. parameter (int)
# b : var. parameter (int)
# hasil : var. hasil pertambahan (int)

def operatorTambah(a,b):
    hasil = a + b
    print(a, '+', b, '=', hasil)

# fungsi operator kurang
# Kamus Lokal
# a : var. parameter (int)
# b : var. parameter (int)
# hasil : var. hasil kurang (int)

def operatorKurang(a,b):
    hasil = a - b
    print(a, '-', b, '=', hasil)

# fungsi operator kali
# Kamus Lokal
# a : var. parameter (int)
# b : var. parameter (int)
# hasil : var. hasil kali (int)

def operatorKali(a,b):
    hasil = a*b
    print(a, '*', b, '=', hasil)

# fungsi operator bagi
# Kamus Lokal
# a : var. parameter (int)
# b : var. parameter (int)
# hasil : var. hasil bagi (float)

def operatorBagi(a,b):
    hasil = a / b
    print(a, '/', b, '=', hasil)
    
# fungsi operator modulo
# Kamus Lokal
# a : var. parameter (int)
# b : var. parameter (int)
# hasil : var. hasil modulo (int)
    
def operatorModulo(a,b):
    hasil = a % b
    print(a, '%', b, '=', hasil)

# fungsi operator pangkat
# Kamus Lokal
# a : var. parameter (int)
# b : var. parameter (int)
# hasil : var. hasil perpangkatan (int)

def operatorPangkat(a,b):
    hasil = a**b
    print(a, '**', b, '=', hasil)
    
## Program Utama ##
# Kamus Lokal
# a : var. input a (int)
# b : var. input b (int)
# c : var. syarat khusus a<b (int)
# operator : var. input operator (str)

def main():
    # input
    a = int(input("a: "))
    b = int(input("b: "))
    operator = str(input("c: "))
    
    # proses syarat khusus
    if (a < b):
        c = b
        b = a
        a = c
        
    # pilihan operator
    print("Perhitungan: ")
    if (operator == '+'):
        operatorTambah(a,b)
    elif(operator == '-'):
        operatorKurang(a,b)
    elif(operator == '/'):
        operatorBagi(a,b)
    elif(operator == '*'):
        operatorKali(a,b)
    elif(operator == '%'):
        operatorModulo(a,b)
    else:
        operatorPangkat(a,b)
        
if __name__ == '__main__':
    main()