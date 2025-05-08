.data
	array: .word 12, 54, 76, 8
	
	msgMedia: .asciiz "A média é: "
	msgAcima: .asciiz " - Estão acima da média: "
	msgAbaixo: .asciiz " - Estão abaixo da média: "



.text
	li $t0, 0 # cont
	li $t1, 16 # tamanho do vetor (4x4)
	li $t2, 4 # qntd de elementos no vetor
	
	la $t3, array # i
	
	for: # somando todos os valores do vetor
		beq $t0, $t1, saidaFor # ENQUANTO T0 NAO FOR IGUAL T1
		
		lw $t4, ($t3) # PEGANDO VALOR DENTRO DO INDICE DO VETOR
		add $t5, $t5, $t4 # SOMANDO CADA VALOR EM T5
	
		addi $t3, $t3, 4 # cont++
		addi $t0, $t0, 4 # i++
		
		j for # JUMP FOR
	
	saidaFor: # calculando a média
		la $t3, array # i
		
		div $t5, $t2 # FAZENDO A DIVISÃO
		mflo $s0 # MOVENDO DE LOWER PRA S0
		
		li $v0, 4 # imprime mensagem
		la $a0, msgMedia
		syscall
		
		li $v0, 1
		move $a0, $s0 # IMPRIMINDO A MÉDIA
		syscall
		# --------------------
		la $t3, array # i
		li $t0, 0 # cont
		li $t6, 0 # armazena o valor
		
		whileIf:
			beq $t0, $t1, saidaWhileIf # enqt nao for igual
			
			lw $t4, ($t3) # pega valor em t3
		
			bgt $s0, $t4, contaAcima # ENQUANTO S0 FOR MAIOR QUE T4
			j continuaAcima
			
			contaAcima: # METODO
				addi $t6, $t6, 1 # cada incremento contará quantos elementos estão abaixo da média
				
			continuaAcima: # METODO
				addi $t3, $t3, 4
				addi $t0, $t0, 4
				j whileIf
			
		saidaWhileIf:
			la $t3, array # i
			
			li $t0, 0 # cont
			li $t7, 0 # armazena o valor
			
			whileIf2:
				beq $t0, $t1, saidaTotal
				
				lw $t4, ($t3)
		
				blt $s0, $t4, contaAbaixo # ENQUANTO S0 FOR MENOR QUE T4
				j continuaAbaixo
				
				contaAbaixo:
					addi $t7, $t7, 1 # cada incremento contará quantos elementos estão acima da média
				
				continuaAbaixo:
					addi $t3, $t3, 4
					addi $t0, $t0, 4
					j whileIf2
				
			saidaTotal:
				li $v0, 4
				la $a0, msgAcima
				syscall
				
				li $v0, 1
				move $a0, $t6
				syscall
				
				li $v0, 4
				la $a0, msgAbaixo
				syscall
				
				li $v0, 1
				move $a0, $t7
				syscall
				
				li $v0, 10
				syscall
		
