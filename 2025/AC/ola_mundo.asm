.data # área para dados na memória principal
	msg: .asciiz "Olá, mundo!" # mensagem a ser exibida

.text #área para instruções do programa
	li $v0, 4 # instrução para impressão de String
	la $a0, msg # indicar o endereço em que está a msg
	syscall # faça! Imprima
	
	# salva ctrl+s, run assemble f3, executar f5
