import sys

class jcc:
    
    def __init__(self, args):
        flagged_args = list(filter(lambda x: x[:][0] == '-', args))
        flagged_indexed_args = list(map(lambda y: [y, args.index(y)], flagged_args)) 
        
        prev_args = []
        i = 0
        
        while (flagged_indexed_args[i][0] != '-o' and i < len(flagged_indexed_args)):
            prev_args.append(flagged_indexed_args[i])
            i += 1     
         
        lower_index_of_files = flagged_indexed_args[i][1] # Index will be at 'filename'
        
        i += 1 # Increment because we don't need '-o' anymore and want the 'filename'
        
        if lower_index_of_files == len(flagged_indexed_args): # If there are no flags after '-o'
            upper_index_of_files = len(args)
        else: 
            upper_index_of_files = flagged_indexed_args[i][1] # Flags after '-o'
        
        self.filename = args[i] # Since we've incremented, 
        self.compilation_files = []
        
        for j in range(lower_index_of_files, upper_index_of_files): # Start at +1 since we do not need '-o'
            self.compilation_files.append(args[j])
        
        print self.filename, self.compilation_files
       
        
    def compile_component(self):
        pass
        
    def link_structures(self):
        pass
        
        

driver = jcc(sys.argv)
