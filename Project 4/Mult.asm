@R0
D=M          // D = R0
@temp
M=D          // temp = R0

@0
D=A
@R2
M=D          // R2 = 0

@R1
D=M
@counter
M=D          // counter = R1

(LOOP)
@counter
D=M
@END
D;JEQ        // if counter == 0, goto END

@temp
D=M
@R2
M=D+M        // R2 = R2 + temp (R0)

@counter
M=M-1        // counter -= 1

@LOOP
0;JMP

(END)
@END
0;JMP        
