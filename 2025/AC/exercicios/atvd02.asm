.data
	array:
		.word 15, 43, 65, 12
	msgSaida: .asciiz "A soma total do vetor é: "
	
.text
	li $t0, 0 # cont
	li $t1, 16 # tamanho do vetor
	la $t2, array # i
	li $t3, 0 # registrador da soma
	
	
	for: 
		beq $t0, $t1, saidaDoLoop # enqt t0 != t1
		
		lw $t4, ($t2) # pegando o primeiro valor da array e colocando em t4
		
		add $t3, $t3, $t4 # t3 = t3 + t4
		
		addi $t2, $t2, 4 # i++
		
		addi $t0, $t0, 4 # cont++
		
		j for
	
	saidaDoLoop:
		li $v0, 4 # imprime mensagem
		la $a0, msgSaida
		syscall
	
		li $v0, 1 # imprime o número
		move $a0, $t3
		syscall
		
		li $v0, 10
		syscall

	
