# File : PR03A_2272008.py
# Program Koordinat
# program yang akan menentukan posisi dari sebuah titik terhadap titik acuan. 
# ---- Kamus Data ----
# ta_x dan ta_y : var. titik acuan (int)
# tx dan ty : var. titik (int)
# p : var. print terletak di mana (str)

def main():
    # Perintah Input
    ta_x = int(input("titik acuan x: "))
    ta_y = int(input("titik acuan y: "))
    tx = int(input("titik x: "))
    ty = int(input("titik y: "))

    # Perintah Proses
    if(tx > ta_x ):
        if(ty > ta_y):
            p = ("terletak disebelah kanan atas titik acuan")
        elif(ty < ta_y):
            p = ("terletak disebelah kanan bawah titik acuan")
        else:
            p = ("terletak disebelah kanan titik acuan")    
    elif(tx < ta_x ):
        if(ty > ta_y):
            p = ("terletak disebelah kiri atas titik acuan")
        elif(ty < ta_y):
            p = ("terletak disebelah kiri bawah titik acuan")   
        else:
            p = ("terletak disebelah kiri titik acuan")     
    else:
        if(ty > ta_y):
            p = ("terletak disebelah atas titik acuan")
        elif(ty < ta_y):
            p = ("terletak disebelah bawah titik acuan")
        else:     
            p = ("memiliki posisi yang sama dengan titik acuan") 
    # Perintah Output
    print('titik','(',tx,',',ty,')', p,end=" ") 
    print('(',ta_x,',',ta_y,')')    

    return 0
        
if __name__ == '__main__':
    main() 