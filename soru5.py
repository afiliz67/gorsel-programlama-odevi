# soru 5
#input="receive-23-1-0"
#input="send-181-3-0-1"
#input="send-181-3-0-1\nreceive-170-3-0\n"
#input="receive-150-0-1"
input = "receive-150-0-1\n0-4-5-6-\n"
commands = input.split("\n")


def bolum_bir_gecerlimi(deger: int):
    return 0 <= deger <= 255


def bolum_iki_gecerlimi(deger: int):
    return 1 <= deger <= 4


def bolum_uc_ve_dort_gecerlimi(deger: int):
    return deger == 0 or deger == 1


def sinyal_gucu(deger: int):
    if deger < 51:
        return "Cok Zayif Sinyal"
    elif deger < 101:
        return "Zayif Sinyal"
    elif deger < 151:
        return "Orta Sinyal"
    elif deger < 201:
        return "Guclu Sinyal"
    else:
        return "Cok Guclu Sinyal"


def cihaz_turu(tur: int):
    if tur == 1:
        return "Televizyon"
    elif tur == 2:
        return "Camasir Makinesi"
    elif tur == 3:
        return "Buzdolabi"
    else:
        return "Firin"


def durumu(durum: int):
    if durum == 0:
        return "Off"
    else:
        return "On"


def cevap_isteniyormu(cevap: int):
    if cevap == 0:
        return "Cevap istenmiyor"
    else:
        return "Cevap isteniyor"


i = 1
for c in commands:
    if len(c) > 0:
        p = c.split("-")
        hata_tip = 0
        if p[0] == "receive":
            if not bolum_bir_gecerlimi(int(p[1])):
                hata_tip = 1
            if not bolum_iki_gecerlimi(int(p[2])):
                hata_tip = 2
            if not bolum_uc_ve_dort_gecerlimi(int(p[3])):
                hata_tip = 3
            kod = "Gelen"
        elif p[0] == "send":
            if not bolum_bir_gecerlimi(int(p[1])):
                hata_tip = 1
            if not bolum_iki_gecerlimi(int(p[2])):
                hata_tip = 2
            if not bolum_uc_ve_dort_gecerlimi(int(p[3])):
                hata_tip = 3
            if not bolum_uc_ve_dort_gecerlimi(int(p[4])):
                hata_tip = 4
            kod = "Giden"
        else:
            hata_tip = 5

        if hata_tip == 0:
            print("Kod Tipi : " + p[0] + " - " + kod)
            print("Sinyal Gucu : " + p[1] + " - " + sinyal_gucu(int(p[1])))
            print("Cihaz : " + p[2] + " - " + cihaz_turu(int(p[2])))
            print("Durumu: " + p[3] + " - " + durumu(int(p[3])))
            if p[0] == "send":
                print("Cevap : " + p[4] + " - " + cevap_isteniyormu(int(p[4])))
        elif hata_tip == 1:
            print("Error : birinci bolum hatali")
        elif hata_tip == 2:
            print("Error : ikinci bolum hatali")
        elif hata_tip == 3:
            print("Error : ucuncu bolum hatali")
        elif hata_tip == 4:
            print("Error : dorduncu bolum hatali")
        else:
            print("Error : send ya da receive icermiyor")

        if i < len(commands) - 1:
            i = i + 1
            print("------")

#=============== RESTART: D:/Afiliz/uşak/görsel/vize/soru5_yeni.py ==============
#Error : ikinci bolum hatali
#------
#Error : send ya da receive icermiyor
#>>> 
