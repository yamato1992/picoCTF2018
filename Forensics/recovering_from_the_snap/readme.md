## Recovering from the Snap

Problem

>There used to be a bunch of animals here, what did Dr. Xernon do to them?

1. recover animal.dd file with foremost command.
```
8ma10$ foremost animals.dd 
foremost: /usr/local/etc/foremost.conf: No such file or directory
Processing: animals.dd
|*|

8ma10$ cd output/
8ma10$ ls
audit.txt   jpg

8ma10$ cat audit.txt
Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus
Audit File

Foremost started at Tue Dec 31 09:11:51 2019
Invocation: foremost animals.dd 
Output directory: /Users/yamato/Downloads/picoCTF2018/recovering_from_the_snap/output
Configuration file: /usr/local/etc/foremost.conf
------------------------------------------------------------------
File: animals.dd
Start: Tue Dec 31 09:11:51 2019
Length: Unknown
 
Num	 Name (bs=512)	       Size	 File Offset	 Comment 

0:	00000077.jpg 	     617 KB 	      39424 	 
1:	00001313.jpg 	     481 KB 	     672256 	 
2:	00002277.jpg 	     380 KB 	    1165824 	 
3:	00003041.jpg 	     248 KB 	    1556992 	 
4:	00003541.jpg 	     314 KB 	    1812992 	 
5:	00004173.jpg 	     458 KB 	    2136576 	 
6:	00005093.jpg 	     383 KB 	    2607616 	 
7:	00005861.jpg 	      39 KB 	    3000832 	 
Finish: Tue Dec 31 09:11:52 2019

8 FILES EXTRACTED
	
jpg:= 8
------------------------------------------------------------------

Foremost finished at Tue Dec 31 09:11:52 2019
```

2. open 00005861.jpg and see the flag.

FLAG - `picoCTF{th3_5n4p_happ3n3d}`