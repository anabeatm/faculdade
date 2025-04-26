.data
	meuArray: 
		.align 2
		.space 16 #aloca 4 espaços no array (4x4)
.text
	move  $t0, $zero #indice do array
	move $t1, $zero #valor a ser alocado no array
	li $t2, 16 #tamamho do array
	for:
		beq $t0, $t2, saida
		sw $t1, meuArray($t0)
		addi $t0, $t0, 4 #sobe em relação ao tamanho do dado (4 bytes)
		addi $t1, $t1, 1 #valor vai ser somado em 1 unid
		j for
		
	saida:
		move  $t0, $zero
		imprime:
			beq $t0, $t2, saiDaImpressao
			li $v0, 1
			lw $a0, meuArray($t0)
			syscall
			
			addi $t0, $t0, 4
			j imprime
		
		saiDaImpressao:
			li $v0, 10
			syscall
		