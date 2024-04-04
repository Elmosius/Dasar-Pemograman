n = int(input("N:"))
a = n * [None]

for i in range (0, n, 1):
    a[i] = str(input(""))
    
cari = str(input("cari:"))

for i in range (0, n, 1):
    p = a[i].lower()
    b = len(a[i])
    