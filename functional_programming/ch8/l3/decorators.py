def configure_plugin_decorator(func):
    
    def wrapper(*args):
        arg_dict = dict(args)


        return func(**arg_dict)
        #** unpacks each key:value into its own item
    return wrapper