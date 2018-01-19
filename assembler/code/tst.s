; testing program ^_^
	lad ax, (1000)
	lad bx, (2000)
	irmov cx, -3
	sub ax, bx
	jc .L3
	add ax cx
	sto ax, (3000)
	stp
.L3:
	add bx cx
	sto bx, (3000)
	stp
