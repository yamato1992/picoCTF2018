import re
import string

with open('./ciphertext') as f:
    s = f.read()

m = re.search(r'{.*}', s)
cipher_txt = m.group()[1:-1]
alphabet = list(string.ascii_lowercase)

for i in range(1, 26):
    plain_txt = ''
    for c in cipher_txt:
            plain_txt += alphabet[(alphabet.index(c) + i) % 26]
    print('picoCTF{%s}' % plain_txt)