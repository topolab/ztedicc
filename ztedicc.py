#!/bin/python
 
import sys
 
zteOUI = ['02DC81', '262C21', '262C24', '262C4C', '2C26C5', '34E0CF', '404A03',
'8C86C5', 'A0EC80', 'A1EC81', 'DC016E', 'DC028E']
 
 
def main():
    if len(sys.argv) != 2:
        print "Uso: %s <ssid>" % (sys.argv[0])
        print "Ej.: %s WLAN_ABCD" % (sys.argv[0])
        exit(1)
 
    ssid = sys.argv[1]
 
    if ssid.index("WLAN_") != 0:
        print "La configuracion de la WiFi no parece estar por defecto :("
        exit(1)
 
    hexa = "0123456789ABCDEF"
    ends = ssid[-4:]
    for oui in zteOUI:
        for i in range(0, 16):
            for j in range(0, 16):
                print "Z%s%c%c%s" % (oui, hexa[i], hexa[j], ends)
 
 
if __name__ == "__main__":
    main()
