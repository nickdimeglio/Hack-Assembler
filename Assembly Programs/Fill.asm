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

// Put your code here.
	
	@8192	 	// identify last screen address
	D=A

	@last
	M=D



	
(CLEARED)		// Screen is clear, wait to blacken

	@SCREEN
	D=A
	
	@pixel
	M=D

	@KBD
	D=M

	@BLACKEN	// If key pressed, blacken screen
	D;JNE

	@CLEARED
	0;JMP

	
(BLACKEN)

	@pixel		// Blacken current pixel
	A=M
	M=-1

	D=A		// Check to see if we're done
	@last	
	D=M-D

	@BLACKENED
	D;JEQ

	@pixel		// If not, increment pixel
	M=M+1

	@BLACKEN
	0;JMP


	
(BLACKENED)		// Screen is black, wait to clear

	@SCREEN
	D=M

	@pixel
	M=D

	@KBD
	D=M

	@CLEAR		// If no key is pressed, clear screen
	D;JEQ

	@BLACKENED
	0;JMP

(CLEAR)

	@pixel		// Blacken current pixel
	A=M
	M=0


	D=A		// Check to see if we're done	
	@last
	D=M-D

	@CLEARED
	D;JEQ

	@p		// If not, increment pixel
	M=M+1

	@CLEAR
	0;JMP
			
