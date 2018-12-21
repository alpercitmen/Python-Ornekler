def asalBul(sayi):
    if sayi > 1: # girilen sayı 1'den büyük olmalı
        for i in range(2, sayi): # 2 ile girilen sayı arasındaki sayılar kotrol ediliyor
            if sayi % i == 0: # eğer girilen sayı 1 ve kendisi dışında bir sayıya tam bölünüyorsa
                print(sayi, ": sayı asal DEĞİL") # sayı asal değildir
                break # döngüden çık
            else:
                if i == (sayi-1):  # eğer girilen sayı 1 ve kendisi dışında bir sayıya tam bölünmüyorsa
                    print(sayi, ": sayı asal") # sayı asaldır
    else:
        print("2 ya da daha büyük bir sayı girin")
        
        
