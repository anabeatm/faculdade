.text
	li $t0, 75 # $t0 recebe 75
	li $t1, 25 # $t1 recebe 25
	add $s0, $t0, $t1 # s0 = t0 + t1 -> 100 = 75 + 25
	addi $s1, $s0, 36 # s1 = s0 + 36 -> 136 = 100 + 36
	# mesma ideia funciona para sub