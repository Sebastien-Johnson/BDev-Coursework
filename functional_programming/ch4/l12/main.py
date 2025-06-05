def list_files(parent_directory, current_filepath=""):
    file_paths = list()

    for child in parent_directory:
        if parent_directory[child] is None:
            file_paths.append(current_filepath + "/" + child)
        else:        
            file_paths.extend(list_files(parent_directory[child], current_filepath + "/" + child))

    return file_paths