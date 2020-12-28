// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// probe keyboard input
(LOOP)
	@i
	M=0

	@KBD
	D=M

	@PRINT_WHITE
	D;JEQ

(PRINT_BLACK)
	@SCREEN
	D=A

	@i
	A=D+M
	M=-1

	@i
	M=M+1

	// check if end of screen memory map
	@KBD
	D=A
	@keyboard_address
	M=D
	@SCREEN
	D=A
	@i
	D=D+M
	@keyboard_address
	D=M-D
	@LOOP
	D;JEQ
	@PRINT_BLACK
	0;JMP


(PRINT_WHITE)
	@SCREEN
	D=A

	@i
	A=D+M
	M=0

	@i
	M=M+1
	// check if end of screen memory map
	@KBD
	D=A
	@keyboard_address
	M=D
	@SCREEN
	D=A
	@i
	D=D+M
	@keyboard_address
	D=M-D
	@LOOP
	D;JEQ
	@PRINT_WHITE
	0;JMP