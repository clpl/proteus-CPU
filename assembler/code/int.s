	push ax
	push bx
	push cx
	push dx
	add ax, bx
	xor cx, dx
	pop dx
	pop cx
	pop bx
	pop ax
	iret
