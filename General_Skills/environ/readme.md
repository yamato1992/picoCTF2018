## environ

Problem

>Sometimes you have to configure environment variables before executing a program. Can you find the flag we've hidden in an environment variable on the shell server?

1. login online shell.

2. print environment variables and grep 'picoCTF'.
```
8ma10@pico-2018-shell:~$ printenv | grep picoCTF
SECRET_FLAG=picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}
```

FLAG - `picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}`