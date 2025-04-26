.data
	array:
		.word 15, 43, 65, 12
	msgSaida: .asciiz "A soma total do vetor é: "
	
.text
	move $t0, $zero # indice
	li $t1, 16 # tamanho do vetor
	la $t2, array
	move $t3, $zero # registrador da soma
	
	
	for: 
		beq $t0, $t1, saidaDoLoop
		
		lw $t4, 0($t2)
		
		add $t3, $t3, $t4
		
		addi $t2, $t2, 4
		
		addi $t0, $t0, 4
		
		j for
	
	saidaDoLoop:
		li $v0, 4 # imprime mensagem
		la $a0, msgSaida
		syscall
	
		li $v0, 1
		move $a0, $t3
		syscall
		
		li $v0, 10
		syscall

	