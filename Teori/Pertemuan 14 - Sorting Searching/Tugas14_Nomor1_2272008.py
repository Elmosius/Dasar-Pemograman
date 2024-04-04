# File : Tugas14_Nomor1_2272008.py
# Penulis : Elmosius Suli
# Tujuan : rogram yang menginput N nama mahasiswa ke dalam array nama.
# Program akan mengurutkan nama dari abjad terkecil sampai dengan terbesar

# Fungsi IsiArray()
# fungsi menginput nilai n
# fungsi menginput data, simpan ke array
# fungsi mengirimkan nilai n
# Kamus Global :
# nama : var. array(str)
# Kamus Lokal :
# N : var. input N(int)
# i : var. parameter(int)

def IsiArray():
    global nama
    N = int(input("N : "))

    for i in range(0, N, 1):
        nama[i] = str(input("nama: "))

    return (N)

# Fungsi PrintArray(N)
# fungsi utk cetak data dalam array ke layar
# Kamus Global :
# nama : var. array(str)
# Kamus Lokal :
# N : var. parameter fungsi(int)
# i : var. parameter(int)


def PrintArray(N):
    global nama
    print("--------------------------------")
    print("Daftar nama terurut abjad :")
    for i in range(0, N, 1):
        print(i+1, '.', nama[i])
    print("--------------------------------")

# Fungsi SortedSearch(N,X)
# fungsi untuk mencari nilai X dalam array terurut
# Kamus Global :
# nama : var. array(str)
# Kamus Lokal :
# i : var. parameter(int)
# N : var. parameter fungsi(int)
# X : var. parameter fungsi(str)
# ix : var. index(int)


def SortedSearch(N, X):
    global nama
    i = 0
    while (i < N-1 and nama[i] < X):
        i = i + 1
    if (nama[i] == X):
        ix = i  # A[ix] = X : data ditemukan
    else:
        ix = -1  # data tidak ditemukan
    return ix

# Fungsi Minsort(N)
# fungsi mengurutkan data sehingga terurut dari kecil ke besar
# Kamus Global :
# nama : var. array(str)
# Kamus Lokal :
# N : var. parameter fungsi(int)
# i : var. parameter (int)
# imin : var. index (int)
# temp : var. data temp(str)


def Minsort(N):
    global nama
    for i in range(0, N-1, 1):
        imin = i
        for j in range(i+1, N, 1):
            if nama[j] < nama[imin]:
                imin = j
        temp = nama[i]
        nama[i] = nama[imin]
        nama[imin] = temp

    return

## Program Utama ##
# Kamus Lokal
# N : var. dari fungsi IsiArray (int)
# cari_nama : var. mencari nama yang dicari(str)
# pos : var. index nama yang dicari dari fungsi SortedSearch(int)


def main():
    # panggil fungsi IsiArray()
    N = IsiArray()

    # panggil fungsi Minsort(N)
    Minsort(N)

    # panggil fungsi PrintArray(N)
    PrintArray(N)

    # input nama yang dicari
    cari_nama = str(input("nama yang dicari : "))

    # panggil fungsi SortedSearch(N,nama)
    SortedSearch(N, cari_nama)

    pos = SortedSearch(N, cari_nama)
    if (pos >= 0):
        if (pos == N-1):
            print('sebelum', cari_nama, ':', nama[pos-1])
        elif (pos == 0):
            print('sesudah', cari_nama, ':', nama[pos+1])
        else:
            print(cari_nama, "di antara", nama[pos-1], 'dan', nama[pos+1])

    else:
        # print pesan "nama tidak ditemukan"
        print("nama", cari_nama, "tidak terdaftar")


if __name__ == '__main__':
    # Kamus Global
    # nama : var. array(str)
    global nama
    Nmax = 100
    nama = Nmax * [None]  # deklarasi array nama var.global
    main()
