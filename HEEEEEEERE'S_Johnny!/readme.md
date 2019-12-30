## HEEEEEEERE'S_Johnny!

Problem
>Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with nc 2018shell.picoctf.com 40157. Files can be found here: passwd shadow.

1. make passfile.
```
8ma10$ unshadow passwd shadow > passfile
```

2. crack password with john the ripper.
```
8ma10$ john passfile
Warning: detected hash type "sha512crypt", but the string is also recognized as "HMAC-SHA256"
Use the "--format=HMAC-SHA256" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 2 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 6 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 4 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 5 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 3 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 5 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 7 candidates buffered for the current salt, minimum 8 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
password1        (root)
1g 0:00:00:00 DONE 2/3 (2019-12-30 01:21) 2.777g/s 3022p/s 3022c/s 3022C/s 123456..franklin
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

```
8ma10$ john --show passfile
root:password1:0:0:root:/root:/bin/bash

1 password hash cracked, 0 left
```

3. login with nc.
```
8ma10$ nc 2018shell.picoctf.com 40157
Username: root
Password: password1
picoCTF{J0hn_1$_R1pp3d_1b25af80}
```

FLAG - `picoCTF{J0hn_1$_R1pp3d_1b25af80}`