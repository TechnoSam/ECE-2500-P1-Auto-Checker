add $t3, $s0, $s1
addi $t4, $s1, 117
addiu $t4, $s1, 117
addu $t3, $s0, $s1
and $t0, $s6, $s7
andi $t0, $s1, 0xdead
beq $t0, $zero, HYPERSPACE
bne $t0, $s1, HYPERSPACE
lbu $t4, 8($s3)
lhu $t4, 12($s4)
ll $t4, 16($s5)
lui $t1 0xcafe
lw $t4, 20($s6)
nor $t7, $s3, $s4
or $t7, $s3, $s4
ori $t7, $s3, 0xBEEF
HYPERSPACE:
slt $s1, $t0, $t1
slti $s1, $t0, 0xbabe
sltiu $s1, $t0, 0xbabe
sltu $s1, $t0, $t1
sll $s2, $t3, 2
srl $s4, $t4, 31
sb $t4, 8($s3)
sc $s1, 24($s7)
sh $t4, 12($s4)
sw $t4, 20($s6)
sub $t3, $s0, $s1
subu $t3, $s0, $s1
