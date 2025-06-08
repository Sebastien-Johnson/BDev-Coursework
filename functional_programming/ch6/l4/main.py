def new_collection(initial_docs):
    new_docs = initial_docs.copy()

    def updated_collection(new_line):  
        new_docs.append(new_line)
        return new_docs
    #this stays stateful by returning an updated copy instead
    #of mutating the input or using 'nonlocal'
    
    return updated_collection