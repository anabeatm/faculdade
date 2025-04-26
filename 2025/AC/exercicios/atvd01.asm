# Elabore um código assembly que calcule o resultado da seguinte somatória, 
# onde n deverá ser especificado em um registrador. 
# Imprimir o resultado usando chamadas de sistema.
.data
	msgUsuario: .asciiz "Forneça um número: "
	somaTotal: .asciiz "Sua soma é: "

.text
	li $v0, 4 # imprime mensagem pro usuário
	la $a0, msgUsuario
	syscall
	
	li $v0, 5 # le o número que foi fornecido
	syscall
	move $t0, $v0 # move ele para t0
	
	move $t1, $zero # cria indice
	
	move $t2, $zero # cria registrador que guardará a soma
	
	for: 
		bgt $t1, $t0, saida # enquanto t1 < t0
		
		add $t2, $t2, $t1 # faz a soma: t2 = t2 + t1
		
		addi $t1, $t1, 1 # icrementa o indice
		
		j for # jump for
		
	saida:
		li $v0, 4 # imprime mensagem
		la $a0, somaTotal
		syscall
	
		li $v0, 1 # imprime soma
		move $a0, $t2
		syscall
	
		li $v0, 10 # encerra
		syscall