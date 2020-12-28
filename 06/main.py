import sys
from assembler import Assembler
def assemble(filename: str) -> None:
    # read file contents line by line
    try:
        file = open(filename, encoding="UTF-8")
        assembler = Assembler()
        for line in file:
            assembler.add_line(line)

        new_filename = filename[0:-3] + "hack"
        new_file = open(new_filename, 'w')
        new_file.writelines(assembler.build())
    except OSError:
        print("OSError: " + err)
    finally:
        file.close()
        new_file.close()

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        print(filename)
        assemble(filename)
