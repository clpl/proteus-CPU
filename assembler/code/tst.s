; testing program ^_^
	irmov ax, 123
	irmov bx, 456
	add ax, bx
	jl .L1
	sto ax, (0xff00)
	xor ax, ax
	lad cx, (0xff00)
	sub cx, bx
	push cx
	pop dx
	sub cx, bx
	jl .L2
	stp
.L1:
	sub bx, ax
	sto ax, (0xff01)
	stp
.L2:
	sto cx, (0xff02)
	and cx, bx
	push cx
	pop bx
	irmov cx, 3
	irmov dx, 1
.L3:
	add ax, bx
	sub cx, dx
	jl .L3
	jmp .L4:
	sub ax, bx
	cla
.L4:
	lad ax, (0xff02)
	add ax, bx
	cla
	stp
