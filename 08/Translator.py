
from typing import Counter


class Translator:
    def __init__(self, filename):
        self.filename = filename
        self.counter = 0
        self.virtual_call_stack = ["Empty"]

    
    variable_hash = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT"
    }
    snippets = {
        "double pop": '''
        @SP
        M=M-1
        A=M
        D=M
        @SP
        A=M-1
        M=M{op}D
        ''',
        "single pop":'''
        @SP
        A=M-1
        M={op}
        ''',
        "comparison": '''
        D=M
        M=-1
        @{CHANGE}
        D;{op}
        @SP
        M=M-1
        {push}
    ({CHANGE})
        ''',
        "pop": '''
        @SP
        M=M-1
        A=M
        M=D+M
        D=M-D
        A=M-D
        M=D
        ''',
        "push":'''
        @SP
        M=M+1
        A=M-1
        M=D
        ''',
        "infinite loop":'''
    ({CHANGE})
        @{CHANGE}
        0;JEQ
        ''',
        'label': '''
    ({label})
        ''',
        'goto':'''
        @{label}
        0;JEQ
        ''',
        'if-goto': '''
        @SP
        M=M-1
        A=M
        D=M
        @{label}
        D;JNE
        ''',
        'lcl reassign': '''
        @LCL
        M=M-1
        A=M
        D=M
        @{segment}
        M=D
        '''
    }
    arithmetic_commands = {
        "add": "\n// adding" + snippets["double pop"].format(op="+"),
        "sub": "\n// substracting" + snippets["double pop"].format(op="-"),
        "neg": "\n// negating" + snippets["single pop"].format(op="-M"),
        "eq": "\n//checking equality" + snippets["double pop"].format(op="-")
                + snippets["comparison"],
        "gt": "\n// checking greater" + snippets["double pop"].format(op="-")
                + snippets["comparison"],
        "lt": "\n// checking less" + snippets["double pop"].format(op="-")
                + snippets["comparison"],
        "and": "\n// checking and" + snippets["double pop"].format(op="&"),
        "or": "\n// checking or" + snippets["double pop"].format(op="|"),
        "not": "\n// checking not" + snippets["single pop"].format(op="!M")
    }

    def next_label(self):
        self.counter += 1
        return f"{self.filename}_label_{self.counter}"

    def finish(self):
        return Translator.snippets["infinite loop"].format(CHANGE=self.next_label())

    def interpret(self, line):
        """
        Entry point of the class, taken a line and 
        returns its assembly version in Hack assembly
        """
        line = Translator.clean_input(line)
        if line[0] == "push":
            return self.push_parser(line)
        elif line[0] == "pop":
            return self.pop_parser(line)
        elif line[0] in Translator.arithmetic_commands:
            return self.format_output(line[0])
        elif line[0] in ['label', 'goto', 'if-goto']:
            return self.snippets[line[0]].format(label= f'{self.virtual_call_stack[-1]}${line[1]}')
        elif line[0] in ['function', 'call', 'return']:
            return self.function_parser(line)
        return ""
    
    @staticmethod
    def clean_input(line):
        """
        Removes comments and unnessary whitespace
        """
        return line.split("//")[0].split(" ")

    def push_parser(self, command):
        if command[1] in Translator.variable_hash:
            return f"\n// pushing {command[2]} from {command[1]} to stack\n{Translator.push(Translator.variable_hash[command[1]], int(command[2]))}"
        elif command[1] == "constant":
            return f"\n// pushing constant {command[2]}\n{Translator.push_constant(command[2])}"
        elif command[1] == "temp":
            return f"\n// pushing temp {command[2]}\n{Translator.push_temp(command[2])}"
        elif command[1] == "static":
            return f"\n// pushing static {command[2]}\n{self.push_static(command[2])}"
        elif command[1] == "pointer":
            pointing = "this" if command[2] == "0" else "that"
            return f"\n//pushing pointer {command[2]}\n{Translator.push_pointer(Translator.variable_hash[pointing])}" 


    def format_output(self, line):
        if line == "eq":
            return Translator.arithmetic_commands[line].format(op='JEQ', CHANGE=str(self.next_label()), push=Translator.push_constant(0))
        elif line == "gt":
            return Translator.arithmetic_commands[line].format(op='JGT',  CHANGE=str(self.next_label()), push=Translator.push_constant(0))
        elif line == "lt":
            return Translator.arithmetic_commands[line].format(op='JLT',  CHANGE=str(self.next_label()), push=Translator.push_constant(0))
        else:
            return Translator.arithmetic_commands[line]

    def push_static(self, value):
        return f'''
        @{self.filename+"."+value}
        D=M
        {Translator.snippets['push']}'''

    @staticmethod
    def push_temp(value):
        return f'''
        @{5+int(value)}
        D=M
        {Translator.snippets['push']}'''

    @staticmethod
    def push_constant(constant):
        return f'''
        @{constant}
        D=A
        {Translator.snippets['push']}'''

    @staticmethod
    def push_pointer(pointer):
        return f'''
        @{pointer}
        D=M
        {Translator.snippets['push']}'''

    @staticmethod
    def push_state(segment):
        return f'''
        @{segment}
        D=M
        {Translator.snippets['push']}
        '''

    @staticmethod
    def push(segment, location):
        return f'''
        @{segment}
        D=M
        @{location}
        A=D+A
        D=M
        {Translator.snippets['push']}
        '''
    
    def pop_parser(self, command):
        if command[1] in Translator.variable_hash:
            return f"\n// popping into {command[1]} at {command[2]}\n{Translator.pop(Translator.variable_hash[command[1]], int(command[2]))}"
        elif command[1] == "temp":
            return f"\n// popping into {command[1]} at {command[2]}\n{Translator.pop_temp(command[2])}"
        elif command[1] == "static":
            return f"\n// popping into {command[1]} at {command[2]}\n{self.pop_static(command[2])}"
        elif command[1] == "pointer":
            pointing = "this" if command[2] == "0" else "that"
            return f"\n//popping into {command[1]} at {command[2]}\n{Translator.pop_pointer(Translator.variable_hash[pointing])}"

    @staticmethod
    def pop(segment, location):
        return f'''
        @{segment}
        D=M
        @{location}
        D=D+A
        {Translator.snippets['pop']}
        '''

    @staticmethod
    def pop_temp(value):
        return f'''
        @{5+int(value)}
        D=A
        {Translator.snippets['pop']}
        '''

    def pop_static(self, value):
        return f'''
        @{self.filename+"."+value}
        D=A
        {Translator.snippets['pop']}
        '''

    @staticmethod
    def pop_pointer(pointer):
        return f'''
        @{pointer}
        D=A
        {Translator.snippets['pop']}
        '''
    
    def bootstrap(self):
        '''
        returns bootstrap code for the beginning of
        the vm implementation
        '''
        return f"""
        @256
        D=A
        @SP
        M=D
        {self.function_call(["call", "Sys.init", '0'])}
        """

    def function_parser(self, line):
        switch = {
            'return': self.function_return,
            'function': self.function_start,
            'call': self.function_call }
        return switch[line[0]](line)

    def function_start(self, line):
        self.virtual_call_stack.append(line[1])
        return f'''
    // starting function {line[1]}
    {Translator.snippets['label'].format(label=f'{line[1]}')}
    // fill {line[2]} zeros
        {Translator.push_constant(0)*(int(line[2]))}
    // finish zero fill
        '''

    def function_call(self, line):
        return_label = self.next_label()
        return f'''
    // calling function {line[1]}
        {Translator.push_constant(return_label)}
        {Translator.push_state("LCL")}
        {Translator.push_state("ARG")}
        {Translator.push_state("THIS")}
        {Translator.push_state("THAT")}
        @{line[2]}
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
        @{line[1]}
        0;JEQ
    ({return_label})
        '''
    
    def function_return(self, line):
        return f'''
    // returning from function
        @5
        D=A
        @LCL
        A=M-D
        D=M
        @SP
        A=M
        M=D
        {Translator.pop('ARG', '0')}
        {Translator.snippets['lcl reassign'].format(segment = "THAT")}
        {Translator.snippets['lcl reassign'].format(segment = "THIS")}
        {Translator.push_state("ARG")}
        {Translator.snippets['lcl reassign'].format(segment = "ARG")}
        {Translator.snippets['lcl reassign'].format(segment = "LCL")}
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
        '''