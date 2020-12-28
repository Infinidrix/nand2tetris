
    // starting function SimpleFunction.test
    
    (SimpleFunction.test)
        
    // fill 2 zeros
        
        @0
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        @0
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
    // finish zero fill
        
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
        
        
// pushing 1 from local to stack

        @LCL
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
        
// checking not
        @SP
        A=M-1
        M=!M
        
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
        
        
// adding
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M+D
        
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
        
        
// substracting
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M-D
        
    // returning from function
        @5
        D=A
        @LCL
        A=M-D
        D=M
        @SP
        A=M
        M=D
        
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
        
        
        
        @LCL
        M=M-1
        A=M
        D=M
        @THAT
        M=D
        
        
        @LCL
        M=M-1
        A=M
        D=M
        @THIS
        M=D
        
        
        @ARG
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @LCL
        M=M-1
        A=M
        D=M
        @ARG
        M=D
        
        
        @LCL
        M=M-1
        A=M
        D=M
        @LCL
        M=D
        
        @SP
        A=M-1
        D=M+1
        @SP
        M=M+D
        D=M-D
        M=M-D
        A=D
        A=M
        0;JEQ
        
    (SimpleFunction_label_1)
        @SimpleFunction_label_1
        0;JEQ
        