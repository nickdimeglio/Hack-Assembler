// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

	@prod	// set product = 0
	M=0

	@R0	// If arg1 is 0, end
	D=M

	@END
	D;JEQ

	@x	// else assign to xs
	M=D
	
	@R1	// If arg2 is0, end
	D=M

	@END
	D;JEQ

	@i	// else assign to i
	M=D 

(LOOP)

	@x
	D=M

	@prod	// Add x to product
	M=M+D
	
	@i
	M=M-1	// Subtract 1 from multiplier
	D=M

	@LOOP	// Repeat if i > 0
	D;JGT

(END)
	@prod
	D=M

	@R2
	M=D
	
	@END
	0;JMP
