## Inspect Me

1. visit a [website](http://2018shell.picoctf.com:56252/).

2. inspect html, css, javascript files with inspect function of Google Chrome.

```index.html
8ma10$ cat index.html | grep flag
<!-- I learned HTML! Here's part 1/3 of the flag: picoCTF{ur_4_real_1nspe -->
```

```mycss.css
8ma10$ cat mycss.css | grep flag
/* I learned CSS! Here's part 2/3 of the flag: ct0r_g4dget_9dd3b33c} */
```

```myjs.js
8ma10$ cat myjs.js | grep flag
/* I learned JavaScript! Here's part 3/3 of the flag:  */
```

3. So the answer is concated above words.
```
picoCTF{ur_4_real_1nspect0r_g4dget_9dd3b33c}
```