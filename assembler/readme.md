#汇编器

​	命令格式：`assembler <input file name> [starting address]`，起始地址可以不写，默认为0.

​	输出文件是 ins.txt 和 ins_bin.txt，ins_bin.txt 用来编译asm，ins.txt 有助于调试。

**指令格式**：

​	assembler.c文件里65~79也有指令格式的说明。写不写 `(` `)` `,` 不影响汇编结果。

```asm
stp
sto rA XXXX
lad rA XXXX
;rrmov rA rB
irmov rA XXXX
add rA rB
sub rA rB
and rA rB
xor rA rB
cla
jmp .flag
jc .flag
iret
push rA
pop rA
```

