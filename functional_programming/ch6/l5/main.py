def css_styles(initial_styles):
    new_styles = initial_styles.copy()

    def add_style(selector, property, value):
        if selector not in new_styles:
            new_styles[selector] = {}
            new_styles[selector][property] = value
        else:
            new_styles[selector][property] = value

        return new_styles
    
    return add_style