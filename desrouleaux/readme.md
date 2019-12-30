## Desrouleaux

Problem
>Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with nc 2018shell.picoctf.com 54782. incidents.json

1. access remote server.
```
8ma10$ nc 2018shell.picoctf.com 54782
You'll need to consult the file `incidents.json` to answer the following questions.
```

Question 1.
>What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.

2. find most common source IP address in 'incident.json'.
```
8ma10$ cat incidents.json | grep src_ip | cut -d '"' -f 4 | sort | uniq -c | sort -r | head -1
   4 251.165.34.242
```

Answer Question 1.

```
251.165.34.242
Correct!
```

Question 2.
>How many unique destination IP addresses were targeted by the source IP address 246.69.53.233?


3. execute below python file, return 3 as the answer.
```count_dst_ip.py
8ma10$ python count_dst_ip.py 
src ip address:246.69.53.233
3 ip addresses were targeted by src_ip.
```

Answer Question 2.
```
3
Correct!
```

Question 3.
>What is the number of unique destination ips a file is sent, on average? Needs to be correct to 2 decimal places.

execute below python file, return 1.40 as the answer.
```
8ma10$ python cnt_ave_dst_ip.py 
the number of unique ips a file is sent, on average is 1.40
```

```
1.40
Correct!


Great job. You've earned the flag: picoCTF{J4y_s0n_d3rUUUULo_c74e3495}
```

FLAG - `picoCTF{J4y_s0n_d3rUUUULo_c74e3495}`