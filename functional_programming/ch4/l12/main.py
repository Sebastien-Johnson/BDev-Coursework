def list_files(parent_directory, current_filepath=""):
    file_paths = list()

    for p_dict in parent_directory:
        current_filepath += f"/{parent_directory[p_dict]}"

        if p_dict == None:
            file_paths.append(current_filepath)
        else:
            return file_paths.extend(list_files(p_dict, current_filepath))