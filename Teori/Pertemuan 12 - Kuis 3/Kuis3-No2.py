# File : Kuis3-No2.py
# Penulis : Elmosius Suli
# Tujuan :  Fungsi mengirimkan nilai tengah dari a,b,c,d,e
## Definisi Fungsi ##



# fungsi nilaiMid
# Kamus lokal

def nilaiMid(a,b,c,d,e):
    
    for i in range(0,5,1):
        if(a>b):
            x = a
            a = b
            b = x
        if(b>c):
            x = b
            b = c
            c = x
        if(c>d):
            x = c
            c = d
            d = x
        if(d>e):
            x = d
            d = e
            e = x
    print(c)
        

def main():
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))
    d = int(input(""))
    e = int(input(""))
    
    nilaiMid(a,b,c,d,e)
    
if __name__ == '__main__':
    main()
    
