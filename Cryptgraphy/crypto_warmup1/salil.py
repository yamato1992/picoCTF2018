key = list('thisisalilkey')
e = list('llkjmlmpadkkc')

start = ord('a')
end = ord('z')

ans = []

for k, c in zip(key, e):
    shift = ord(k) - start
    ascii_num = ord(c) - shift
    if ascii_num < start:
        ascii_num = end + 1 - (start - ascii_num)
    ans.append(chr(ascii_num))

print('picoCTF{%s}' % ''.join(ans).upper())