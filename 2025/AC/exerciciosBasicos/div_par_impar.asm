.data 
	string:
		.word "É par."


.text
	main:
		li $v0, 5
		syscall
		move $t0, $v0
		
		li $t1, 2
		div $t0, $t1
		
		mfhi $s1
		beq $s1, 0, $s2
		
		li $v0, 4
		la $a0, string
		syscall
		
		li $v0, 10
		syscall