import os



def encript_content():
    # HINT: For Part 2, you'll need to decrypt the contents of this file
    # The existing scheme plaintext
    # As such, we just convert it back to ASCII and print it out
    ascii = open('index.txt', 'r').read()
    x=[i for i in ascii]
    print(x)
    enc = ' '.join(str(ord(c)) for c in ascii)
    print(enc)
encript_content()    