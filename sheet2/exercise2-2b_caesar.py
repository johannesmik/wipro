# -*- coding: utf-8 -*-
"""
Encode a string using the Caesar cipher.

This version ensures that the shifted text is again element of a-z.

Issues:
    - What happens to special characters like '?' or '.' ?

Author: Johannes, October 2013
Revised: Johannes, October 2014
"""

text = "Hallo das ist ein Test"
shift = -3
ciphertext = ""
alphabet_size = 26

# Text preprocessing
text = text.lower()
text = text.replace(" ", "")

# Ensure that shift is between 0 and 25
shift = shift % 26

# Shift each character, and append to new string ciphertext
for character in text:
    ordinal = ord(character)
    shifted_ordinal = ordinal + shift

    # Get sure that the shifted ordinal is again between ord('a') and ord('z')!
    if shifted_ordinal > ord('z'):
        shifted_ordinal -= alphabet_size
    elif shifted_ordinal < ord('a'):
        shifted_ordinal += alphabet_size

    shifted_character = chr(shifted_ordinal)
    ciphertext += shifted_character

print "Original text:", text
print "Cipher text:", ciphertext
