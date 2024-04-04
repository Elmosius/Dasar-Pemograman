# File : Tugas13_Nomor1_2272008.py
# Penulis : Elmosius Suli
# Tujuan : Program akan menghitung
# nilai rata-rata dari semua data, kemudian program akan
# mencetak tiga kelompok data (sebagai contoh).

# Fungsi matriks
# Kamus Lokal
# d1,d2 : var. paramter(int)
# i : var. parameter for(int)
# arr : var. array sementara(int)

def matriks(d1, d2):
    arr = [None]*d1
    for i in range(0, d1, 1):
        arr[i] = [None]*d2
    return arr

## Program Utama ##
# Kamus lokal
# N : var. input matriks n x n (int)
# A : var. array n x n (int)
# i, j : var. parameter(int)
# rata_rata : var. rata-rata(float)
# jumlah_data : var. jumlah data dalam matriks A(int)
# nilai_terbesar : var. nilai terbesar(int)
# nilai_terkecil : var. nilai terkecil (int)


def main():
    # input untuk N
    N = int(input("N = "))

    # panggil fungsi deklarasi matriks
    A = matriks(N, N)

    # input data ke dalam matriks A (pakai nested for)
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            print("A[", i, ",", j, "]:", end=" ")
            A[i][j] = int(input())

    # print matriks A (pakai nested for)
    print("Matriks A:")
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            print(A[i][j], end=" ")
        print()

    # hitung jumlah data yang ada dalam matriks A (pakai nested for)
    jumlah_data = 0
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            jumlah_data += A[i][j]

    # hitung rata-rata (pakai rumus)
    rata_rata = round(jumlah_data/(N*N), 1)

    # tentukan nilai terbesar, terkecil dalam matriks (pakai nested for)
    nilai_terbesar = A[0][0]
    nilai_terkecil = A[0][0]
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            if (A[i][j] > nilai_terbesar):
                nilai_terbesar = A[i][j]
            if (nilai_terkecil > A[i][j]):
                nilai_terkecil = A[i][j]

    # print nilai rata-rata
    print("Nilai rata-rata : ", rata_rata)

    # print nilai terbesar dan terkecil
    print("Nilai terbesar : ", nilai_terbesar)
    print("Nilai terkecil : ", nilai_terkecil)

    # print elemen pada baris-1 < rata-rata
    print("Kelompok data baris-1 yang <", rata_rata, ":", end=" ")
    for i in range(0, N, 1):
        if (rata_rata > A[0][i]):
            print(A[0][i], end=" ")
    print()
    # print elemen pada baris-2 < rata-rata
    print("Kelompok data baris-2 yang <", rata_rata, ":", end=" ")
    for i in range(0, N, 1):
        if (rata_rata > A[1][i]):
            print(A[1][i], end=" ")
    print()

    # print elemen pada baris-3 < rata-rata
    print("Kelompok data baris-3 yang <", rata_rata, ":", end=" ")
    for i in range(0, N, 1):
        if (rata_rata > A[2][i]):
            print(A[2][i], end=" ")


if __name__ == '__main__':
    main()
