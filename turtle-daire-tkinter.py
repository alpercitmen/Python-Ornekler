#tkinter modülünden turtle kullanarak daire çizdiren kod
from turtle import *

kenar = 1
while True:
    forward(1) # her defasında 1 birim ilerleyecek
    right(1) # her defasında 1 derece dönecek
    kenar+=1
    if kenar == 360: # ilerleme ve dönemyi 360 kere yaptıktak sonra döngüden çıkacak
        break

