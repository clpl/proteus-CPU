; testing program ^_^
	irmov ax, 123
	irmov bx, 456
	add ax, bx
	jl .L1
	sto ax, (1000)
	xor ax, ax
	lad cx, (1000)
	sub cx, bx
	lad cx, (1001)
	sub cx, bx
	jl .L2
	stp
.L1:
	sub bx, ax
	sto ax, (1000)
	stp
.L2:
	lad cx, (1002)
	add cx, bx
	lad cx, (1003)
	stp
