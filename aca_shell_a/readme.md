## Aca Sheel A

Problem

>It's never a bad idea to brush up on those linux skills or even learn some new ones before you set off on this adventure! Connect with nc 2018shell.picoctf.com 58422.

1. access 2018shell.picoctf.com 58422.
```
8ma10$ nc 2018shell.picoctf.com 58422
Sweet! We have gotten access into the system but we aren't root.
It's some sort of restricted shell! I can't see what you are typing
but I can see your output. I'll be here to help you along.
If you need help, type "echo 'Help Me!'" and I'll see what I can do
There is not much time left!
```

Question 1.
> If you need help, type "echo 'Help Me!'" and I'll see what I can do
There is not much time left!

2. echo 'Help Me!' and look some direcotories.
```
~/$ echo 'Help Me!'
Help Me!

You got this! Have you looked for any  directories?
~/$ ls
blackmail
executables
passwords
photos
secret

~/$ cd secret
Now we are cookin'! Take a look around there and tell me what you find!

~/secret$ ls      
intel_1
intel_2
intel_3
intel_4
intel_5
profile_ahqueith5aekongieP4ahzugi
profile_ahShaighaxahMooshuP1johgo
profile_aik4hah9ilie9foru0Phoaph0
profile_AipieG5Ua9aewei5ieSoh7aph
profile_bah9Ech9oa4xaicohphahfaiG
profile_ie7sheiP7su2At2ahw6iRikoe
profile_of0Nee4laith8odaeLachoonu
profile_poh9eij4Choophaweiwev6eev
profile_poo3ipohGohThi9Cohverai7e
profile_Xei2uu5suwangohceedaifohs
Sabatoge them! Get rid of all their intel files!
```

Question 2.
>Sabatoge them! Get rid of all their intel files!

3. remove some intel files.
```
~/secret$ rm intel_*
Nice! Once they are all gone, I think I can drop you a file of an exploit!
```

4. echo 'Drop it in!' and execute a file.

```
Just type "echo 'Drop it in!' " and we can give it a whirl!

~/secret$ echo 'Drop it in!'
Drop it in!
I placed a file in the executables folder as it looks like the only place we can execute from!
Run the script I wrote to have a little more impact on the system!

~/secret$ cd ..
~/$ cd executables
~/executables$ ls
dontLookHere

~/executables$ ./dontLookHere
 ecfd a9a8 6b91 9d7a 27bc 4c2e a0c4 27e9 bc50 c325 6f51 5e57 6f04 6ad9 71dd 668f 80bb df4d 38a1 1ba3 029b 9674 c05c 18ac 3952
 a075 a4fd ccad 29c9 4f5a 5651 9039 2fe6 f3a4 a9bc 0767 91ee 10db a597 6cbe e03d bea3 95b7 72a4 05d7 e465 e474 772b cfe0 ecb0
 a7d9 c71d a60e 8463 f425 0dc0 a256 795e 8dc2 12c3 5a7f 5013 70ef 7167 979b 74a0 e5f6 5a3f 3600 034c 08cb f08a 4538 5fd6 2538
 53f8 69c4 1788 fa84 f337 6cf7 1a76 2972 1b33 74dd dbe5 963c e33d 20e8 17e1 a278 9435 c482 803b 7062 d7f2 6792 7b3b 4943 2408
 8d46 41e3 7619 9d59 fdd8 6efa fe2b 84e6 0330 690d 7290 f19c 04cd 11ed fa85 b60e 816c 4760 b0b6 5d11 6ce3 d474 0999 82aa d4d1
 f169 b50e 6630 a2f5 c773 f818 eeff 0ad7 772f 9fbc abf4 d607 6e2f bc7e 52e3 3e74 1902 d511 f3ec f728 e89f e28f d78f 5f66 9dde
 9140 0d4d 918e 88bc a3b6 72ce fce7 e0e6 f707 0c46 bf17 89db a303 1afb 4601 69c8 9f63 37b6 60f7 dcc9 5a42 a9d6 c21e 49b2 7b4c
 7203 07a1 d8f6 8dd0 6604 a942 df9c 0281 b812 b85f f061 e117 7cc8 8a8a 1342 87b0 8a9c 314d c082 3e8f f3d1 3aab 5db4 a48b f7d3
 e27e e041 4ec7 2aa7 7943 97ac d6b1 e85d 1d82 5cca cbaa 6c53 b772 0f3d 93a0 144a 331b 375d b6c5 e600 f597 20e7 8cd8 cca4 dbab
 fa1e 4cf0 f2a9 c7f5 fb66 198d dc87 9579 62b5 0f64 36a8 9558 6edb 881b 37e6 e45f 8b18 b158 3f50 1119 2a2f 197e 6446 09fe 6f2c
 a601 ccc7 e2e5 d2c0 610a fda5 bd53 91e4 3444 3b35 58cc 0835 3c85 3c20 e7df e324 b524 b24c 5108 dfbf 9c79 974d f3c7 8592 899c
 93d8 bc88 d766 2d29 6382 5712 9c70 808e 4bd7 d808 7cb3 6f38 b4ca e829 d916 fe77 aa25 a2a7 4499 8873 4ce1 f42f 874e 75df 7cef
 e26a 894a 9732 ad01 5a4b 9b83 6255 5be8 8f89 680c 68c1 a37f 9e4f 667e a6b2 7bcc 6103 3f42 33ee 65b7 7d78 c058 a9d3 7658 abda
 cfca 6c68 5e7e 290d 0a50 a044 6f00 ff00 ac86 8dcf d2cf 9623 703a 412a 1b93 3a06 ffc7 ad55 3264 602f 127b b7c3 c533 79a4 5e31
 5689 5cf8 a4ca 1458 b936 8a2f c16f 740c 09b7 4b0f 9b9f 92aa 8366 e25f e43b fbcb ce82 6a5e cca7 824b c31b 5eb6 937f c3d8 a82e
 c55d 75bf f7df c1c0 b722 111c f77a e088 09f8 396a 662e 5a34 b6a9 f9c8 304d 258b 7770 689a 49a3 a4d1 dfa2 117d 15c2 16fa 6cfa
 2b35 13d0 ec17 dec0 8f5a 5d0e c016 754e f333 c2d3 cdcd 2ba9 a97b d375 0942 935a cebd 43e4 03a9 4dfa 0260 6781 a250 9e0f 166d
 97b1 b754 b3a1 9e74 7a63 120f f939 216f 3d2f 3a49 f738 14d8 e818 0636 de40 536e dc43 464c 941d 4def e3cb 61f5 ee94 7ad7 4112
 e815 063a 45bf 4168 2df4 87af 6a9c 9049 ab07 f4db 7a37 8305 a7fb dfcf 83b7 0c7d e5c8 8f98 eb13 e7f0 4417 a003 3271 aa00 3517
 043f 57fb 98ae 2fed f310 e0f2 e7b0 ab09 7c56 264a 4a3a 6a9f 6869 d069 68b3 2b55 125b 1718 c2d6 fa1e 066b 1d05 b408 4ec6 fd71
 3f2d 63a5 3409 926a 75c5 6f85 a4ef 5696 099d 42f6 d53b bca9 9cb5 0b57 e8ec 0e4e a2b3 de89 4267 b1af 0ae2 5efa 4664 0d43 0b84
 51c2 e7d9 b292 390e b549 ef6d d1cd 14fb e3ed 8554 4246 48a7 5a25 5370 22e5 995d 40c9 dd89 0cc6 fbb0 8a7c c877 8e25 78b3 e294
 aabf 0408 6283 4b87 b504 9862 162e 0c37 5139 c9f0 b3b5 c4b8 e831 21bd ab02 f679 f799 c814 43c9 d819 7256 dcaf 9ba9 6f15 7993
 d77f a215 5816 ea21 667b 19e0 caa6 d6f8 dac3 639f f8de 146b 50c4 ba9e c844 cfde 1859 cbfa 1c38 f847 3e84 53a5 df42 a5ca dab1
 31a3 acbc 83dc e905 d4d9 f598 8457 03ec 8976 6f72 95ab d2e6 14fe daf1 293a f5bf 6376 adf0 c97e ee2d 7fc4 f66a d458 c3cc 14e9
 1bb1 1715 5f1e 7339 0f59 dae9 9808 1e9e a691 e673 4508 e57b 347e acfb e5c2 97e4 41f8 1aa5 ec31 5a77 7d9d 0887 3f52 b5df f1ba
 2274 3b79 4880 d8f1 8f7c 36f1 a3d8 d141 a67d b808 ca4d b9ed 6cb4 9379 d5c2 c5b2 b8cb ce7a 5a41 fbc6 85d0 af5e a75f bed5 ab60
 69c7 5feb d5e7 c084 884a 84ef 9bb2 2d02 663d cc27 b1b5 744d 1865 a071 6ef0 4f81 d5a3 9e33 44d4 5af2 0171 00cd 2345 2c62 2e14
 662e c718 ca44 3776 2132 b5ee 265f bcdb d110 9f26 277a 132f a702 56af fd2c 1810 a1a5 b01c 1812 fc6d 9ce0 bd26 2d73 f727 c90a
 7682 289c a059 f9f9 3d21 2ab3 bd79 e2ab c31c f2da a8b4 e59d 3048 e70e 125e a4d6 4a61 d267 5d99 fb99 b0ab f202 f78a 19f0 8021
 4495 d790 f425 90ee da29 b8e1 2b59 ab31 58dd ff43 1161 08ec 5645 555b 2d9e ceab 19d0 fda2 49ba f9f3 4167 a8dc c4e7 b49a 63f3
Looking through the text above, I think I have found the password. I am just having trouble with a username.
Oh drats! They are onto us! We could get kicked out soon!
Quick! Print the username to the screen so we can close are backdoor and log into the account directly!
You have to find another way other than echo!
```


5. show username with whoami command.
```
~/executables$ whoami
l33th4x0r
Perfect! One second!
Okay, I think I have got what we are looking for. I just need to to copy the file to a place we can read.
```

6. copy the file TopSecret in tmp direcotory into the passwords folder.
```
Try copying the file called TopSecret in tmp directory into the passwords folder.

~/executables$ cp /tmp/TopSecret ../passwords/
Server shutdown in 10 seconds...
Quick! go read the file before we lose our connection!
```

6. show TopSecret file.
```
~/executables$ cd ..
~/$ cd passwords
~/passwords$ cat TopSecret
Major General John M. Schofield's graduation address to the graduating class of 1879 at West Point is as follows: The discipline which makes the soldiers of a free country reliable in battle is not to be gained by harsh or tyrannical treatment.On the contrary, such treatment is far more likely to destroy than to make an army.It is possible to impart instruction and give commands in such a manner and such a tone of voice as to inspire in the soldier no feeling butan intense desire to obey, while the opposite manner and tone of voice cannot fail to excite strong resentment and a desire to disobey.The one mode or other of dealing with subordinates springs from a corresponding spirit in the breast of the commander.He who feels the respect which is due to others, cannot fail to inspire in them respect for himself, while he who feels,and hence manifests disrespect towards others, especially his subordinates, cannot fail to inspire hatred against himself.
picoCTF{CrUsHeD_It_4e355279}
```

FALG - `picoCTF{CrUsHeD_It_4e355279}`