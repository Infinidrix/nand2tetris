
// pushing constant 3030

        @3030
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
//popping into pointer at 0

        @THIS
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// pushing constant 3040

        @3040
        D=A
        
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
        
        
// pushing constant 32

        @32
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into this at 2

        @THIS
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
        
        
// pushing constant 46

        @46
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into that at 6

        @THAT
        D=M
        @6
        D=D+A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
//pushing pointer 0

        @THIS
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
//pushing pointer 1

        @THAT
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
        
// pushing 2 from this to stack

        @THIS
        D=M
        @2
        A=D+A
        D=M
        
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
        
// pushing 6 from that to stack

        @THAT
        D=M
        @6
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
        
    (YIAKJJCAED)
        @YIAKJJCAED
        0;JEQ
        