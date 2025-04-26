.data
	espaco: .byte ' '

.text
	
	li $v0, 5
	syscall
	
	move $t0, $v0 # valor lido
	
	move $t1, $zero
	
	
	while:
		bgt $t1, $t0, saida # while t1 <= t0
		
		li $v0, 1 # imprime t1
		move $a0, $t1
		syscall
		
		li $v0, 4 # imprime espaço em branco
		la $a0, espaco
		syscall
		
		addi $t1, $t1, 1
		j while # jump while, ou seja, volta pro while
	
	saida: 
		li $v0, 10
		syscall
		
		
	
		
	