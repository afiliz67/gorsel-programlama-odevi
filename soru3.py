#Girilen bir string ifadede aranan bir ifade bulunduğunda bir
#onceki ve bir sonraki
#karakteri ekrana getiren python kodunu yazınız.
#• Girilen ifade : “Usak Universtesi”
#• Aranan ifade : ver
#• Sonuc : ivers
#
#ifade =input("Herhangi bir ifade giriniz : ")
#ifade ="Manchester Üniversitesi ingiltere"
ifade="Denizli Pamukkale Ünivesitesi"
#ifade ="mugla sıtkı koçman Universitesi"
#ifade="Manisa Celal Bayar Üniversitesi"
#ifade="usak universitesi"
ara =input("Aranacak bir ifade giriniz : ") # mesela "ch" girsem
index = ifade.find(ara)
if index != -1:
    if index == 0:
        print (ifade[0:index+len(ara)+1])
    print(ifade[index - 1:index + len(ara) + 1])

#====== RESTART: D:\Afiliz\uşak\görsel\vize\soru3_yeni.py =======
#Aranacak bir ifade giriniz : ukkal
#mukkale
#>>> 
