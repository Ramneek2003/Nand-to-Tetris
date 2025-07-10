(START)
@KBD
D=M
@BLACK_SCREEN
D;JNE        // If a key is pressed, jump to BLACK_SCREEN

// Otherwise, clear screen (set to white)
@0
D=A
@i
M=D          // i = 0

(WHITE_LOOP)
@i
D=M
@8192
D=D-A
@START
D;JEQ        // If i == 8192, go back to START

@i
D=M
@SCREEN
A=A+D        // A = SCREEN + i
M=0          // Set pixel to white

@i
M=M+1        // i++
@WHITE_LOOP
0;JMP


(BLACK_SCREEN)
@0
D=A
@i
M=D          // i = 0

(BLACK_LOOP)
@i
D=M
@8192
D=D-A
@START
D;JEQ        // If i == 8192, go back to START

@i
D=M
@SCREEN
A=A+D        // A = SCREEN + i
M=-1         // Set pixel to black

@i
M=M+1        // i++
@BLACK_LOOP
0;JMP