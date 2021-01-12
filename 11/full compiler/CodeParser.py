
from io import TextIOBase
from CodeWriter import CodeWriter

class CodeParser:

    KEYWORDS = {
        "class", "constructor", "function", "method", "field",
        "static", "var", "int", "char", "boolean", "void", "true",
        "false", "null", "this", "let", "do", "if", "else",
        "while", "return"
    }
    SYMBOLS = set("{}()[].,;+-*/&|<>=-~")

    def __init__(self, input: TextIOBase, output: TextIOBase):
        self.input = input
        self.output = output
        self.tokens = []
        self.location = 0
        self.writer = CodeWriter(output)
        self.generate_tokens()
        self.parse_file()

    def next_token(self):
        if self.location >= len(self.tokens):
            return
        self.location += 1
        if self.tokens[self.location - 1][1] == "Keyboard":
            hi = 0
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
                self.tokens.append((curr_type, curr_token))
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
                self.tokens.append(('symbol', value))
            
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
            if token[1] == "class":
                self.compile_class(token)
            token = self.next_token()
    
    def compile_class(self, token):
        token = self.next_token()
        self.writer.class_dec(token[1])
        while token:
            if token[1] == "static" or token[1] == "field":
                self.compile_class_var_dec(token)
            elif token[1] in ["constructor", "function", "method"]:
                self.compile_subroutine(token)
            elif token[1] == "}":
                break
            token = self.next_token()

    def compile_class_var_dec(self, token):
        var_scope = token[1]
        token = self.next_token()
        var_type = token[1]
        token = self.next_token()
        while token:
            if token[1] == ";":
                break
            elif token[0] != "symbol":
                self.writer.class_var_dec([token[1], var_type, var_scope])
            token = self.next_token()

    def compile_subroutine(self, token):
        subroutine_type = token[1]
        token = self.next_token()
        while token:
            if token[1] == "(":
                self.compile_params(token)
            elif token[1] == "{":
                self.compile_subroutine_body(token)
                break
            if self.peek()[1] == "(":
                self.writer.subroutine_dec(token[1], subroutine_type)
            token = self.next_token()

    def compile_params(self, token):
        token = self.next_token()
        is_type = True
        var_type = None
        while token:
            if token[1] == ")":
                break
            elif is_type:
                var_type = token[1]
                is_type = False
            elif token[1] == ",":
                is_type = True
            else:
                self.writer.params_list([token[1], var_type])
            token = self.next_token()
        
    def compile_subroutine_body(self,token):
        self.compile_body(self.next_token(), True)

    def compile_body(self, token, is_func = False):
        
        while token:
            if token[1] == "}":
                break
            elif token[1] == "var":
                self.compile_var_dec(token)
            elif is_func:
                self.writer.subroutine_body() # TODO: do this function
                is_func = False
                continue
            elif token[1] == "let":
                self.compile_let(token)
            elif token[1] == "if":
                self.compile_if(token)
            elif token[1] == "while":
                self.compile_while(token)
            elif token[1] == "do":
                self.compile_do(token)
            elif token[1] == "return":
                self.compile_return(token)
            token = self.next_token()

    def compile_var_dec(self,token):
        token = self.next_token()
        var_type = token[1]
        while token:
            if token[1] == ";":
                break
            elif token[1] not in [var_type, ","]:
                self.writer.subroutine_var_dec([token[1], var_type, "local"])
            token = self.next_token()

    def compile_let(self,token):
        is_array = False
        token = self.next_token()
        var_name = token[1]
        while token:
            if token[1] == "[":
                self.compile_expression(self.next_token())
                is_array = True
            if token[1] == "=":
                self.compile_expression(self.next_token())
            elif token[1] == ";":
                break
            token = self.next_token()
        self.writer.let_statement(var_name, is_array) 
    
    def compile_if(self,token):
        self.compile_expression(self.next_token())
        self.writer.if_start()
        self.compile_body(self.next_token())
        if self.peek()[1] == "else":
            self.writer.else_start()
            self.next_token()
            self.next_token()
            self.compile_body(self.next_token())
        self.writer.if_end()

    def compile_while(self,token):
        self.writer.while_begin()
        self.compile_expression(self.next_token())
        self.writer.while_start()
        self.compile_body(self.next_token())
        self.writer.while_end()

    def compile_do(self,token):
        self.compile_subroutine_call(self.next_token())
        self.writer.do_statement()
        self.next_token()

    def compile_return(self,token):
        token = self.next_token()
        has_expression = False
        while token:
            if token[1] == ";":
                break
            else:
                has_expression = True
                self.compile_expression(token)
            token = self.next_token()
        self.writer.return_statement(has_expression)

    def compile_subroutine_call(self,token, class_name = None, subroutine_name = None):
        while token:
            if token[1] == ")":
                break
            if token[1] == "(":
                self.writer.subroutine_call_start(class_name)
                self.compile_expression_list(token)
            if self.peek()[1] == ".":
                class_name = token[1]
            elif self.peek()[1] == "(":
                subroutine_name = token[1]
            
            token = self.next_token()
        self.writer.subroutine_call_end(class_name, subroutine_name)

    def compile_expression_list(self,token):
        arg_count = 0
        token = self.peek()
        while token:
            if token[1] == ")":
                break
            self.next_token()
            if token[1] == ",":
                pass
            else:
                self.compile_expression(token)
                arg_count += 1
            token = self.peek()
        self.writer.add_args(arg_count)

    def compile_expression(self,token):
        op = None
        while True:
            self.compile_term(token)
            if op:
                self.writer.push_op(op)
            if self.peek()[1] not in "+-*/&|<>=":
                break
            op = self.next_token()[1]
            token = self.next_token()

    def compile_term(self,token):
        if token[0] == "integerConstant":
            self.writer.push_int(token[1])
        elif token[0] == "stringConstant":
            self.writer.push_string(token[1])
        elif token[0] == "keyword":
            self.writer.push_keyword(token[1])
        elif token[0] == "identifier":
            var_name = token[1]
            if self.peek()[1] == "[":
                token = self.next_token()
                self.compile_expression(self.next_token())
                token = self.next_token()
                self.writer.array_reference(var_name)
            elif self.peek()[1] == ".":
                token = self.next_token()
                self.compile_subroutine_call(self.next_token(), var_name)
            else:
                self.writer.push_var(var_name)
        elif token[1] == "(":
            self.compile_expression(self.next_token())
            token = self.next_token()
        elif token[1] == "-" or token[1] == "~":
            self.compile_term(self.next_token()) 
            self.writer.push_unary_op(token[1])       
