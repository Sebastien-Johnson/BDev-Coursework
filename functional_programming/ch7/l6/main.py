def new_resizer(max_width, max_height):
    
    def min_dimensions(min_width=0, min_height=0):
        if min_height > max_height or min_width > max_width:
            raise Exception("minimum size cannot exceed maximum size")
        
        def set_params(width, height):
            width = max(width, min_width)
            width = min(width, max_width)
            height = max(height, min_height)
            height = min(height, max_height)
            return width, height
        return set_params
    return min_dimensions