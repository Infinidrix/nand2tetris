
// pushing constant 0

        @0
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into local at 0

        @LCL
        D=M
        @0
        D=D+A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
    (LOOP_START)
        
// pushing 0 from argument to stack

        @ARG
        D=M
        @0
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
// pushing 0 from local to stack

        @LCL
        D=M
        @0
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
// adding
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M+D
        
// popping into local at 0	

        @LCL
        D=M
        @0
        D=D+A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// pushing 0 from argument to stack

        @ARG
        D=M
        @0
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
// pushing constant 1

        @1
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// substracting
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M-D
        
// popping into argument at 0

        @ARG
        D=M
        @0
        D=D+A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// pushing 0 from argument to stack

        @ARG
        D=M
        @0
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @SP
        M=M-1
        A=M
        D=M
        @LOOP_START
        D;JNE
        
// pushing 0 from local to stack

        @LCL
        D=M
        @0
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
    (BasicLoop_label_1)
        @BasicLoop_label_1
        0;JEQ
        