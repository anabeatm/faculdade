.data
	caractere: .byte 'a' # caractere para ser impresso
.text

	li $v0, 4 # imprimir char ou String
	la $a0, caractere
	syscall
	
	li $v0, 10 # encerrar o programa
	syscall