class Assembler:
    def __init__(self):
        self.symbol_table = {
                "SP": 0,
                "LCL": 1,
                "ARG": 2,
                "THIS": 3,
                "THAT": 4,
                "R0": 0,
                "R1": 1,
                "R2": 2,
                "R3": 3,
                "R4": 4,
                "R5": 5,
                "R6": 6,
                "R7": 7,
                "R8": 8,
                "R9": 9,
                "R10": 10,
                "R11": 11,
                "R12": 12,
                "R13": 13,
                "R14": 14,
                "R15": 15,
                "SCREEN": 16384,
                "KBD": 24576
        }
        self.COMP_MAP = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "M": "1110000",
            "!D": "0001101",
            "!A": "0110001",
            "!M": "1110001",
            "-D": "0001111",
            "-A": "0110011",
            "-M": "1110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "M+1": "1110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "M-1": "1110010",
            "D+A": "0000010",
            "D+M": "1000010",
            "D-A": "0010011",
            "D-M": "1010011",
            "A-D": "0000111",
            "M-D": "1000111",
            "D&A": "0000000",
            "D&M": "1000000",
            "D|A": "0010101",
            "D|M": "1010101"
        }
        self.DEST_MAP = {
            "": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111"
        }
        self.JUMP_MAP = {
            "": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }
        self.output_lines = []
        self.printout = []
        self.built_line = 0
        self.line_count = 0
        self.symbol_lim = 16
    def add_line(self, line):
        self.new_line = line
        self.clean_input()
        if not self.new_line or len(self.new_line) == 0: 
            return
        self.append_output()
    def clean_input(self):
        self.new_line = self.new_line.split('//')[0].strip()
    def append_output(self):
        if self.new_line[0] == "(":
            return self.build_labels()
        self.line_count += 1
        self.output_lines.append(self.new_line)
    def build_labels(self):
        self.symbol_table[self.new_line[1:-1]] = self.line_count

    def build(self):
        for line in self.output_lines:
            if line[0] == "@":
                self.build_a_instruction(line)
            else:
                self.build_c_instruction(line)
        return self.printout
    def build_a_instruction(self, line):
        address = line[1:]
        if not address.isdigit():
            if address not in self.symbol_table:
                self.symbol_table[address] = self.symbol_lim
                self.symbol_lim += 1
            address = self.symbol_table[address]
        else:
            address = int(address) 
        address = bin(address)[2:]
        address = "0"*(16 - len(address)) + address
        self.printout.append(address + "\n")
    def build_c_instruction(self, line):
        dest_inst = line.split("=")
        if len(dest_inst) == 1:
            dest_inst = self.DEST_MAP[""]
        else:
            line = dest_inst[1]
            dest_inst = self.DEST_MAP[dest_inst[0]]
        jump_inst = line.split(";")
        if len(jump_inst) == 1:
            jump_inst = self.JUMP_MAP[""]
        else:
            line = jump_inst[0]
            jump_inst = self.JUMP_MAP [jump_inst[1]]
        comp_inst = self.COMP_MAP[line] 
        self.printout.append("111" + comp_inst + dest_inst + jump_inst + "\n")