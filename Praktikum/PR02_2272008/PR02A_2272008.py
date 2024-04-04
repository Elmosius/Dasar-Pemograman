# File : PR02A_2272008.py
# The Operators
# program yang akan menjalankan algoritma berikut, dimana operator yang dapat 
# diterima hanya +, -, *, dan /. 
# ---- Kamus Data ----
# angka_1, angka_2,dan angka_3 (int)
# operasi_1 dan operasi_2 (str)
# menggunakan operasi Boolean (and, or) 
# menggunakan operasi perbandingan (==, !=)
# menggunakan kondisi (if, elif)

def main():

    # program input angka
    angka_1 = int(input("angka1: "))
    angka_2 = int(input("angka2: "))
    angka_3 = int(input("angka3: "))

    # input operasi
    operasi_1 = str(input("operasi1: "))
    operasi_2 = str(input("operasi2: "))

    # output angka operasi

    if(operasi_1 == "+" and operasi_2 == "*"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 + angka_2)*angka_3)
    elif(operasi_1 == "+" and operasi_2 == "/"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 + angka_2)/angka_3)
    elif(operasi_1 == "+" and operasi_2 == "-"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 + angka_2)-angka_3)
    elif(operasi_1 == "+" and operasi_2 == "+"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 + angka_2)+angka_3)

    elif(operasi_1 == "-" and operasi_2 == "*"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 - angka_2)*angka_3)    
    elif(operasi_1 == "-" and operasi_2 == "/"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 - angka_2)/angka_3)             
    elif(operasi_1 == "-" and operasi_2 == "+"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 - angka_2)+angka_3)
    elif(operasi_1 == "-" and operasi_2 == "-"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 - angka_2)-angka_3)      

    elif(operasi_1 == "*" and operasi_2 == "+"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 * angka_2)+angka_3)
    elif(operasi_1 == "*" and operasi_2 == "-"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 * angka_2)-angka_3)             
    elif(operasi_1 == "*" and operasi_2 == "/"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 * angka_2)/angka_3) 
    elif(operasi_1 == "*" and operasi_2 == "*"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 * angka_2)*angka_3)    

    elif(operasi_1 == "/" and operasi_2 == "+"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 / angka_2)+angka_3)
    elif(operasi_1 == "/" and operasi_2 == "-"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 / angka_2)-angka_3)             
    elif(operasi_1 == "/" and operasi_2 == "/"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 / angka_2)/angka_3) 
    elif(operasi_1 == "/" and operasi_2 == "*"):
        print('(',angka_1,operasi_1, angka_2,')',operasi_2, angka_3,"= ", end="")
        print((angka_1 / angka_2)*angka_3)    
    elif(operasi_1 or operasi_2 != "+" or "-" or "/" or "*"):
        print("salah operator nih")
            
if __name__ == '__main__':
    main()     