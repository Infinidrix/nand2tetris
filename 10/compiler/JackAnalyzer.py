import sys
import os
from CodeParser import CodeParser

def main(args):
    filenames = []
    if len(args) < 2:
        args = ["", "C:\\Users\\Biruk Solomon\\Desktop\\IT stuff\\Class\\Interests\\nand2tetris\\projects\\09\\Pac-Man"]
    path = os.path.abspath(args[1])
    if os.path.isdir(path):
        additional = parse_dir(path)
        filenames.extend(additional)
    else:
        filenames.append(path)

    for filename in filenames:
        output_filename = filename[:-5] + "_test.xml"
        with open(os.path.join(path,filename)) as input_file, open(os.path.join(path, output_filename), 'w') as output_file:
            CodeParser(input_file, output_file)
            

def parse_dir(dir_path):
    '''
    returns a list of all .jack filenames
    immediately under the given dir_path
    '''
    filenames = []
    for entry in os.listdir(dir_path):
        entry = os.path.join(dir_path, entry)
        print(entry)
        if os.path.isfile(entry) and entry.endswith('.jack'):
            filenames.append(entry)
    return filenames
if __name__ == "__main__":
    main(sys.argv)