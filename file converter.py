import os
import glob

girisUzanti = input("Hangi uzantıyı dönüştürmek istiyorusunuz?: ") #giriş dosyası uzantısı
sonucUzanti = input("Hangi uzantıda çıktı almak istiyorsunuz?: ") #çıkış dosyası uzantısı

dizin = os.path.dirname(os.path.realpath(__file__)) #dosyanın çalıştırıldığı dizin 
dosyalar = glob.glob("{0}/*.{1}".format(dizin, girisUzanti)) #girilen uzantıdaki dosyaları bul 

print(len(dosyalar), "dosya bulundu.\nDönüştürme başlıyor...")

for i in range(len(dosyalar)):
    yeni = dosyalar[i].split(".") #dosya adını ve uzantısı ayır (yeni[0] dosya adı, yeni[-1] dosya uzantısı)
    if yeni[-1] == girisUzanti:
        dosyaAd = yeni[0].split("/")[-1] #klasör isimleri haric dosya adı
        os.system('ffmpeg -i "'+dosyalar[i]+'" -acodec libmp3lame "$(basename "'+dizin+'/'+dosyaAd+'")".{0}'.format(sonucUzanti))
