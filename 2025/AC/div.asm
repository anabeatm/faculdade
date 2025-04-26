.text
	li $t0, 10 
	li $t1, 2 
	div $t0, $t1 # realiza a divisão inteira
	# parte inteira vai para lo e o resto vai para hi
	
	srl $s2, $t0, 2 # divide por 2 casas a direita
	
	mflo $s0 # move o contéudo de lo para s0
	mfhi $s1 # move o contéudo de hi para s1
	
	
	
	
	li $v0, 10
	syscall
	
	