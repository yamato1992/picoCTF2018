## hertz

Problem

>Here's another simple cipher for you where we made a bunch of substitutions. Can you decrypt it? Connect with nc 2018shell.picoctf.com 48186.

1. access the server and get a cipher text.
```
8ma10$ nc 2018shell.picoctf.com 48186 > cipher_txt.txt
```

2. count and clac rate each character with count_character.py.
```
8ma10$ python count_character.py 
t: count:43, rate:2.5473933649289098
j: count:123, rate:7.286729857819905
x: count:148, rate:8.76777251184834
r: count:30, rate:1.7772511848341233
b: count:113, rate:6.694312796208531
z: count:143, rate:8.471563981042655
c: count:141, rate:8.35308056872038
p: count:98, rate:5.805687203791469
q: count:93, rate:5.509478672985782
u: count:206, rate:12.203791469194313
s: count:121, rate:7.168246445497631
l: count:34, rate:2.014218009478673
m: count:42, rate:2.4881516587677726
n: count:46, rate:2.7251184834123223
k: count:67, rate:3.9691943127962084
f: count:23, rate:1.3625592417061612
a: count:37, rate:2.191943127962085
h: count:26, rate:1.5402843601895735
e: count:75, rate:4.443127962085308
g: count:36, rate:2.132701421800948
w: count:28, rate:1.6587677725118484
y: count:3, rate:0.17772511848341233
i: count:9, rate:0.533175355450237
d: count:2, rate:0.11848341232227488
o: count:1, rate:0.05924170616113744
```

3. substitute each character with substitute.py.
```
8ma10$ python substitute.py 
-------------------------------------------------------------------------------
congrats here is your flag - substitution_ciphers_are_solvable_vdascrwiam
-------------------------------------------------------------------------------
"well, prince, so genoa and lucca are now just family estates of the
buonapartes. but i warn you, if you dont tell me that this means war,
if you still try to defend the infamies and horrors perpetrated by that
antichrist-i really believe he is antichrist-i will have nothing
more to do with you and you are no longer my friend, no longer my
'faithful slave,' as you call yourself! but how do you do? i see i
have frightened you-sit down and tell me all the news."

it was in july, 1805, and the speaker was the well-known anna pavlovna
scherer, maid of honor and favorite of the empress marya fedorovna.
with these words she greeted prince vasili kuragin, a man of high
rank and importance, who was the first to arrive at her reception. anna
pvlovna had had a cough for some days. she was, as she said, suffering
from la grippe; grippe being then a new word in st. petersburg, used
only by the elite.

all her invitations without exception, written in french, and delivered
by a scarlet-liveried footman that morning, ran as follows:

"if you have nothing better to do, count (or prince), and if the
prospect of spending an evening with a poor invalid is not too terrible,
i shall be very charmed to see you tonight between 7 and 10 annette
scherer."

"heavens! what a virulent attack!" replied the prince, not in the
least disconcerted by this reception. he had just entered, wearing an
embroidered court uniform, knee breeches, and shoes, and had stars on
his breast and a serene expression on his flat face. he spoke in that
refined french in which our grandfathers not only spoke but thought, and
with the gentle, patronizing intonation natural to a man of importance
who had grown old in society and at court. he went up to anna pvlovna,
kissed her hand, presenting to her his bald, scented, and shining head,
and complacently seated himself on the sofa.

"first of all, dear friend, tell me how you are. set your friend's
mind at rest," said he without altering his tone, beneath the
politeness and affected sympathy of which indifference and even irony
could be discerned.
```

FLAG - `picoCTF{substitution_ciphers_are_solvable_vdascrwiam}`