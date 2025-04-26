.data
	msg: .asciiz "Número Inteiro: "
	par: .asciiz "O número é par"
	impar: .asciiz "O número é ímpar"
	
.text
	li $v0, 4 #imprimir msg na tela
	la $a0, msg
	syscall
	
	li $v0, 5 #lendo o número
	syscall
	
	li $t0, 2 #armazena 2 no registrador t0
	
	div $v0, $t0 #realiza a divisão dos numeros
	
	mfhi $t1 # t1 recebe o resto da divisão
	
	beq $t1, $zero, imprimePar #se t1 == 0, imprime a partir do rótulo (PULE)
	#se t1 != 0, realize a instrução a seguir (NÃO PULE)
	li $v0, 4
	la $a0, impar
	syscall
	
	li $v0, 10 #encerra o programa antes de ele realizar a instrução de par
	syscall
	
	imprimePar: #rótulo
		li $v0, 4
		la $a0, par
		syscall
		
	li $v0, 10 #encerra o programa com imprimePar sendo realizado
	syscall
	
	