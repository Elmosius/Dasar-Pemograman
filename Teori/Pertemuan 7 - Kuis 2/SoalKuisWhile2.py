# File : SoalKuisWhile2.py
# Program untuk jumlah data dengan while
# x : var.input utk nilai data x (integer)
# negatif : var.untuk pengendali (boolean)
# sum : var. utk hitung jumlah (integer)
    
def main():
 
    x = int(input("Nilai x :"))
    negatif = False
    sum = 0

    while (x != 9999) and (negatif == False):
        if (x % 2 == 0):
            sum = sum + x
            print(x)
            
        elif (x < 0):
            negatif = True
            sum = sum - x
        else:
            print(x)
            
        x = int(input("Nilai x :"))
    print("Jumlah :",sum)

if __name__ == '__main__':
    main()  
