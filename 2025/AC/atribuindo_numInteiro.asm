.data
	idade: .word 43 # valor inteiro na memória RAM
.text
	li $v0, 1
	lw $a0, idade
	syscall
	
	li $v0, 10
	syscall