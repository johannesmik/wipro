"""
Caesar Cipher

Author: Johannes, October 2013
Revised: Johannes, October 2014
"""

def encode(text, shift):
    """
    Encode a string using the Caesar cipher.

    Issues:
        - What happens to special characters like '?' or '.' in the text?
    """

    ciphertext = ""
    alphabet_size = 26

    # Text preprocessing
    text = text.lower()
    text = text.replace(" ", "")

    # Ensure that shift is between 0 and 25
    shift %= 26

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

    return ciphertext

def decode(text, shift):
    return encode(text, -shift)

if __name__ == "__main__":
    print "Encode 'Hallo Welt' with shift=10: ", encode('Hallo Welt', 10)
    print "Decode 'nomynsxqgybuc' with shift=10: ", decode('nomynsxqgybuc', 10)