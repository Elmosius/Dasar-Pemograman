# File : Kuis1-1.py
# Penulis : Elmosius Suli
# Program Kuis1 - Aksi Sequential
# Kamus Data
# x : var. utk perhitungan(integer)
# y : var. utk input (integer)
# z : var. utk input (integer)

y = int (input("Nilai y :"))
z = int (input("Nilai z :"))

x = z // y
y = z % x + 1
y = y/((x + z)*(y - x))

print ("Nilai x : ",x)
print ("Nilai y baru : ",y)
print ("Nilai z baru : ",z)
