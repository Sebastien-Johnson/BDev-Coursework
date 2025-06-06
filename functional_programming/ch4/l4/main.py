def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    
    zipped = {keys[0] : values[0]} #logged first index of current inputs
    return {**zipped, **zipmap(keys[1:], values[1:])} #merge current dict with recalled, updated function
