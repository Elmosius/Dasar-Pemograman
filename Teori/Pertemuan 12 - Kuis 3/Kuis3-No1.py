# File : Kuis3-no1.py
# Program dgn Function
## Definisi Fungsi FX
# kamus lokal
# x,y : parameter fungsi FX (integer)
# s : var. jumlah (integer)
# i : var. counter (integer)

def FX(x,y):
    s = 10
    i = 2
    while (i < x):
        s = s - y
        i = i + 3
    return s
 
## Program utama ##
# Kamus Data
# p : var. utk input nilai p(integer)
# q : var. utk input nilai q(integer)
def main():
    p = int(input("Nilai p :"))
    q = int(input("Nilai q :"))
    print ("nilai FX :", FX(p,q))
    print ("nilai FX :", FX(p-q,p))
    print ("nilai FX(FX) :", FX(FX(q,p),p*2))
           
if __name__ == '__main__':
    main()

# input
# p : 9
# q : 2

# output
# nilai FX : 4
# nilai FX : -8
# nilai FX(FX) : -44