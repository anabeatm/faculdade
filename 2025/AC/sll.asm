.text
	li $t0, 12
	sll $t1, $t0, 2 # t1 = t0 * (2^2) -> 48 = 12 * (2^2)
	
	li $v0, 10
	syscall