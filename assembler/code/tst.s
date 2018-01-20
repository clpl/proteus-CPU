; testing program ^_^
	irmov ax, 123
	irmov bx, 456
	add ax, bx
	sto ax, (1000)
	xor ax, ax
	lad cx, (1000)
	sub cx, bx
	lad cx, (1001)
