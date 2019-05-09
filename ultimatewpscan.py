#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Ultiwpscan")
print(""" 
   111111111   11111111111         111111111111111    1  111111111
   1                     1         1      1      1    1  1
   1                    1          1      1      1    1  1
   1                   1           1      1      1    1  11111111
   1   11111          1            1      1      1    1  1       1
   1      11         1             1      1      1    1  1       1
   111111111        1111111111     1      1      1  . 1  111111111

wpscan      (CAN BALI THT) 

1) wpscan-pluginsip
2) wpscan-users 
3) wpscan-themes
4) wpscan-normaltarama
5) wpscan-help
6) wpscan-ultipluginsip
7) wpscan-update

""")

islemno = input("Islem No Girin: ")
if (islemno=="1"):
       wpscanip = input("Wpscan için wordpress İp Girin: ")
       os.system("wpscan --url " + wpscanip + " --enumerate p ")
elif (islemno=="2"):
       wpscanip = input("Wpscan için wordpress İp Girin: ")
       os.system("wpscan --url " + wpscanip + " --enumerate u ")
elif (islemno=="3"):
       wpscanip = input("Wpscan için wordpress İp Girin: ")
       os.system("wpscan --url " + wpscanip + " --enumerate t ")
elif (islemno=="4"):
       wpscanip = input("Wpscan için wordpress İp Girin: ")
       os.system("wpscan --url " + wpscanip )
elif (islemno=="5"):
       os.system("wpscan --help ")
elif (islemno=="6"):
       wpscanip = input("Wpscan için wordpress İp Girin: ")
       os.system("wpscan --url " + wpscanip + " --enumerate ap ")
elif (islemno=="7"):
       wpscanip = input("Wpscan için wordpress İp Girin: ")
       os.system("wpscan --update ")


else:
       print("hatali tuşlama kanki ")





 



