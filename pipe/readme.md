## pipe

Problem
>During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. Can you find a way to save the output from this program and search for the flag? Connect with 2018shell.picoctf.com 2015.

```
8ma10$ nc 2018shell.picoctf.com 2015 > output.txt

8ma10$ cat output.txt | grep picoCTF
picoCTF{almost_like_mario_8861411c}
```

FLAG - `picoCTF{almost_like_mario_8861411c}`