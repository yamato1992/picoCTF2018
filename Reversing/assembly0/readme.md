## assembly 0

Problem

>What does asm0(0xd8,0x7a) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/assembly-0_1_fc43dbf0079fd5aab87236bf3bf4ac63.

1. login online shell and move the folder.

2. see the assembly file 'intro_asm_rev.S', so return eax value after copy ebx to eax.
```
8ma10@pico-2018-shell:/problems/assembly-0_1_fc43dbf0079fd5aab87236bf3bf4ac63$ cat intro_asm_rev.S
.intel_syntax noprefix                       
.bits 32

.global asm0

asm0:
    push    ebp                                 
    mov     ebp,esp                             
    mov     eax,DWORD PTR [ebp+0x8]             
    mov     ebx,DWORD PTR [ebp+0xc]             
    mov     eax,ebx                             
    mov     esp,ebp                             
    pop     ebp                                 
    ret             
```

3. this question gives arguments(0xd8, 0x7a), so it returns 0x7a.

FLAG - `0x7a`