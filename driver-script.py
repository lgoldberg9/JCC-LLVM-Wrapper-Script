import sys

class jcc:
    """
    A class used to assist with gcc to llvm driver script.
    """
    
    def __init__(self, args):
        """
        Constructor for the class.
        
        Fields
        
        self.filename -- name of file to be converted to bytecode.
        self.compfiles -- array of files to be compiled with or linked together.
        self.prior_flags -- array of flags that precede the filename.
        self.after_flags -- array of flags that succeed the files in compfiles.
        """
        self.filename = ""
        self.compfiles = []
        self.prior_flags = []
        self.after_flags = []
        
        self.setup_args(args)
        
    def setup_args(self, args):
        """
        Method used to parse inputs of the command line into their respective arrays.
        
        Arguments:
        args -- array of arguments to parse.
        
        Preconditions: args must be nonempty.
        Postconditions: filename, compfiles, and prior_flags are nonempty.
        """
        enumed_args = list(map(lambda x: [x, args.index(x)], args))
        flagged_args = list(filter(lambda x: x[:][0][0] == '-', enumed_args))
        
        while (flagged_args[0][0] != '-o'):
            self.prior_flags.append(flagged_args.pop(0)[0])
        
        flag = flagged_args.pop(0) # Pop array containing '-o'
        self.prior_flags.append(flag[0])
        lower_index_bound = flag[1] + 1 # Lower_index_bound represents the filename, not '-o'
        
        if flagged_args == []: # Check if there are any flags after '-o'.
            upper_index_bound = len(args) # If there are no flags after '-o', upper bound is end of command line.
        else:
            flag = flagged_args.pop(0) # Pop off next flag after files.
            self.after_flags.append(flag[0])
            upper_index_bound = flag[1] # Otherwise, upper bound is first flag after c files.

        self.after_flags.extend(list(map(lambda x: x[0], flagged_args)))
        
        self.filename = args[lower_index_bound]
        
        # Gather all args between filename and the next flag (if there is a flag).
        self.compfiles = list(filter(lambda x: lower_index_bound < x[:][1] and x[:][1] < upper_index_bound, enumed_args))
        self.compfiles = list(map(lambda x: x[0], self.compfiles))   
        
    def compile_component(self):
        pass
        
    def link_structures(self):
        pass
    
    def print_fields(self):
        print self.filename
        print self.compfiles
        print self.prior_flags
        print self.after_flags
        
        

driver = jcc(sys.argv)
driver.print_fields()
