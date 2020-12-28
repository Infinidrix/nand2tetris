import sys
from Translator import Translator

def main():
    file_name = "".join(sys.argv[1].split(".")[:-1])
    ext = ".asm"
    with open(file_name + ext, "w") as write_file:
        with open(sys.argv[1], encoding="UTF-8") as read_file:
            translator = Translator(file_name.split("\\")[-1].split("/")[-1])
            for line in read_file:
                print(f'Line {line}') 
                value = translator.interpret(line[:-1])
                print(value)
                write_file.write(value)
            write_file.write(translator.finish())


if __name__ == "__main__":
    main()