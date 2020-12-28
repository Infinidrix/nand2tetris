
// pushing 1 from argument to stack

        @ARG
        D=M
        @1
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
//popping into pointer at 1

        @THAT
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// pushing constant 0

        @0
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into that at 0

        @THAT
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
        
        
// pushing constant 1

        @1
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into that at 1

        @THAT
        D=M
        @1
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
        
        
// pushing constant 2

        @2
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
        
        
    (Empty$MAIN_LOOP_START)
        
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
        @Empty$COMPUTE_ELEMENT
        D;JNE
        
        @Empty$END_PROGRAM
        0;JEQ
        
    (Empty$COMPUTE_ELEMENT)
        
// pushing 0 from that to stack

        @THAT
        D=M
        @0
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
// pushing 1 from that to stack

        @THAT
        D=M
        @1
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
        
// popping into that at 2

        @THAT
        D=M
        @2
        D=D+A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
//pushing pointer 1

        @THAT
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
        
// adding
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M+D
        
//popping into pointer at 1

        @THAT
        D=A
        
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
        
        
        @Empty$MAIN_LOOP_START
        0;JEQ
        
    (Empty$END_PROGRAM)
        
    (FibonacciSeries_label_1)
        @FibonacciSeries_label_1
        0;JEQ
        