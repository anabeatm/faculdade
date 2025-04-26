.data
	msg: .asciiz "Salário: R$"
	zero: .double 0.0
	saida: .asciiz "Seu salário é R$"

.text
	li $v0, 4 #imprime a mensagem
	la $a0, msg
	syscall
	
	li $v0, 7 #lendo o número
	syscall #valor lido estará em f0
	
	ldc1 $f2, zero #f2 recebe zero 0.0 -> tem que ser um rgtr par
	
	add.d $f12, $f2, $f0 #somar o número que leu, somar com zero e atribuir a f12
	
	li $v0, 4
	la $a0, saida
	syscall #imprime saida
	
	li $v0, 3
	syscall #imprime float
	
	li $v0, 10
	syscall #encerra programa