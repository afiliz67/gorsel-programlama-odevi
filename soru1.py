# Girilen bir string ifadenin email adresi olup olmadığını
#doğrulayan python kodunu string metodları kullanmadan yazınız
# Örnek Email : ali.erbey@usak.edu.tr

import re

regex = '^([a-z0-9]+[\._])*[a-z0-9]+[@](\w+[.])+\w{2,3}$'

def check(email):
    if (re.search(regex, email)):
        print("Geçerli bir Email adresi")
    else:
        print("Geçersiz bir Email adresi")

a = input("Bir e-mail adresi giriniz : " )
b = check(a)

#=============== RESTART: D:\Afiliz\uşak\görsel\vize\soru1_yeni.py ==============
#Bir e-mail adresi giriniz : afiliz67@gmail.com
#Geçerli bir Email adresi
#>>> 
#=============== RESTART: D:\Afiliz\uşak\görsel\vize\soru1_yeni.py ==============
#Bir e-mail adresi giriniz : filiza99@hotmail.com
#Geçerli bir Email adresi
#=============== RESTART: D:\Afiliz\uşak\görsel\vize\soru1_yeni.py ==============
#Bir e-mail adresi giriniz : afiliz at usak.edu.tr
#Geçersiz bir Email adresi
#>>> 
