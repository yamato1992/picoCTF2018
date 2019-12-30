def rot13(c):
    if 'A' <= c and c <= 'Z':
        return chr((ord(c) - ord('A') + 13) % 26 + ord('A'))

    if 'a' <= c and c <= 'z':
        return chr((ord(c) - ord('a') + 13) % 26 + ord('a'))

    return c

encrypt_str = list(input('encrypt string:'))
print(''.join([rot13(c) for c in encrypt_str]))
