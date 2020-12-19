# Üç basamaklı rakamları biririnden farklı
# 648 doğal sayısı yazdıran Python kodu
sayac =0
for i in range(100,999):
    a=int(i/100)
    b=int((i%100)/10)
    c=int(i%10)
    if(a != b and a != c and b != c):
      # print("üç basamaklı sayı :",i) 
       sayac = sayac+1
      # print(sayac, ".sayı = ",sayac )
       print(sayac, ". rakmaları birbirinden farklı üç basmaklı sayı = ",i, "dir") 
