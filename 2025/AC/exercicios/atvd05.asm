.data
	n: .asciiz "Escreva um número limite: "
	espaco: .asciiz " - "
	msgNewLine: .asciiz "\n"

	array: .word 0:100       
	arrayDoQuadradoPft: .word 0:100

.text
	main:
		# solicita um número
		li $v0, 4
		la $a0, n
		syscall
	
		li $v0, 5         # leitura de número
		syscall
	
		move $t0, $v0     # número limite informado pelo usuário
	

		li $t1, 1         # cont
		la $t2, array     # i
		
	preenchendoVetor:
	
		bgt $t1, $t0, fimPreenchendoVetor  # se $t1 > $t0, sai
		
		sw $t1, ($t2)     # armazena $t1 no vetor
		addi $t1, $t1, 1  # cont++
		addi $t2, $t2, 4  # i++
		
		j preenchendoVetor
		
	fimPreenchendoVetor:
	
		li $t1, 0         # cont
		la $t2, array     # i
		la $t3, arrayDoQuadradoPft  # j
		
		percorrendoVetor:
			bge $t1, $t0, fimPercorrendoVetor  # se $t1 >= $t0, sai

			lw $t4, ($t2)         # carrega valor do array
			mul $t5, $t4, $t4     # calcula o quadrado
			sw $t5, ($t3)         # armazena o quadrado no vetor dos quadrados pfts
			
			addi $t1, $t1, 1      # cont++
			addi $t2, $t2, 4      # i++
			addi $t3, $t3, 4      # j++
			
			j percorrendoVetor
		
		fimPercorrendoVetor:
	
		# imprimindo valores
		li $t1, 0 # cont
		la $t2, array # i
		la $t3, arrayDoQuadradoPft # j
		
		imprimindoValores:
			bge $t1, $t0, fimImprimindoValores # se $t1 >= $t0, sai
			
			# imprime número
			li $v0, 1
			lw $a0, ($t2)     
			syscall
			
			# imprime " - "
			li $v0, 4
			la $a0, espaco 
			syscall
			
			# imprime o quadrado
			li $v0, 1
			lw $a0, ($t3)      
			syscall
			
			# new line
			li $v0, 4
			la $a0, msgNewLine 
			syscall

			addi $t1, $t1, 1
			addi $t2, $t2, 4
			addi $t3, $t3, 4
			
			j imprimindoValores
			
		fimImprimindoValores:
			li $v0, 10
			syscall
