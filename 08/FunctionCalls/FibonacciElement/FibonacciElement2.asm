
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
        
        
    // starting function Main.fibonacci
    
    (Main.fibonacci)
        
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
        
        
// pushing constant 2

        @2
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// checking less
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M-D
        
        D=M
        M=-1
        @Main_label_2
        D;JLT
        @SP
        M=M-1
        
        @0
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
    (Main_label_2)
        
        @SP
        M=M-1
        A=M
        D=M
        @IF_TRUE
        D;JNE
        
        @IF_FALSE
        0;JEQ
        
    (IF_TRUE)
        
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
        
    (IF_FALSE)
        
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
        
    // calling function Main.fibonacci
        
        @Main_label_3
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
        
        
        @1
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
        @Main.fibonacci
        0;JEQ
    (Main_label_3)
        
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
        
    // calling function Main.fibonacci
        
        @Main_label_4
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
        
        
        @1
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
        @Main.fibonacci
        0;JEQ
    (Main_label_4)
        
// adding
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M+D
        
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
        
// pushing constant 4

        @4
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
    // calling function Main.fibonacci
        
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
        
        
        @1
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
        @Main.fibonacci
        0;JEQ
    (Sys_label_5)
        
    (WHILE)
        
        @WHILE
        0;JEQ
        
    (Sys_label_6)
        @Sys_label_6
        0;JEQ
        