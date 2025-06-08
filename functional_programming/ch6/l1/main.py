def word_count_aggregator():
    count = 0

    def word_counter(doc):
        nonlocal count
        split_doc = doc.split()

        for word in split_doc:
            count += 1

        return count
    
    return word_counter