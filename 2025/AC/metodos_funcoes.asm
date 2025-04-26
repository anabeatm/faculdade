.data
	msgUsuario: .asciiz "Forneça um número: "
	msgPar: .asciiz "É par."
	msgImpar: .asciiz "É ímpar."
.text
	.main: 
		la $a0, msgUsuario
		jal imprimeString # chama funcao que imprime a string
		
		jal lerInteiro # chama a funcao que lera a entrada
		
		move $a0, $v0 # vai mover o valor de $a0 pra $v0
		jal ehImpar #chama a funcao que retorna os valores
		
		beq $v0, $zero, imprimePar # testa se é par ou impar
				
		la $a0, msgImpar
		jal imprimeString
		
		jal encerrarCodigo # chama funcao que encerra
		
	imprimePar: # imprime se for par
		la $a0, msgPar
		jal imprimeString
		jal encerrarCodigo
	
	ehImpar: #funcao que verifica se é ímpar
	# retornará 1 se for impar
	# retornará 0 se for par
		li $t0, 2
		div $a0, $t0
		mfhi $v0
		
		jr $ra # retorna pra quem chamar essa função
	
	imprimeString: # funcao que imprime string
		li $v0, 4
		syscall
		
		jr $ra
		
	lerInteiro: # funcao que le inteiro
		li $v0, 5
		syscall
		
		jr $ra
		
	encerrarCodigo: # funcao que encerra codigo
		li $v0, 10
		syscall