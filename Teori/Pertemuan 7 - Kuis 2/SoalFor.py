# File : SoalFor.py
# Program untuk cetak angka
# N:var.input untuk nilai awal(integer)
# M:var.input utk nilai akhir(integer)
# i:var.counter untuk for (integer)

def main():
    N = int(input("N: "))
    M = int(input("M: "))

    for i in range(N,M,2):
        if(i % 3 == 0):
            print("Haii",end=" ")
        elif(i % 2 == 0):
            print("semangat",end=" ")
        else:
            print("selalu", end=" ")

if __name__ == '__main__':
    main()