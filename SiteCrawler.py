import mechanize,sys,re
import requests
import txt
import os 
from colorama import Fore, Back, Style, init
init(autoreset=True)
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('user-agent',
                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]

def bilgi():
    print("""
###      ###  _____         _    ___     _     _   
#	       o # |_   _|  _ _ _| |__/ _ \ __(_)_ _| |_ 
	             | || || | '_| / / (_) (_-< | ' \  _|
               |_| \_,_|_| |_\_\ \__//__/_|_||_\__|
#	         # Proje Adı: https://github.com/TurkOsint
###      ### Kodlayan : https://github.com/EyupErgin
""")

    print(Fore.WHITE+"[TurkOsint] Örnek Kullanım: python crawler.py google.com")

try:
    print("""
###      ###  _____         _    ___     _     _   
#	       o # |_   _|  _ _ _| |__/ _ \ __(_)_ _| |_ 
	             | || || | '_| / / (_) (_-< | ' \  _|
               |_| \_,_|_| |_\_\ \__//__/_|_||_\__|
#	         # Proje Adı: https://github.com/TurkOsint
###      ### Kodlayan : https://github.com/EyupErgin
""")

    dosya = open("sonuc.txt","w")
    txt = open("sonuc.txt")
    link = sys.argv[1]
    denetle = link.split(".")

    if re.findall(":",denetle[0]):
        bilgi()
        sys.exit()

    d_link = "http://"+link
    print("[TurkOsint] Tarama Başladı >  "+link)


    br.open(d_link)
    for links in br.links():
        if re.findall(denetle[1],links.url):
            dosya.write(links.url+"\n")
        else:
            dosya.write(d_link+links.url+"\n")
    print("[TurkOsint] Tamamlandı. Dosyaya Yazıldı. Açınız. >> sonuc.txt")
    print("")
except:
    bilgi()

