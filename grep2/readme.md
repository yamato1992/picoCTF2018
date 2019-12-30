## grep 2

Problem
>This one is a little bit harder. Can you find the flag in /problems/grep-2_0_783d3e2c8ea2ebd3799ca6a5d28fc742/files on the shell server? Remember, grep is your friend.

1. login online shell.

2. move the folder.
```
8ma10@pico-2018-shell:~$ cd /problems/grep-2_0_783d3e2c8ea2ebd3799ca6a5d28fc742/files
```

3. cat and grep 'picoCTF' to each file.
```
8ma10@pico-2018-shell:/problems/grep-2_0_783d3e2c8ea2ebd3799ca6a5d28fc742/files$ cat ./file*/file* | grep picoCTF
picoCTF{grep_r_and_you_will_find_24c911ab}
```

FLAG - `picoCTF{grep_r_and_you_will_find_24c911ab}`
