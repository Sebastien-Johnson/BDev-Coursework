def lines_with_sequence(char):
    

    def with_char(length):
        sequence = char * length
        
        def with_length(doc):
            count = 0
            new_doc = doc.split()

            for line in new_doc:
                if sequence in line:
                    count += 1

            return count
        return with_length
    return with_char
