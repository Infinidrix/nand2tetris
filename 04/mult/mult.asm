// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Load R0, set i = R0 and sum = 0
	@R0
	D=M

	@i
	M=D

	@sum
	M=0

// Loops until i == 0 (R0 times)
(LOOP)
	@i
	D=M

	@END
	D;JEQ

	@R1 // load R1
	D=M

	@sum // add R1 to 
	M=D+M

	@i  // decrement i by 1
	M=M-1

	@LOOP
	0;JMP

(END)
@sum 
D=M

@R2 // assign sum to R2
M=D

(ENDLOOP)
@ENDLOOP
0;JMP