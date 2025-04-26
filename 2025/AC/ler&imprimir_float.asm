.data
	msg: .asciiz "Salário: R$"
	zero: .float 0.0
	saida: .asciiz "Seu salário é R$"

.text
	li $v0, 4 #imprime a mensagem
	la $a0, msg
	syscall
	
	li $v0, 6 #lendo o número
	syscall #valor lido estará em f0
	
	lwc1 $f1, zero #f1 recebe zero 0.0
	
	add.s $f12, $f1, $f0 #somar o número que leu, somar com zero e atribuir a f12
	
	li $v0, 4
	la $a0, saida
	syscall #imprime saida
	
	li $v0, 2
	syscall #imprime float
	
	li $v0, 10
	syscall #encerra programa