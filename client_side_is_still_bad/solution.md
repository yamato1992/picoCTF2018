## Client side is still bad

1. show index.html
```
function verify() {
checkpass = document.getElementById("pass").value;
split = 4;
if (checkpass.substring(split*7, split*8) == '}') {
    if (checkpass.substring(split*6, split*7) == '06ac') {
    if (checkpass.substring(split*5, split*6) == 'd_5e') {
        if (checkpass.substring(split*4, split*5) == 's_ba') {
        if (checkpass.substring(split*3, split*4) == 'nt_i') {
        if (checkpass.substring(split*2, split*3) == 'clie') {
            if (checkpass.substring(split, split*2) == 'CTF{') {
            if (checkpass.substring(0,split) == 'pico') {
                alert("You got the flag!")
                }
            }
            }
    
        }
        }
    }
    }
}
else {
    alert("Incorrect password");
}
}
```

2. concat each words.
```
picoCTF{client_is_bad_5e06ac}
```