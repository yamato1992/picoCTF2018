## strings

Problem
>Can you find the flag in this file without actually running it? You can also find the file in /problems/strings_1_c7bac958dd6a4b695dc72446d8014f59 on the shell server.

1. login online shell server.

2. move the folder.
```
8ma10@pico-2018-shell:~$ cd /problemsstrings_1_c7bac958dd6a4b695dc72446d8014f59      
```
3. open file with strings command and grep 'pico'.
```
8ma10@pico-2018-shell:/problemsstrings_1_c7bac958dd6a4b695dc72446d8014f59$ strings strings | grep pico                             
picoCTF{sTrIngS_sAVeS_Time_d7c8de6c}
```

FLAG - `picoCTF{sTrIngS_sAVeS_Time_d7c8de6c}`
