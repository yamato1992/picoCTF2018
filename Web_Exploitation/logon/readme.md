## Logon

Problem

>I made a website so now you can log on to! I don't seem to have the admin password. See if you can't get to the flag. http://2018shell.picoctf.com:62746 (link)


1. logon user except admin user.
```
Username foo
Password foo
```

2. After succeed logon, check the cookie.

Google Chrome
>Inspect -> Applications -> Cookies

3. the cookies on this site has admin attribute, so rewrite value from 'Flase' to 'True'.

4. reload this site, you can see the flag.

FLAG - `picoCTF{l0g1ns_ar3nt_r34l_92020990}`

