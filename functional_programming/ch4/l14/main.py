def find_longest_word(document, longest_word=""):
    split_doc = document.split(" ", 1)
    
    if len(split_doc) == 1:
        if len(split_doc[0]) > len(longest_word):
            return split_doc[0]
        else:
            return longest_word
    
    if len(split_doc[0]) > len(longest_word):
        longest_word = split_doc[0]

    return find_longest_word(split_doc[1], longest_word)


'''
split_doc = document.split(" ", 1)
    
    if len(split_doc) == 1:
        if len(split_doc[0]) > len(longest_word):
            return split_doc[0]
        else:
            return longest_word
    
    if len(split_doc[0]) > len(longest_word):
        longest_word = split_doc[0]

    return find_longest_word(split_doc[1], longest_word)
'''
    
