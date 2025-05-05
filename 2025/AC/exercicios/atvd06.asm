.data
	array: .word 13, 65, 34, 98
	msgMaior: .asciiz "O maior número: "

.text
	.main:
		li $t0, 0 # cont
		la $t1, array # i
		li $t2, 16 # tamanho do vetor
		lw $t3, ($t1) # maior número	
	
	
	for:
		beq $t0, $t2, fimFor # se t0 == t2
		
		lw $t4, ($t1) # numero atual
		
		bgt $t3, $t4, else # se t3 > t4
		move $t3, $t4	# t3 = t4
			
		else: 
			addi $t1, $t1, 4 # i++
			addi $t0, $t0, 4 # cont++
			j for 
	fimFor:
		# imprime mensagem
		li $v0, 4 
		la $a0, msgMaior
		syscall
		
		# imprime maior número
		li $v0, 1
		move $a0, $t3
		syscall
		
		li $v0, 10
		syscall
		
	