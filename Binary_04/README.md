# Binary 04

Download the file at https://xxxxxxxxxx/bh02.zip and then find a way to get the flag.

## Solution

In this challenge, you have to manipulate `gdb` and use the `jump` method to bypass the comparison.

I set two breakpoints, one on `main` (I used Ghidra to get an overview of the binary), then another on a comparison which is supposed to move us away from the flag: `0x000055555555482f <+101>:   callq  0x5555555546a0 <strcmp@plt>`.

Finally, I made a little jump to the following address `0x000055555555483c`, after the `jne`.

```
# Dry run
$ ./program 
密码是什么？
> What?!
不正确的.

$ gdb program 
(gdb) b main
Breakpoint 1 at 0x7ce
(gdb) r
Starting program: /[REDACTED]/Binary_04/program 

Breakpoint 1, 0x00005555555547ce in main ()
(gdb) disas
Dump of assembler code for function main:
   0x00005555555547ca <+0>: push   %rbp
   0x00005555555547cb <+1>: mov    %rsp,%rbp
=> 0x00005555555547ce <+4>: add    $0xffffffffffffff80,%rsp
   0x00005555555547d2 <+8>: mov    %fs:0x28,%rax
   0x00005555555547db <+17>:    mov    %rax,-0x8(%rbp)
   0x00005555555547df <+21>:    xor    %eax,%eax
   0x00005555555547e1 <+23>:    lea    0x1f0(%rip),%rax        # 0x5555555549d8
   0x00005555555547e8 <+30>:    mov    %rax,-0x78(%rbp)
   0x00005555555547ec <+34>:    lea    0x1ed(%rip),%rdi        # 0x5555555549e0
   0x00005555555547f3 <+41>:    callq  0x555555554660 <puts@plt>
   0x00005555555547f8 <+46>:    lea    0x1fd(%rip),%rdi        # 0x5555555549fc
   0x00005555555547ff <+53>:    mov    $0x0,%eax
   0x0000555555554804 <+58>:    callq  0x555555554680 <printf@plt>
   0x0000555555554809 <+63>:    mov    0x200800(%rip),%rdx        # 0x555555755010 <stdin@@GLIBC_2.2.5>
   0x0000555555554810 <+70>:    lea    -0x50(%rbp),%rax
   0x0000555555554814 <+74>:    mov    $0x3c,%esi
   0x0000555555554819 <+79>:    mov    %rax,%rdi
   0x000055555555481c <+82>:    callq  0x555555554690 <fgets@plt>
   0x0000555555554821 <+87>:    lea    -0x50(%rbp),%rdx
   0x0000555555554825 <+91>:    mov    -0x78(%rbp),%rax
   0x0000555555554829 <+95>:    mov    %rdx,%rsi
   0x000055555555482c <+98>:    mov    %rax,%rdi
   0x000055555555482f <+101>:   callq  0x5555555546a0 <strcmp@plt>
   0x0000555555554834 <+106>:   test   %eax,%eax
   0x0000555555554836 <+108>:   jne    0x555555554921 <main+343>
   0x000055555555483c <+114>:   movb   $0xd1,-0x70(%rbp)
   0x0000555555554840 <+118>:   movb   $0xc0,-0x6f(%rbp)
   0x0000555555554844 <+122>:   movb   $0x57,-0x6e(%rbp)
   0x0000555555554848 <+126>:   movb   $0x75,-0x6d(%rbp)
   0x000055555555484c <+130>:   movb   $0x72,-0x6c(%rbp)
   0x0000555555554850 <+134>:   movb   $0xa9,-0x6b(%rbp)
--Type <RET> for more, q to quit, c to continue without paging--
End of assembler dump.
(gdb) b *0x000055555555482f
Breakpoint 2 at 0x55555555482f
(gdb) c
Continuing.
密码是什么？
> 123

Breakpoint 2, 0x000055555555482f in main ()
(gdb) disas
Dump of assembler code for function main:
   0x00005555555547ca <+0>: push   %rbp
   0x00005555555547cb <+1>: mov    %rsp,%rbp
   0x00005555555547ce <+4>: add    $0xffffffffffffff80,%rsp
   0x00005555555547d2 <+8>: mov    %fs:0x28,%rax
   0x00005555555547db <+17>:    mov    %rax,-0x8(%rbp)
   0x00005555555547df <+21>:    xor    %eax,%eax
   0x00005555555547e1 <+23>:    lea    0x1f0(%rip),%rax        # 0x5555555549d8
   0x00005555555547e8 <+30>:    mov    %rax,-0x78(%rbp)
   0x00005555555547ec <+34>:    lea    0x1ed(%rip),%rdi        # 0x5555555549e0
   0x00005555555547f3 <+41>:    callq  0x555555554660 <puts@plt>
   0x00005555555547f8 <+46>:    lea    0x1fd(%rip),%rdi        # 0x5555555549fc
   0x00005555555547ff <+53>:    mov    $0x0,%eax
   0x0000555555554804 <+58>:    callq  0x555555554680 <printf@plt>
   0x0000555555554809 <+63>:    mov    0x200800(%rip),%rdx        # 0x555555755010 <stdin@@GLIBC_2.2.5>
   0x0000555555554810 <+70>:    lea    -0x50(%rbp),%rax
   0x0000555555554814 <+74>:    mov    $0x3c,%esi
   0x0000555555554819 <+79>:    mov    %rax,%rdi
   0x000055555555481c <+82>:    callq  0x555555554690 <fgets@plt>
   0x0000555555554821 <+87>:    lea    -0x50(%rbp),%rdx
   0x0000555555554825 <+91>:    mov    -0x78(%rbp),%rax
   0x0000555555554829 <+95>:    mov    %rdx,%rsi
   0x000055555555482c <+98>:    mov    %rax,%rdi
=> 0x000055555555482f <+101>:   callq  0x5555555546a0 <strcmp@plt>
   0x0000555555554834 <+106>:   test   %eax,%eax
   0x0000555555554836 <+108>:   jne    0x555555554921 <main+343>
   0x000055555555483c <+114>:   movb   $0xd1,-0x70(%rbp)
   0x0000555555554840 <+118>:   movb   $0xc0,-0x6f(%rbp)
   0x0000555555554844 <+122>:   movb   $0x57,-0x6e(%rbp)
   0x0000555555554848 <+126>:   movb   $0x75,-0x6d(%rbp)
--Type <RET> for more, q to quit, c to continue without paging--q
Quit

(gdb) j *0x000055555555483c
Continuing at 0x55555555483c.
正确!

旗: gHn3*jXvs&H!@jGs
[Inferior 1 (process 16233) exited normally]
(gdb) 
```

Flag is `gHn3*jXvs&H!@jGs`
