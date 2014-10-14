__author__ = 'johannes'

import math
import random

# Erzeuge Zufallszahl zwischen 0 und 1000
zahl_cpu = int(random.random()*1000)

# Geht auch:
#zahl_cpu = random.randint(0,1000)

zahl_spieler = -1
versuche = 0

print "Errate meine Zahl! (Zwischen 0 und 1000)"

while zahl_spieler != zahl_cpu:
    versuche += 1
    zahl_spieler = int(raw_input(">>"))

    if zahl_spieler < zahl_cpu:
        print "Meine Zahl ist grosser"
    elif zahl_spieler > zahl_cpu:
        print "Meine Zahl ist kleiner"

print "Toll! Du hast meine Zahl erraten (Mit ", versuche, " Versuchen)"