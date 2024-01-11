def read_file(file_path):
    """
    Read the contents of a text file and return it as a string.

    This function opens a text file in read mode, reads its content, and then returns the content as a string.
    It's designed to handle text files, so it's not suitable for binary files.

    Parameters:
    file_path (str): The path to the text file that needs to be read.

    Returns:
    str: The content of the text file as a string.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def count_characters(file_path):
    """
    Count the number of characters in a given text.

    This function takes a string as input and returns the total number of characters in it.
    Characters include letters, numbers, spaces, and punctuation marks.

    Parameters:
    file_path (str): The path to the text file that needs to be read.

    Returns:
    int: The total number of characters in the text.
    """
    text = read_file(file_path)
    return len(text)
