
def main():
    A = 5 * [None]
    B = 5 * [None]
    
    for i in range(0,5,1):
       A[i] = int(input(""))
       
    j = 4
    for i in range(0,5,1):
        B[j] = A[i]
        j = j-1  
       
    for i in range(0,5,1):
        print(B[i])
if __name__ == '__main__':
    main()