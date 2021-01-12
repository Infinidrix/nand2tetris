from io import TextIOBase


class CodeWriter:
    def __init__(self, output: TextIOBase):
        self.output = output
        self.class_symbol_table = {}
        self.method_symbol_table = {}
        self.subroutine_name = None
        self.class_name = None
        self.label_count = 0
        self.label_stack = []
        self.arg_counts = []
        self.subroutine_type = "None"

    OPS = {
        "+": """
add""",
        "-": """
sub""",
        "*": """
call Math.multiply 2""",
        "/": """
call Math.divide 2""",
        "&": """
and""",
        "|": """
or""",
        "<": """
lt""",
        ">": """
gt""",
        "=": """
eq"""
    }

    KEYWORDS = {
        "true": """
push constant 1
neg""",
        "false": """
push constant 0""",
        "null": """
push constant 0""",
        "this": """
push pointer 0""" # TODO: make sure that constructor has this working
    }

    SNIPPETS = {
        "declare function": """
function {class_name}.{subrout} {local}""",
        "declare constructor": """
function {class_name}.new {local}
push constant {size}
call Memory.alloc 1
pop pointer 0""",
        "declare method": """
function {class_name}.{subrout} {local}
push argument 0
pop pointer 0""",
        "let statement": """
pop {segment} {location}""",
        "let array": """
pop temp 0
push {segment} {location}
add
pop pointer 1
push temp 0
pop that 0""",
        "array reference": """
push {segment} {location}
add
pop pointer 1
push that 0""", 
        "cond statement": """
not
if-goto {not_label}""",
        "else statement": """ 
goto {finish_label}
label {prev_label}""",
        "while statement": """ 
goto {prev_label}
label {finish_label}""",
        "push char": """
push constant {char}
call String.appendChar 2""",

        "string": """
push constant {size}
call String.new 1{calls}"""    
    }

    def subroutine_dec(self, name, subroutine_type):
        self.subroutine_name = name
        self.method_symbol_table.clear()
        self.method_symbol_table[".local"] = 0
        self.method_symbol_table[".argument"] = 0
        if subroutine_type == "method":
            self.method_symbol_table[".argument"] = 1
            self.method_symbol_table["this"] = ["this", self.class_name, "argument", 0]
        self.subroutine_type = subroutine_type

    def subroutine_body(self):
        if self.subroutine_type == "constructor":
            self.output.write(CodeWriter.SNIPPETS["declare constructor"].format(class_name = self.class_name, local = self.method_symbol_table[".local"], size = self.class_symbol_table[".field"]))
        elif self.subroutine_type == "method":
            self.output.write(CodeWriter.SNIPPETS["declare method"].format(class_name = self.class_name, subrout = self.subroutine_name, local = self.method_symbol_table[".local"]))
        elif self.subroutine_type == "function":
            self.output.write(CodeWriter.SNIPPETS["declare function"].format(class_name = self.class_name, subrout = self.subroutine_name, local = self.method_symbol_table[".local"]))
        else:
            print(f"this shouldn't be happening with function types: {self.subroutine_type}")

            
    def print_subroutine(self):
        print(f"""
For subroutine {self.subroutine_name} in {self.class_name} we have
{self.method_symbol_table}""")


    def print_class(self):
        print(f"""
For class {self.class_name} we have
{self.class_symbol_table}""")

    def params_list(self, param):
        self.method_symbol_table[param[0]] = param + ["argument", self.method_symbol_table[".argument"]]
        self.method_symbol_table[".argument"] += 1

    def class_dec(self, name):
        self.class_name = name
        self.class_symbol_table.clear()
        self.class_symbol_table[".field"] = 0
        self.class_symbol_table[".static"] = 0

    def class_var_dec(self, var):
        var_scope = "." + var[2]
        var[2] = var[2] if var[2] != "field" else "this"
        self.class_symbol_table[var[0]] = var + [self.class_symbol_table[var_scope]]
        self.class_symbol_table[var_scope] += 1

    def subroutine_var_dec(self, var):
        self.method_symbol_table[var[0]] = var + [self.method_symbol_table[".local"]]
        self.method_symbol_table[".local"] += 1

    def symbol_lookup(self, identifier):
        if identifier in self.method_symbol_table:
            return (self.method_symbol_table[identifier])
        return (self.class_symbol_table[identifier])
    def is_var(self, identifier):
        return (identifier in self.method_symbol_table or identifier in self.class_symbol_table)
    
    def let_statement(self, identifier, is_arr):
        entry = self.symbol_lookup(identifier)
        if is_arr:
            return self.output.write(CodeWriter.SNIPPETS["let array"].format(segment = entry[2], location = entry[3]))
        self.output.write(CodeWriter.SNIPPETS["let statement"].format(segment = entry[2], location = entry[3]))

    def if_start(self):
        self.label_count += 1
        self.label_stack.append(f"{self.class_name}.{self.subroutine_name}.{self.label_count}")
        self.output.write(CodeWriter.SNIPPETS["cond statement"].format(not_label = self.label_stack[-1]))

    def else_start(self):
        self.label_count += 1
        prev_label = self.label_stack.pop()
        self.label_stack.append(f"{self.class_name}.{self.subroutine_name}.{self.label_count}")
        self.output.write(CodeWriter.SNIPPETS["else statement"].format(finish_label = self.label_stack[-1], prev_label = prev_label))

    def if_end(self):
        self.output.write(f"""
label {self.label_stack.pop()}""")

    def while_begin(self):
        self.label_count += 1
        self.label_stack.append(f"{self.class_name}.{self.subroutine_name}.{self.label_count}")
        self.output.write(f"""
label {self.label_stack[-1]}""")

    def while_start(self):
        self.if_start()

    def while_end(self):
        finish_label = self.label_stack.pop()
        prev_label = self.label_stack.pop()
        self.output.write(CodeWriter.SNIPPETS["while statement"].format(prev_label = prev_label, finish_label = finish_label))

    def return_statement(self, has_expr):
        if has_expr:
            return self.output.write("""
return""")

        self.output.write("""
push constant 0
return""")
    
    def do_statement(self):
        self.output.write("""
pop temp 0""")

    def subroutine_call_start(self, identifier): 
        self.arg_counts.append(0)
        if identifier == None:
            self.arg_counts[-1] += 1
            self.output.write(f"""
push pointer 0""")
        elif self.is_var(identifier):
            self.arg_counts[-1] += 1
            entry = self.symbol_lookup(identifier)
            self.output.write(f"""
push {entry[2]} {entry[3]}""")

    def add_args(self, arg_count):
        self.arg_counts[-1] += arg_count

    def subroutine_call_end(self, identifier, subroutine):
        if not identifier:
            identifier = self.class_name
        if self.is_var(identifier):
            identifier = self.symbol_lookup(identifier)[1]
        self.output.write(f"""
call {identifier}.{subroutine} {self.arg_counts.pop()}""")

    def push_op(self, op):
        self.output.write(CodeWriter.OPS[op])

    def push_int(self, num):
        self.output.write(f"""
push constant {num}""")
    
    def push_string(self, string):
        self.output.write(CodeWriter.SNIPPETS["string"]\
                .format(size = len(string), \
                calls = "".join([CodeWriter.SNIPPETS["push char"].format(char = ord(c)) for c in string])))

    def push_keyword(self, keyword):
        self.output.write(CodeWriter.KEYWORDS[keyword])

    def array_reference(self, identifier):
        entry = self.symbol_lookup(identifier)
        self.output.write(CodeWriter.SNIPPETS["array reference"].format(segment = entry[2], location = entry[3]))
    
    def push_unary_op(self, op):
        self.output.write(f"""
{"neg" if op == "-" else "not"}""")
    
    def push_var(self, var):
        entry = self.symbol_lookup(var)
        self.output.write(f"""
push {entry[2]} {entry[3]}""")
