
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
        
        
    // starting function Sys.init
    
    (Sys.init)
        
    // fill 0 zeros
        
    // finish zero fill
        
// pushing constant 4000	

        @4000	
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
        
        
// pushing constant 5000

        @5000
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
        
        
    // calling function Sys.main
        
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
        @Sys.main
        0;JEQ
    (Sys_label_2)
        
// popping into temp at 1

        @6
        D=A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
    (Sys.init$LOOP)
        
        @Sys.init$LOOP
        0;JEQ
        
    // starting function Sys.main
    
    (Sys.main)
        
    // fill 5 zeros
        
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
        
        @0
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
    // finish zero fill
        
// pushing constant 4001

        @4001
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
        
        
// pushing constant 5001

        @5001
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
        
        
// pushing constant 200

        @200
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into local at 1

        @LCL
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
        
        
// pushing constant 40

        @40
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into local at 2

        @LCL
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
        
        
// pushing constant 6

        @6
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
// popping into local at 3

        @LCL
        D=M
        @3
        D=D+A
        
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        
        
// pushing constant 123

        @123
        D=A
        
        @SP
        M=M+1
        A=M-1
        M=D
        
    // calling function Sys.add12
        
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
        @Sys.add12
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
        
        
// pushing 2 from local to stack

        @LCL
        D=M
        @2
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
// pushing 3 from local to stack

        @LCL
        D=M
        @3
        A=D+A
        D=M
        
        @SP
        M=M+1
        A=M-1
        M=D
        
        
// pushing 4 from local to stack

        @LCL
        D=M
        @4
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
        
// adding
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M+D
        
// adding
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M+D
        
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
        
    // starting function Sys.add12
    
    (Sys.add12)
        
    // fill 0 zeros
        
    // finish zero fill
        
// pushing constant 4002

        @4002
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
        
        
// pushing constant 5002

        @5002
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
        
        
// pushing constant 12

        @12
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
        
    (Sys_label_4)
        @Sys_label_4
        0;JEQ
        