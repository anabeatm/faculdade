.data
	espaco: .byte ' '
	
	array:
		.word 1, 2, 3, 4
	array2: 
		.word 1, 2, 3, 4
	
	array3:
		.word 0:4 # vetor de 4 zeros (vazio)	


.text
	main:
		li $t0, 0 # indice
		
		li $t1, 16 # tamanho dos vetores
		
		la $t2, array # pegando o primeiro endereço do vetor e atribuindo a $t2
		
		la $t3, array2 # pegando o primeiro endereço do vetor e atribuindo a $t3
		
		la $t4, array3 # pegando o primeiro endereço do vetor e atribuindo a $t4

		for:
			beq $t0, $t1, saida # enqt não for igual
			
			lw $t7, ($t2) # colocando em t7 o valor em que está o t2
			lw $t8, ($t3)
			
			add $t9, $t7, $t8 # somando os valores de cada vetor
			
			sw $t9, ($t4) # armazenando o valor de t9 no vetor

			addi $t2, $t2, 4 # incrementando o indice do vetor
			addi $t3, $t3, 4
			addi $t4, $t4, 4

			addi $t0, $t0, 4 # i++

			j for # jump for
		
		saida:
			li $t0, 0 # indice
			
			while: # imprimindo os valores do vetor
				beq $t0, $t1, saiDaImpressao
				
				li $v0, 1
				
				lw $a0, array3($t0)
				syscall
				
				li $v0, 4 # imprime espaço em branco
				la $a0, espaco
				syscall

				addi $t0, $t0, 4

				j while
			
			saiDaImpressao: # encerrando
				li $v0, 10
				syscall
