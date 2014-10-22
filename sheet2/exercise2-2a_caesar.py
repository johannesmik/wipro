# -*- coding: utf-8 -*-
"""
Encode a string using the Caesar cipher.

Issues we have to fix:
    - What happens to characters like Z, and why?
    - What happens if the shift is negative?
    - What happens to 

Author: Johannes, October 2013
Revised: Johannes, October 2014
"""

text = "Hallo das ist ein Test."
shift = 3
ciphertext = ""

# Text preprocessing
text = text.lower()
text = text.replace(" ", "")

# Ensure that shift is between 0 and 25
shift = shift % 26

# Shift each character, and append to new string ciphertext
for character in text:
    ordinal = ord(character)
    shifted_ordinal = ordinal + shift
    shifted_character = chr(shifted_ordinal)
    ciphertext += shifted_character

print "Original text:", text
print "Cipher text:", ciphertext
