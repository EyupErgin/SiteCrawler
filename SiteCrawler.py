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
    print(Fore.WHITE+"Example Usage: python3 SiteCrawler.py -s example.com ")

try:
    print("""
Project Name : SiteCrawler
Created : https://github.com/EyupErgin
Github  : https://github.com/IntelSights/SiteCrawler/
""")

    dosya = open("export.txt","w")
    txt = open("export.txt")
    link = sys.argv[2]
    denetle = link.split(".")

    if re.findall(":",denetle[0]):
        bilgi()
        sys.exit()

    d_link = "http://"+link
    print("Scan Started >  "+link)


    br.open(d_link)
    for links in br.links():
        if re.findall(denetle[1],links.url):
            dosya.write(links.url+"\n")
        else:
            dosya.write(d_link+links.url+"\n")
    print("Completed. Written to File. Open it > export.txt")
    print("")
except:
    bilgi()

