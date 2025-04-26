.data
	pergunta: .asciiz "Digite seu nome: "
	saida: .asciiz "Olá, "
	nome: .space 25
	
.text
	
	li $v0, 4 #impressao da pergunta
	la $a0, pergunta
	syscall
	
	
	li $v0, 8 #leitura do nome
	la $a0, nome
	la $a1, 25
	syscall
	
	la $t1, nome #guarda o ponteiro da string em t1
	
	
	li $v0, 4 #mostra saudacao
	la $a0, saida
	syscall
	
	
	move $a0, $t1 #impressao do nome
	li $v0, 4
	syscall
	
	li $v0, 10 #encerramento
	syscall
	