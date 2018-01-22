; testing program ^_^
	irmov ax, 123			;ax = 0x7b
	irmov bx, 456			;bx = 0x1c8
	add ax, bx				;ax = 0x243
	jl .L1
	sto ax, (0xff00)	;(0xff00) = 0x243
	xor ax, ax				;ax = 0x0
	lad cx, (0xff00)	;cx = 0x243
	sub cx, bx				;cx = 0x7b
	push cx						;sp = 0xefff
	pop dx						;dx = 0x7b  sp = 0xf000
	sub cx, bx				;cx = 0xfeb3
	jl .L2
	stp
.L1:
	sub bx, ax
	sto ax, (0xff01)
	stp
.L2:
	sto cx, (0xff02)	;(0xff02) = 0xfeb3
	and cx, bx				;cx = 0x80
	push cx						;sp = 0xefff
	pop bx						;bx = 0x80  sp = 0xf000
	irmov cx, 3				;cx = 0x3
	irmov dx, 1				;dx = 0x1
.L3:
	add ax, bx				;ax = 0x80, 0x100, 0x180, 0x200
	sub cx, dx				;cx = 0x2, 0x1, 0x0, 0xffff
	jl .L4
	jmp .L3:
.L4:
	lad ax, (0xff02)	;ax = 0xfeb3
	add ax, bx				;ax = 0xff33
	cla								;ax = 0
	stp
