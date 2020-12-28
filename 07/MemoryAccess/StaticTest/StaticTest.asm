
// pushing constant 111

        @111
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// pushing constant 333

        @333
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// pushing constant 888

        @888
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into static at 8

        @StaticTest.8
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// popping into static at 3

        @StaticTest.3
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// popping into static at 1

        @StaticTest.1
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// pushing static 3

        @StaticTest.3
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// pushing static 1

        @StaticTest.1
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
        
// pushing static 8

        @StaticTest.8
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
        
    (EDXNZLPLME)
        @EDXNZLPLME
        0;JEQ
        