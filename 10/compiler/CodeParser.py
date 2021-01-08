
from io import TextIOBase

class CodeParser:

    KEYWORDS = {
        "class", "constructor", "function", "method", "field",
        "static", "var", "int", "char", "boolean", "void", "true",
        "false", "null", "this", "let", "do", "if", "else",
        "while", "return"
    }
    SYMBOLS = {i: i for i in "{}()[].,;+-*/&|<>=-~"}
    SYMBOLS[">"] = "&gt;"
    SYMBOLS["<"] = "&lt;"
    SYMBOLS["&"] = "&amp;"

    def __init__(self, input: TextIOBase, output: TextIOBase):
        self.input = input
        self.output = output
        self.tokens = []
        self.location = 0
        self.generate_tokens()
        self.parse_file()

    def next_token(self):
        if self.location >= len(self.tokens):
            return
        self.location += 1
        return self.tokens[self.location - 1]

    def peek(self):
        if self.location >= len(self.tokens):
            return
        return self.tokens[self.location]


    def generate_tokens(self):
        def choose_type(curr_type, curr_token):
            if curr_type == "integerConstant":
                return curr_type, curr_token
            else:
                return "identifier", curr_token

        curr_token = "" # comment, integerConstant, stringConstant, keyword
        curr_type = ""
        value = self.input.read(1)
        while value:
            # If we're building a String constant
            if curr_type == "stringConstant" and value != '"':
                curr_token += value
                value = self.input.read(1)
                continue
            elif curr_type == 'block comment':
                if value == '*':
                    value = self.input.read(1)
                    if value == '/':
                        curr_type = ""
                value = self.input.read(1)
                continue
                
            # If prev concat made a keyword
            if curr_token in CodeParser.KEYWORDS:
                self.tokens.append((curr_type, curr_token))
                curr_token = ""
                curr_type = ""
            # If we are dealing with a number
            if value.isdigit():
                if not curr_token:
                    curr_type = "integerConstant"
                    curr_token = value
                else:
                    curr_token += value

            # check for block comment
            elif value == "/" and curr_type == 'symbol':
                curr_token = ""
                curr_type = ""
                self.input.readline()
            elif value == "*": 
                if curr_type == 'symbol':
                    curr_token = ""
                    curr_type = "block comment"
                else:
                    if curr_token:
                        self.tokens.append(choose_type(curr_type, curr_token))
                    self.tokens.append(('symbol', value))

            # check if / appeared in anticipation of comment
            # checks for whether there is a comment are above
            elif curr_token in CodeParser.SYMBOLS:
                self.tokens.append((curr_type, CodeParser.SYMBOLS[curr_token]))
                curr_token = ""
                curr_type = "" 
            # if / saves it to look ahead for comments
            elif value == "/":
                if curr_token: self.tokens.append(choose_type(curr_type, curr_token))
                curr_type = "symbol"
                curr_token = "/"
            # in case of whitespace return the token found so far
            elif value == " " and curr_token:
                self.tokens.append(choose_type(curr_type, curr_token))
                curr_token = ""
                curr_type = ""
            # checks if encoutered a symbol
            elif value in CodeParser.SYMBOLS:
                if curr_token:
                    self.tokens.append(choose_type(curr_type, curr_token))
                curr_token = ""
                curr_type = ""
                self.tokens.append(('symbol', CodeParser.SYMBOLS[value]))
            
            # check whether to terminate or start a StringConstant
            elif value == '"':
                if curr_type == "stringConstant":
                    self.tokens.append((curr_type, curr_token))
                    curr_token = ""
                    curr_type = ""
                else:
                    if curr_token: self.tokens.append((curr_type, curr_token))
                    curr_token = ""
                    curr_type = "stringConstant"
            elif (value.isalpha() or value == "_"): 
                if not curr_token:
                    curr_type = "keyword"
                    curr_token = value
                else:
                    curr_token += value
            value = self.input.read(1)

    def parse_file(self):
        token = self.next_token()
        while token:
            # determine what to do based on the token
            if token[1] == "class":
                self.compile_class(0, token)
            elif token[1] == "var":
                self.compile_var_dec(0, token)
            elif token[1] == "static" or token[1] == "field":
                self.compile_class_var_dec(0, token)
            elif token[1] == "let":
                self.compile_let(0, token)
            elif token[1] == "if":
                self.compile_if(0, token)
            elif token[1] == "while":
                self.compile_while(0, token)
            elif token[1] == "do":
                self.compile_do(0, token)
            elif token[1] == "return":
                self.compile_return(0, token)
            token = self.next_token()
    def compile_class(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(space_indent_prev + "<class>\n")

        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        token = self.next_token()
        while token:
            if token[1] == "static" or token[1] == "field":
                self.compile_class_var_dec(indent + 1, token)
            elif token[1] in ["constructor", "function", "method"]:
                self.compile_subroutine(indent + 1, token)
            elif token[1] == "}":
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
                break
            else:
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            token = self.next_token()
        self.output.write(f"{space_indent_prev}</class>\n")

    def compile_class_var_dec(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<classVarDec>\n")
        
        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        token = self.next_token()
        while token:
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            if token[1] == ";":
                break
            token = self.next_token()
        self.output.write(f"{space_indent_prev}</classVarDec>\n")

    def compile_subroutine(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<subroutineDec>\n")
        
        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        token = self.next_token()
        while token:
            if token[1] == "(":
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
                self.compile_params(indent + 1, token)
            elif token[1] == "{":
                self.compile_subroutine_body(indent + 1, token)
                break
            else:
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            token = self.next_token()

        self.output.write(f"{space_indent_prev}</subroutineDec>\n")

    def compile_params(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<parameterList>\n")

        space_indent = space_indent_prev + "  "
        token = self.next_token()
        while token:
            if token[1] == ")":
                break
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            token = self.next_token()
        
        self.output.write(f"{space_indent_prev}</parameterList>\n")
        self.output.write(f"{space_indent_prev}<{token[0]}> {token[1]} </{token[0]}>\n")

    def compile_subroutine_body(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<subroutineBody>\n")
        
        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        statement_added = False
        token = self.next_token()
        while token:
            if token [1] == "}":
                break
            elif token[1] == "var":
                self.compile_var_dec(indent + 1, token)
            else:
                if not statement_added:
                    self.output.write(f"{space_indent}<statements>\n")
                    statement_added = True
                if token[1] == "let":
                    self.compile_let(indent + 2, token)
                elif token[1] == "if":
                    self.compile_if(indent + 2, token)
                elif token[1] == "while":
                    self.compile_while(indent + 2, token)
                elif token[1] == "do":
                    self.compile_do(indent + 2, token)
                elif token[1] == "return":
                    self.compile_return(indent + 2, token)
            token = self.next_token()
        if statement_added:
            self.output.write(f"{space_indent}</statements>\n")
        
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")   
        self.output.write(f"{space_indent_prev}</subroutineBody>\n")

    def compile_var_dec(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<varDec>\n")
        
        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")

        token = self.next_token()
        while token:
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            if token[1] == ";":
                break
            token = self.next_token()
        self.output.write(f"{space_indent_prev}</varDec>\n")

    def compile_let(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<letStatement>\n")
        
        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        token = self.next_token()
        while token:
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            if token[1] == "[" or token[1] == "=":
                self.compile_expression(indent + 1, self.next_token())
            elif token[1] == ";":
                break
            token = self.next_token()
        self.output.write(f"{space_indent_prev}</letStatement>\n")
    
    def compile_if(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<ifStatement>\n")
        
        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        token = self.next_token()
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        self.compile_expression(indent + 1, self.next_token())
        token = self.next_token()
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        token = self.next_token()
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        self.output.write(f"{space_indent}<statements>\n")
        token = self.next_token()
        while token:
            if token[1] == "let":
                self.compile_let(indent + 2, token)
            elif token[1] == "if":
                self.compile_if(indent + 2, token)
            elif token[1] == "while":
                self.compile_while(indent + 2, token)
            elif token[1] == "do":
                self.compile_do(indent + 2, token)
            elif token[1] == "return":
                self.compile_return(indent + 2, token)
            elif token[1] == "}":
                self.output.write(f"{space_indent}</statements>\n")
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
                break
            token = self.next_token()
        if self.peek()[1] == "else":
            token = self.next_token()
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            token = self.next_token()
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            self.output.write(f"{space_indent}<statements>\n")
            token = self.next_token()
            while token:
                if token[1] == "let":
                    self.compile_let(indent + 2, token)
                elif token[1] == "if":
                    self.compile_if(indent + 2, token)
                elif token[1] == "while":
                    self.compile_while(indent + 2, token)
                elif token[1] == "do":
                    self.compile_do(indent + 2, token)
                elif token[1] == "return":
                    self.compile_return(indent + 2, token)
                elif token[1] == "}":
                    self.output.write(f"{space_indent}</statements>\n")
                    self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
                    break
                token = self.next_token()
        self.output.write(f"{space_indent_prev}</ifStatement>\n")

    def compile_while(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<whileStatement>\n")
        
        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        token = self.next_token()
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        self.compile_expression(indent + 1, self.next_token())
        token = self.next_token()
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        token = self.next_token()
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        self.output.write(f"{space_indent}<statements>\n")
        token = self.next_token()
        while token:
            if token[1] == "let":
                self.compile_let(indent + 2, token)
            elif token[1] == "if":
                self.compile_if(indent + 2, token)
            elif token[1] == "while":
                self.compile_while(indent + 2, token)
            elif token[1] == "do":
                self.compile_do(indent + 2, token)
            elif token[1] == "return":
                self.compile_return(indent + 2, token)
            elif token[1] == "}":
                self.output.write(f"{space_indent}</statements>\n")
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
                break
            token = self.next_token()
        self.output.write(f"{space_indent_prev}</whileStatement>\n")
        
    def compile_do(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<doStatement>\n")
        
        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")

        self.compile_subroutine_call(indent + 1, self.next_token())
        token = self.next_token()
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")

        self.output.write(f"{space_indent_prev}</doStatement>\n")

    def compile_return(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<returnStatement>\n")
        
        space_indent = space_indent_prev + "  "
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        
        token = self.next_token()
        while token:
            if token[1] == ";":
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
                break
            else:
                self.compile_expression(indent + 1, token)
            token = self.next_token()
        
        self.output.write(f"{space_indent_prev}</returnStatement>\n")

    def compile_subroutine_call(self, indent, token):
        space_indent = "  " * indent
        self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        token = self.peek()
        while token:
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            self.next_token()
            if token[1] == ")":
                return
            if token[1] == "(":
                self.compile_expression_list(indent, token)
            token = self.peek()

    def compile_expression_list(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<expressionList>\n")
        
        space_indent = space_indent_prev + "  "
        token = self.peek()
        while token:
            if token[1] == ")":
                break
            self.next_token()
            if token[1] == ",":
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            else:
                self.compile_expression(indent + 1, token)
            token = self.peek()
        self.output.write(f"{space_indent_prev}</expressionList>\n")


    def compile_expression(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<expression>\n")
        
        space_indent = space_indent_prev + "  "
        while True:
            self.compile_term(indent + 1, token)
            if self.peek()[1] not in map(lambda char: CodeParser.SYMBOLS[char], "+-*/&|<>="):
                break
            token = self.next_token()
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            token = self.next_token()

        self.output.write(f"{space_indent_prev}</expression>\n")

    def compile_term(self, indent, token):
        space_indent_prev = "  " * indent
        self.output.write(f"{space_indent_prev}<term>\n")

        space_indent = space_indent_prev + "  "
        if token[0] in ["integerConstant", "stringConstant", "keyword"]:
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        elif token[0] in ["identifier"]:
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            if self.peek()[1] == "[":
                token = self.next_token()
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
                self.compile_expression(indent + 1, self.next_token())
                token = self.next_token()
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            elif self.peek()[1] == ".":
                token = self.next_token()
                self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
                self.compile_subroutine_call(indent + 1, self.next_token())
        elif token[1] == "(":
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            self.compile_expression(indent + 1, self.next_token())
            token = self.next_token()
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
        elif token[1] == "-" or token[1] == "~":
            self.output.write(f"{space_indent}<{token[0]}> {token[1]} </{token[0]}>\n")
            self.compile_term(indent + 1, self.next_token())        
        self.output.write(f"{space_indent_prev}</term>\n")
