import os
import argparse

class jcc:
    """
    A class used to assist with gcc to llvm driver script.
    """
    
    def __init__(self):
        """
        Constructor for the class.
        
        Fields
        args -- Namespace of flags and their respective arguments, parsed by setup_args.
        
        """
        self.args = None
        
        self.setup_args()
        
    def setup_args(self):
        """
        Method used to parse inputs of the command line into their respective arrays.
        
        Arguments:
        [No additional]
        
        Preconditions: [No additional]
        Postconditions: self.args is nonempty and has a '-o' option.
        """
        
        parser = argparse.ArgumentParser(description="GCC to LLVM Driver Script")

        # Driver control arguments
        parser.add_argument('-v', action='store_true')

        # Compiler pass-through arguments
        parser.add_argument('-c', action='store_true')
        parser.add_argument('-o')
        parser.add_argument('-O', type=int, default=2)
        parser.add_argument('-g', action='store_true')
        parser.add_argument('-ansi', action='store_true')
        parser.add_argument('-W', action='append', default=[])
        parser.add_argument('-f', action='append', default=[])
        parser.add_argument('-D', action='append', default=[])
        parser.add_argument('-L', action='append', default=[])
        parser.add_argument('-I', action='append', default=[])
        parser.add_argument('-l', action='append', default=[])
        parser.add_argument('input', nargs='+')

        # Do the parse
        self.args = parser.parse_args()   
        
    def arg(self, flag, values):
        """
        Method used to parse specific flags and prepare them for insertion into the command line.
        
        Arguments:
        flag -- specific gcc flag to be parsed.
        values -- successive gcc flag options that accompanied 'flag'.
        
        Preconditions: flag must be a gcc flag.
        Postconditions: returns a correctly formatted string containing the flag and any successive values.
        Credit: Modified from Charlie Curtsinger's stabalizer driver script.
        """
        if not isinstance(values, list):
            values = [values]

        cmd = ''
        for v in values:
            if v == True:
                cmd += ' -'+flag
            elif v == False:
                pass
            else:
                cmd += ' -'+flag+v
        return cmd

    def compile_component(self, input_c):
        """
        Method used to setup command line output for clang compilation.
        
        Arguments:
        input_c -- a .c file.
        
        Preconditions: input_c contains no errors.
        Postconditions: initiates a compilation command using clang with all flags
            except linking flags included and then return the name of the compiled file.
        Credit: Modified from Charlie Curtsinger's stabalizer driver script.
        """
        if input_c.endswith('.o'):
            return input_c
    
        cmd = 'clang -O0 -c -emit-llvm'
        obj_file = self.arg('o ', input_c.replace('.c', '.o'))
        cmd += self.arg('o ', input_c.replace('.c', '.o'))

        cmd += self.arg('O', 0)
        cmd += self.arg('g', self.args.g)
        cmd += self.arg('I', self.args.I)
        cmd += self.arg('f', self.args.f)
        cmd += self.arg('D', self.args.D)

        cmd += ' ' + input_c
        #cmd += self.arg('l', self.args.l)
        #cmd += self.arg('L', self.args.L)

        if self.args.v:
            print cmd
        #os.system(cmd)

        return obj_file.replace(' -o ', '')
        
    def link_structures(self, inputs):
        """
        Method used to link object files.
        
        Arguments:
        inputs -- an array of '.o' files.
        
        Preconditions: inputs must be nonempty
        Postconditions: links together '.o' files and then returns location of corresponding 
            bytecode file for llvm processing.
        Credit: Modified from Charlie Curtsinger's stabalizer driver script.
        """
        cmd = 'llvm-link -o ' + self.args.o + '.bc '

        cmd += ' '.join(inputs)

        if self.args.v:
            print cmd
        #os.system(cmd)
        return self.args.o + '.bc'
        
def main():
    driver = jcc()
    driver.args.v = True
    
    object_files = map(driver.compile_component, driver.args.input)
            
    if not driver.args.c:
        linked = driver.link_structures(object_files)

    
main()