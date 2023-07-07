from ensure import ensure_annotations



def output_file(file_name:str) -> str:
    output_file= ""
    splitted_file_name = file_name.split(".")

    if "." in file_name and splitted_file_name[-1] != "docx" : 
        output_file = splitted_file_name[0] + ".docx"

    elif "." not in file_name:
        output_file = file_name + ".docx"
    return output_file


