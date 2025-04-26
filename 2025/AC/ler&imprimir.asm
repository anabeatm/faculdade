.data
	saudacao: .asciiz "Digite sua idade: "
	saida: .asciiz "Sua idade é "
	
.text
	li $v0, 4 # imprimir string
	la $a0, saudacao
	syscall # imprime a mensagem saudação
	
	li $v0, 5 # leitura de int
	syscall
	
	move $t0, $v0 # valor fornecido está em t0
	
	li $v0, 4
	la $a0, saida
	syscall # imprime saida
	
	li $v0, 1
	move $a0, $t0 # move valor que está em t0 para ser impresso em a0
	syscall
	
	li $v0, 10
	syscall
	