import pandas as pd

def full_output(file_path, count):
    """
    Create a pandas DataFrame containing file names and their character counts.

    This function takes a list of file paths, reads each file, counts the number of characters,
    and then creates a pandas DataFrame with this information.

    Parameters:
    file_path (str): The path to the text file that needs to be read.
    count (int): The total number of characters in the text.

    Returns:
    pandas.DataFrame: A DataFrame with two columns: 'File Name' and 'Character Count'.
    """
    data = []

    file_name = file_path.split('/')[-1]
    data.append([file_name, count])

    return pd.DataFrame(data, columns=['File Name', 'Character Count'])