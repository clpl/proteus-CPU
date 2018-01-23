#汇编器

​	命令格式：`assembler <input filename> <output filename> [starting address]`，起始地址可以不写，默认为0.

​	输出文件是 `<output filename>.txt` 和 `<output filename>_bin.txt`， `<output filename>_bin.txt` 用来编译asm，`<output filename>.txt` 用来帮助调试。

**指令格式**：

​	assembler.c文件里65~79也有指令格式的说明。写不写 `(` `)` `,` 不影响汇编结果。十六进制数要加前缀 `0x` 。

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
jl .flag
iret
push rA
pop rA
```

