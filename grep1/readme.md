## grep 1

Problem
>Can you find the flag in file? This would be really obnoxious to look through by hand, see if you can find a faster way. You can also find the file in /problems/grep-1_3_8d9cff3d178c231ab735dfef3267a1c2 on the shell server.

1. login online shell.

2. move to tha folder.
```
8ma10@pico-2018-shell:~$ cd /problems/grep-1_3_8d9cff3d178c231ab735dfef3267a1c2
```

3. open file and grep 'picoCTF{'.
```
8ma10@pico-2018-shell:/problems/grep-1_3_8d9cff3d178c231ab735dfef3267a1c2$ cat file | grep picoCTF{
picoCTF{grep_and_you_will_find_cdf2e7c2}
```

FLAG - `picoCTF{grep_and_you_will_find_cdf2e7c2}`