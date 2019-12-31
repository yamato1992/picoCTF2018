from colorama import Fore

with open('./cipher_txt.txt') as f:
    cipher_txt = f.read()

sub = {
    'a': 'p',
    'b': 'r',
    'c': 't',
    'd': 'x',
    'e': 'd',
    'f': 'b',
    'g': 'w',
    'h': 'v',
    'i': 'k',
    'j': 'o',
    'k': 'l',
    'l': 'y',
    'm': 'u',
    'n': 'f',
    'o': 'z',
    'p': 's',
    'q': 'h',
    'r': 'g',
    's': 'i',
    't': 'c',
    'u': 'e',
    'w': 'm',
    'x': 'n',
    'y': 'j',
    'z': 'a',
}

plain_txt = ''

for c in cipher_txt:
    if c in sub:
        c = c.replace(c, f'{Fore.GREEN}{sub[c]}{Fore.RESET}')
    plain_txt += c

print(plain_txt)
