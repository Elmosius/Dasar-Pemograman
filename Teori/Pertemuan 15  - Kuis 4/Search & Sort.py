def seqSearch1(x):
    ketemu = False
    i = 0
    while (i < N and not ketemu):
        if (arrA[i] == x):
            ketemu = True
        else:
            i += 1

    if (ketemu):
        ix = i
    else:
        ix = -1

    return ix


def SortedSearch(x):
    i = 0
    while (i < N-1 and arrA[i] < x):
        i += 1
    if (arrA[i] == x):
        ix = i
    else:
        ix = -1

    return ix


def SentinelSearch(x):
    arrA[N] = x
    i = 0
    while (arrA[i] != x):
        i += 1

    if (i < N):
        ix = i
    else:
        ix = -1

    return ix


def BinSearch(x):
    ketemu = False
    atas = 0
    bawah = N-1
    ix = -1

    while (atas <= bawah and not ketemu):
        tengah = (atas + bawah) // 2

        if (arrA[tengah] == x):
            ketemu = True
            ix = tengah
        elif (x < arrA[tengah]):
            bawah = tengah - 1
        else:
            atas = tengah + 1

    return ix


def Maxsort():

    for i in range(0, N-1, 1):
        imax = i
        for j in range(i+1, N, 1):
            if (arrA[j] > arrA[imax]):
                imax = j
        temp = arrA[i]
        arrA[i] = arrA[imax]
        arrA[imax] = temp

    return (arrA)


def insertionSort():
    for i in range(1, N, 1):
        tem = arrA[i]
        j = i-1

        while (tem < arrA[j] and i > 0):
            arrA[j+1] = arrA[j]
            j -= 1
            if (tem >= arrA[j]):
                arrA[j+1] = tem
            else:
                arrA[j+1] = arrA[j]
                arrA[j] = tem
    return (arrA)


def main():
    # input
    for i in range(0, N, 1):
        arrA[i] = int(input())
    x = int(input("Angka yang mau dicari : "))

    # Sorting ================
    # MaxSort
    # arrB = Maxsort()

    # for i in range(0,N,1):
    #     print(arrB[i], end=" ")

    # InsertionSort
    arrC = Maxsort()

    for i in range(0, N, 1):
        print(arrC[i], end=" ")

    # print("SeqSearch 1")
    # a = seqSearch1(x)

    # if (a >= 0):
    #     print("Data X ada di  A[", i, "]")
    # else:
    #     print("Data X tidak ada dlm A")

    # print("="*25)
    # print("Sorted Search")
    # b = SortedSearch(x)

    # if (b >= 0):
    #     print("Data X ada di  A[", i, "]")
    # else:
    #     print("Data X tidak ada dlm A")

    # print("="*25)
    # print("Sentinel")
    # c = SentinelSearch(x)

    # if (c >= 0):
    #     print("Data X ada di  A[", i, "]")
    # else:
    #     print("Data X tidak ada dlm A")

    # print("="*25)
    # print("Binary Search")
    # d = BinSearch(x)

    # if (d >= 0):
    #     print("Data X ada di  A[", i, "]")
    # else:
    #     print("Data X tidak ada dlm A")


if __name__ == '__main__':
    global N, arrA
    N = int(input("N :"))
    arrA = N * [None]

    main()
