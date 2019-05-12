import random
print("""
#####################################
#                                   #
#       Zar Atma Simülasyonu        #
#                                   #
#       1 - Tek Zar                 #
#       2 - Çift Zar                #
#       3 - Çıkış                   #
#                                   #
#####################################
""")
while True:
    try:
        zarSayisi = int(input("Tek zar mı Çift zar mı?: "))
        if zarSayisi == 1:
            zar = random.randint(1,6)
            print(zar)
        elif zarSayisi == 2:
            zar1 = random.randint(1,6)
            zar2 = random.randint(1,6)
            print(str(zar1) + " - " + str(zar2))
        elif zarSayisi == 3:
            break
        else:
            print("Hatalı değer girdiniz! Tekrar deneyin.")
    except ValueError:
        print("Hatalı değer girdiniz! Tekrar deneyin.")
