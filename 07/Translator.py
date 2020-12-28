
from random import choice
from string import ascii_uppercase


class Translator:
    def __init__(self, filename):
        self.filename = filename

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

    @staticmethod
    def random(size = 10):
        return "".join([choice(ascii_uppercase) for _ in range(size)])

    @staticmethod
    def finish():
        return Translator.snippets["infinite loop"].format(CHANGE=Translator.random())

    def interpret(self, line):
        """
        Entry point of the class, taken a line and 
        returns it's assembly version in Hack assembly
        """
        line = Translator.clean_input(line)
        if line[0] == "push":
            return self.push_parser(line)
        elif line[0] == "pop":
            return self.pop_parser(line)
        elif line[0] in Translator.arithmetic_commands:
            return Translator.format_output(line[0])
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


    @staticmethod
    def format_output(line):
        # print(f'Got here {line}, {Translator.arithmetic_commands}')
        if line == "eq":
            return Translator.arithmetic_commands[line].format(op='JEQ', CHANGE=str(Translator.random()), push=Translator.push_constant(0))
        elif line == "gt":
            return Translator.arithmetic_commands[line].format(op='JGT',  CHANGE=str(Translator.random()), push=Translator.push_constant(0))
        elif line == "lt":
            return Translator.arithmetic_commands[line].format(op='JLT',  CHANGE=str(Translator.random()), push=Translator.push_constant(0))
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
    def push(segment, location):
        return f'''
        @{segment}
        D=M
        @{location}
        A=D+A
        D=M
        {Translator.snippets['push']}
        '''
    
    def pop_parser(self, command: str):
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