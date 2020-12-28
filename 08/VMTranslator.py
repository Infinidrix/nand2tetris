from Translator import Translator
import sys
import os
from Translator import Translator

def main(args):
    filenames = []
    is_sys_present = False
    path = os.path.abspath(args[1])
    if os.path.isdir(path):
        additional, is_sys_present = parse_dir(path)
        filenames.extend(additional)
        output = os.path.join(path, f"{os.path.basename(path)}.asm")
    else:
        filenames.append(path)
        output = path[:-3] + ".asm"
        if os.path.basename(path) == 'Sys.vm':
            is_sys_present = True

    translator = Translator("")
    with open(output, 'w') as output_file:
        if is_sys_present:
            output_file.write(translator.bootstrap())
        for filename in filenames:
            translator.filename = os.path.basename(filename[:-3])
            with open(os.path.join(path,filename)) as input_file:
                for line in input_file:
                    translated = translator.interpret(line[:-1])
                    output_file.write(translated)
        output_file.write(translator.finish())

def parse_dir(dir_path):
    '''
    returns a list of all .vm filenames
    immediately under the given dir_path
    '''
    filenames = []
    is_sys_present = False
    for entry in os.listdir(dir_path):
        entry = os.path.join(dir_path, entry)
        print(entry)
        if os.path.isfile(entry) and entry.endswith('.vm'):
            filenames.append(entry)
            if os.path.basename(entry) == 'Sys.vm':
                is_sys_present = True
    return filenames, is_sys_present
if __name__ == "__main__":
    main(sys.argv)