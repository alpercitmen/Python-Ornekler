def şifrele(gizlenecek_yazı, anahtar):
    harfler = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z',' ', '.', ',']

    gizli_yazı = []

    for yazı in gizlenecek_yazı:
        for harf in harfler:
            if harf == yazı:
                harf_değer = harfler.index(harf)
                harf_değer += int(anahtar)
                if harf_değer > int(len(harfler)) - 1:
                    while True:
                        harf_değer -= int(len(harfler))
                        if harf_değer < int(len(harfler)):
                            break
                gizli_yazı.append(harfler[harf_değer])
    return ''.join(gizli_yazı)

def şifre_çöz(şifreli_yazı, anahtar):
    harfler = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z',' ', '.', ',']
    
    çözülen_yazı = []
    
    for şifre in şifreli_yazı:
        for harf in harfler:
            if şifre == harf:
                harf_değer = harfler.index(harf)
                harf_değer -= int(anahtar)
                if harf_değer < 0:
                    while True:
                        harf_değer += int(len(harfler))
                        if harf_değer >= 0:
                            break
                çözülen_yazı.append(harfler[harf_değer])
    return ''.join(çözülen_yazı)


işlem = int(input("Şifreleme için 1\nŞifre çözmek için 2 girin!"))

if işlem == 1:
    gönder = input("Şifrelemek istediğiniz yazıyı girin: ")
    anahtar = input("Şifreleme anahtarı girin: ")
    sonuç = şifrele(gönder, anahtar)
    print("şifreli:", sonuç)
else:
    gönder = input("Çözmek istediğiniz yazıyı girin: ")
    anahtar = input("Şifreleme anahtarı girin: ")
    çöz = şifre_çöz(gönder, anahtar)
    print("çözülmüş:", çöz)












