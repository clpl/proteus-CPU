**term.txt存放端口名称**

**input.txt存放微指令**，格式：

* XXXXXX（微指令地址）
* A:XXXXXX（ALU控制信号，S3, S2, S1, S0, M, CN）
* N:XXXXXX（下一条微指令地址）
* P:XX（P字段P1，P2）
* 使能信号
* end表示一条微指令结束

例：

000001
​	PC_OUT_EN
​	AR_EN
​	P:00
​	N:000010
end

**output.txt为输出** 