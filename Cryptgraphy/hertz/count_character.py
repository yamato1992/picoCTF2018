from collections import Counter
from string import ascii_lowercase

with open('./cipher_txt.txt') as f:
    cipher_txt = f.read()

char_count = Counter(c for c in cipher_txt if c in ascii_lowercase)
total_chars = sum(char_count.values())

for char, count in char_count.items():
    rate = count * 100 / total_chars
    print(f'{char}: count:{count}, rate:{rate}')
