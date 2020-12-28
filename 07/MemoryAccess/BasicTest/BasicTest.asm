
// pushing constant 10

        @10
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into ['pop', 'local', '0']

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
        
        
// pushing constant 21

        @21
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// pushing constant 22

        @22
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into ['pop', 'argument', '2']

        @ARG
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
        
        
// popping into ['pop', 'argument', '1']

        @ARG
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
        
        
// pushing constant 36

        @36
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into ['pop', 'this', '6']

        @THIS
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
        
        
// pushing constant 42

        @42
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// pushing constant 45

        @45
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into ['pop', 'that', '5']

        @THAT
        D=M
        @5
        D=D+A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// popping into ['pop', 'that', '2']

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
        
        
// pushing constant 510

        @510
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into ['pop', 'temp', '6']

        @11
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
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
        
        
// pushing 5 from that to stack

        @THAT
        D=M
        @5
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
        
// pushing 6 from this to stack

        @THIS
        D=M
        @6
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
// pushing 6 from this to stack

        @THIS
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
        
// substracting
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M-D
        
// pushing temp 6

        @11
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
        
    (SGSCNFWTTM)
        @SGSCNFWTTM
        0;JEQ
        