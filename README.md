微程序流程图：https://www.processon.com/diagraming/5a4f89e3e4b01acda58c3d8b

微指令表：https://shimo.im/sheet/hZ38w8z0aB0NJl4N

# 任务分配

| 内容         | 状态   | 分配   |
| ---------- | ---- | ---- |
| ALU        | 已完成  | CL封装 |
| RAM/ROM    | 已完成  | CL   |
| I/O        | 已完成  | LSY  |
| REGISTER   | 已完成  | LSY  |
| PC         | 已完成  | DY   |
| PSW        | 已完成  | DY   |
| CLOCK      | 忽略   | CL    |
| CONTROLLER | 困难   | ALL  |

![控制器](http://owvqyk7j0.bkt.clouddn.com/controller.PNG)

![控制台](http://owvqyk7j0.bkt.clouddn.com/console.PNG)

![数据通路](http://owvqyk7j0.bkt.clouddn.com/data_bus.PNG)


# proteus-CPU

计组大作业

__软件版本__：Proteus 8.4 SP0

__总线__：16位数据，16位地址

__结构__：待定

__寄存器__：四个通用寄存器，其中包括累加寄存器AC

__指令集__：

| 序号   | 指令               | 功能                            | 备注     | 二进制形式（16进制） | 微程序首地址 |
| ---- | ---------------- | ----------------------------- | ------ | ----------- | ------ |
| 1    | STO (XXXX), R\_i | R\_i -> 存储器                   |        | 01 0@ $$ $$ | 000001 |
| 2    | LAD R\_i, (XXXX) | 存储器 -> R\_i                   |        | 02 0@ $$ $$ | 001000 |
| 3    | RRMOV R\_i, R\_j | R\_j -> R\_i                  |        | 03 @@       | 000111 |
| 4    | IRMOV R\_i, XXXX | XXXX -> R\_i                  |        | 04 0@ $$ $$ | 001000 |
| 5    | ADD R\_i, R\_j   | R\_i + R\_j -> R\_i           |        | 05 @@       | 110000 |
| 6    | SUB R\_i, R\_j   | R\_i - R\_i -> R\_i           |        | 06 @@       | 110100 |
| 7    | AND R\_i, R\_j   | R\_i & R\_j -> R\_i           |        | 07 @@       | 111000 |
| 8    | XOR R\_i, R\_j   | R\_i ^ R\_j -> R\_i           |        | 08 @@       | 111100 |
| 9    | CLA              | AC <- 0000H                   |        | 09 00       | 001111 |
| 10   | JMP FLAG         | PC <- PC+offset               | 64KB   | 0A 00 $$ $$ | 001010 |
| 11   | JL FLAG          | if R_i < R_j, PC <- PC+offset | 64KB   | 0B 00 $$ $$ | 100010 |
| 12   | IRET             | 中断返回                          | 恢复现场   | 0C 00       | 011001 |
| 13   | PUSH R\_i        | SP <- SP-1, (SP) <- R\_i      | 写一个机器字 | 0D 0@       | 010000 |
| 14   | POP R\_i         | R\_i <- (SP), SP <- SP+1      |        | 0E 0@       | 010101 |

@:寄存器指示符（0<=@<=3)

$:立即数


# 工作流

先一起设计好每个元件的接口，

分开做每个元件，放在单独的文件夹里并测试，总目录/component

测试无误后编译并生成元件，放在/build下

最后一起合并


# 元件

## ALU

### 输入

ALU_BUS 低有效，ALU运算结果到BUS的出口开关

ALU_M, ALU_CN, ALU_S0, ALU_S1... 运算控制

ZREG1_EN,ZREG2_EN 高有效，暂存器1，2的使能端 

16位数据到ZREG1,ZREG2

### 输出

16位运算结果到BUS

## 存储器

### 输入

MEM_CE 高有效 存储器的片选信号

MEM_WE CE有效情况下，1为写，0为读

AR_LD 同步 AR置数信号

总线输入 16位地址

CLK 全局时钟信号

### 输出

16位数据到BUS


## 寄存器组

四个16位寄存器 AC R1, R2, R3

自带四选一

### 输入：

REG\_BUS_IN[0..15] 接总线

REG_CLK 时钟信号 上升沿

IN\_SEL[0,1] 选择信号 从总线输入的使能 AC为0

OUT\_SEL[0,1] 选择信号 输出到总线的使能

REG\_AC\_CLR 累加器AC清零


### 输出：

REG\_BUS\_OUT[0..15] 输出到总线

## I/O

逻辑门输入，七段显示输出（七段显示接通用寄存器）

输入寄存器RI，长期有效

### 输入

INPUT_EN 输入寄存器到总线的使能端，高有效

### 输出

INPUT_BUS[0..15] 输入的数据，接总线


## PC

### 端口

DBUS[0..15]：数据总线，输入端

PC[0..15]：数据总线，输出端

CLR：同步清零，高有效

W/R：读/写使能，1为写有效，0为读有效

PCINC：PC值+1，高有效

LPC：同步置数，高有效

CLK：时钟信号，上升沿

### 优先级

CLK > CLR > W/R > PCINC, LPC （全部为同步操作）

PCINC与LPC不可同时为1

W/R为写有效时，DBUS做输入；读有效时，DBUS做输出

## 控制器流程

T1把当前微程序存到微程序寄存器里，T2把微程序寄存器后六位，也就是下一个微程序地址存到一排寄存器里，同时这个步骤可以用p字段进行跳转

## PSW

### 端口

CLR：同步清零，高有效

EN：使能信号，高有效

IC：溢出（进位）信号，高有效

CLK：时钟脉冲，上升沿

### 优先级

CLK > CLR > EN > IC
