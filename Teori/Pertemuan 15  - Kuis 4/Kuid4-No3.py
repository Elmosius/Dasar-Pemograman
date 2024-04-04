# File : Kuis3-No3.py
# Penulis : Elmosius Suli
## Definisi Fungsi ##


def menaik(arrA):
    for i in range(0, N-1, 1):
        imin = i
        for j in range(i+1, N, 1):
            if arrA[j] < arrA[imin]:
                imin = j
        temp = arrA[i]
        arrA[i] = arrA[imin]
        arrA[imin] = temp

    for i in range(0, N, 1):
        print(arrA[i], end=" ")
    print()

def menurun(arrA):
    for i in range(0, N-1, 1):
        imax = i
        for j in range(i+1, N, 1):
            if arrA[j] > arrA[imax]:
                imax = j
        temp = arrA[i]
        arrA[i] = arrA[imax]
        arrA[imax] = temp

    for i in range(0, N, 1):
        print(arrA[i], end=" ")
    print()

def main():
    arrA = N * [None]
    for i in range(0, N, 1):
        arrA[i] = str(input(""))

    menaik(arrA)
    menurun(arrA)


if __name__ == '__main__':
    global N
    N = int(input("N: "))

    main()
