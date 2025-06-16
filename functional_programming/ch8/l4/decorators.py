def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        fn = lambda item: (item[0], convert_md_to_txt(item[1]))
        #converts kwarg item value into tuple, leaves key unchanged
        return func(
            *list(map(convert_md_to_txt, args)),
            **dict(map(fn, kwargs.items()))
        )
        #returns function with new mapped list and idct
    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
