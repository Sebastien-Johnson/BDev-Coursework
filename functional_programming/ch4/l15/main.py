def count_nested_levels(nested_documents, target_document_id, level=1):

    for doc in nested_documents: 
    #loops through dicts
        if doc == target_document_id:
        #returns if id found
            return level
        elif isinstance(nested_documents[doc], dict):
        #checks if 'doc' is a dict
            next_doc = count_nested_levels(nested_documents[doc], target_document_id, level+1)
            #turns reursive call into object
            if next_doc != -1:
            #returns result of call if id is found/ not -1
                return next_doc
    
    return -1
    #id not found