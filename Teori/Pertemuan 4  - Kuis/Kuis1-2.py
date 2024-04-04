# File : Kuis1no2.py 
# Penulis : Elmosius Suli
# Program IF banyak kasus
# Kamus Data
# a : var. input (integer)
# b : var. input (integer)

a = int(input("Nilai a :"))
b = int(input("Nilai b :"))

if ((b // a) < 10):
    if ((a > 10) and (a == 50)):
        a = a % b
    else:
        b = b + a
else:
    b = b / a

print ("Nilai a: ",a,"Nilai b", b)