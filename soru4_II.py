# Üç basamaklı rakamları biririnden farklı
# 648 doğal sayısı yazdıran Python kodu
sayac=1
for x in range(1,10):
    for y in range(0, 10):
        for z in range(0, 10):
            if x != y and y != z and x != z :
                #print(str(x) + str(y) + str(z))
              print(sayac,".rakmaları birbirinden farklı üç basmaklı sayı = ",str(x) + str(y) + str(z), " dir")
              sayac=sayac+1


#=============== RESTART: D:\Afiliz\uşak\görsel\vize\soru4_yeni.py ==============
#1 .rakmaları birbirinden farklı üç basmaklı sayı =  102  dir
#2 .rakmaları birbirinden farklı üç basmaklı sayı =  103  dir
#..................................
#647 .rakmaları birbirinden farklı üç basmaklı sayı =  986  dir
#648 .rakmaları birbirinden farklı üç basmaklı sayı =  987  dir
#>>> 
