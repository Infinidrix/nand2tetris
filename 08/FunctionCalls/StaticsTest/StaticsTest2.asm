
        @256
        D=A
        @SP
        M=D
        
    // calling function Sys.init
        
        @_label_1
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @LCL
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @ARG
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THIS
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THAT
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @0
        D=A
        @5
        D=A+D
        @SP
        D=M-D
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Sys.init
        0;JEQ
    (_label_1)
        
        
    // starting function Class1.set
    
    (Class1.set)
        
    // fill 0 zeros
        
    // finish zero fill
        
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
        
        
// popping into static at 0

        @Class1.0
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
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
        
        
// popping into static at 1

        @Class1.1
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
        
    // starting function Class1.get
    
    (Class1.get)
        
    // fill 0 zeros
        
    // finish zero fill
        
// pushing static 0

        @Class1.0
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// pushing static 1

        @Class1.1
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
        
    // starting function Class2.set
    
    (Class2.set)
        
    // fill 0 zeros
        
    // finish zero fill
        
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
        
        
// popping into static at 0

        @Class2.0
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
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
        
        
// popping into static at 1

        @Class2.1
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
        
    // starting function Class2.get
    
    (Class2.get)
        
    // fill 0 zeros
        
    // finish zero fill
        
// pushing static 0

        @Class2.0
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// pushing static 1

        @Class2.1
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
        
    // starting function Sys.init
    
    (Sys.init)
        
    // fill 0 zeros
        
    // finish zero fill
        
// pushing constant 6

        @6
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// pushing constant 8

        @8
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
    // calling function Class1.set
        
        @Sys_label_2
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @LCL
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @ARG
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THIS
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THAT
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @2
        D=A
        @5
        D=A+D
        @SP
        D=M-D
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Class1.set
        0;JEQ
    (Sys_label_2)
        
// popping into temp at 0

        @5
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// pushing constant 23

        @23
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// pushing constant 15

        @15
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
    // calling function Class2.set
        
        @Sys_label_3
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @LCL
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @ARG
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THIS
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THAT
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @2
        D=A
        @5
        D=A+D
        @SP
        D=M-D
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Class2.set
        0;JEQ
    (Sys_label_3)
        
// popping into temp at 0

        @5
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
    // calling function Class1.get
        
        @Sys_label_4
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @LCL
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @ARG
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THIS
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THAT
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @0
        D=A
        @5
        D=A+D
        @SP
        D=M-D
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Class1.get
        0;JEQ
    (Sys_label_4)
        
    // calling function Class2.get
        
        @Sys_label_5
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @LCL
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @ARG
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THIS
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        
        @THAT
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
        @0
        D=A
        @5
        D=A+D
        @SP
        D=M-D
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Class2.get
        0;JEQ
    (Sys_label_5)
        
    (WHILE)
        
        @WHILE
        0;JEQ
        
    (Sys_label_6)
        @Sys_label_6
        0;JEQ
        