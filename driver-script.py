import sys

class jcc:
    """
    
    """
    
    def __init__(self, args):
        self.filename = ""
        self.compfiles = []
        
        
        
    def setup_args(self):
        enumed_args = list(map(lambda x: [x, args.index(x)], args))
        flagged_args = list(filter(lambda x: x[:][0][0] == '-', enumed_args))
        
        while (flagged_args[0][0] != '-o'):
            flagged_args.pop(0)
        
        lower_index_bound = flagged_args.pop(0)[1] + 1 # Lower_index_bound represents the filename, not '-o'
        
        if flagged_args == []: # Check if there are any flags after '-o'.
            upper_index_bound = len(args) # If there are no flags after '-o', upper bound is end of command line.
        else:
            upper_index_bound = flagged_args.pop(0)[1] # Otherwise, upper bound is first flag after c files.
        
        self.filename = args[lower_index_bound]
        
        # Gather all args between filename and the next flag (if there is a flag).
        self.compfiles = list(filter(lambda x: lower_index_bound < x[:][1] and x[:][1] < upper_index_bound, enumed_args))
        self.compfiles = list(map(lambda x: x[0], self.compfiles))   
        
    def compile_component(self):
        pass
        
    def link_structures(self):
        pass
        
        

driver = jcc(sys.argv)
