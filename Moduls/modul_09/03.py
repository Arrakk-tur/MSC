# def simple_gen():
#     yield "First"
#     yield "Second"


# gen = simple_gen()
# print(gen)
# print(type(gen))

# print(next(gen))
# print(next(gen))

# sq = (i**2 for i in range(10))
# print(sq)

def read_file(filename: str):
    """
    Opens a file and reads it line by line using standart way.

    Args:
        filename (str): The name of the file to be opened.

    Returns:
        list: A list containing the lines from the file.

    """
    text = open(filename, 'r')
    lines = text.readlines()
    text.close()
    return lines


def read_file_gen(filename: str):
    """
    Opens a file and reads it line by line using Generator. 

    Args:
        filename (str): The name of the file to be opened.

    Yields:
        str: A line from the file.

    """
    text = open(filename, 'r')
    while True:
        line = text.readline()
        if not line:
            text.close()
        yield line
