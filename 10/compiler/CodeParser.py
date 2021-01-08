
from io import TextIOBase


class CodeParser:

    KEYWORDS = {
        "class", "constructor", "function", "method", "field",
        "static", "var", "int", "char", "boolean", "void", "true",
        "false", "null", "this", "let", "do", "if", "else",
        "while", "return"
    }
    SYMBOLS = {i: i for i in "{}()[].,;+-*/&|<>=-"}
    SYMBOLS[">"] = "&gt;"
    SYMBOLS["<"] = "&lt;"
    SYMBOLS["&"] = "&amp;"

    @staticmethod
    def next_token(input: TextIOBase):
        def choose_type(curr_type, curr_token):
            if curr_type == "integerConstant":
                return curr_type, curr_token
            else:
                return "identifier", curr_token

        curr_token = "" # comment, integerConstant, stringConstant, keyword
        curr_type = ""
        while value := input.read(1):
            if value == "*":
                print("HI")
            # If we're building a String constant
            if curr_type == "stringConstant" and value != '"':
                curr_token += value
                continue
            elif curr_type == 'block comment':
                if value == '*':
                    value = input.read(1)
                    if value == '/':
                        curr_type = ""
                continue
                
            # If prev concat made a keyword
            if curr_token in CodeParser.KEYWORDS:
                yield curr_type, curr_token
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
                input.readline()
            elif value == "*": 
                if curr_type == 'symbol':
                    curr_token = ""
                    curr_type = "block comment"
                else:
                    if curr_token:
                        yield choose_type(curr_type, curr_token)
                    yield 'symbol', value

            # check if / appeared in anticipation of comment
            # checks for whether there is a comment are above
            elif curr_token in CodeParser.SYMBOLS:
                yield curr_type, CodeParser.SYMBOLS[curr_token]
                curr_token = ""
                curr_type = "" 
            # if / saves it to look ahead for comments
            elif value == "/":
                if curr_token: yield choose_type(curr_type, curr_token)
                curr_type = "symbol"
                curr_token = "/"
            # in case of whitespace return the token found so far
            elif value == " " and curr_token:
                yield choose_type(curr_type, curr_token)
                curr_token = ""
                curr_type = ""
            # checks if encoutered a symbol
            elif value in CodeParser.SYMBOLS:
                if curr_token:
                    yield choose_type(curr_type, curr_token)
                curr_token = ""
                curr_type = ""
                yield 'symbol', CodeParser.SYMBOLS[value]
            
            # check whether to terminate or start a StringConstant
            elif value == '"':
                if curr_type == "stringConstant":
                    yield curr_type, curr_token
                    curr_token = ""
                    curr_type = ""
                else:
                    if curr_token: yield curr_type, curr_token
                    curr_token = ""
                    curr_type = "stringConstant"
            elif (value.isalpha() or value == "_"): 
                if not curr_token:
                    curr_type = "keyword"
                    curr_token = value
                else:
                    curr_token += value


    @staticmethod
    def parse_file(input, output):
        output.write("<tokens>\n")
        for token in CodeParser.next_token(input):
            # determine what to do based on the token
            output.write(f"<{token[0]}> {token[1]} </{token[0]}>\n")
        output.write("</tokens>\n")
            
