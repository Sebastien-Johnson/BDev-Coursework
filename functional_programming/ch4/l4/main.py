def zipmap(keys, values):
    if keys == None or values == None:
        return {}
    
    zipped = zipmap(keys[+1], values[+1])