#Girilen bir string ifadenin url olup olmadığını doğrulayan python kodunu
#string metodları kullanmadan yazınız.
#• Ornek URL : www.alierbey.com 

import re


def isValidURL(str):
    p = re.compile('^(([^:/?#]+):)?(//([^/?#]))?([^?#])(\?([^#]))?(#(.))?')
    if re.search(p, str):
        return True
    else:
        return False


url = input("Bir web adresi giriniz : " )

if isValidURL(url):
    print("Bu bir URL adresidir")
else:
    print("Bu bir URL adresi değildir")
    
#======== RESTART: D:\Afiliz\uşak\görsel\vize\soru2_yeni.py ==========
#Bir web adresi giriniz : 
#======== RESTART: D:\Afiliz\uşak\görsel\vize\soru2_yeni.py ========
#Bir web adresi giriniz : www.hotmail.com
#Bu bir URL adresidir
#>>> 
#===== RESTART: D:\Afiliz\uşak\görsel\vize\soru2_yeni.py ==========
#Bir web adresi giriniz : www.maths.mancheter.ac.uk
#Bu bir URL adresidir
#>>> 
