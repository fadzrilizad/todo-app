FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """
    Read the text file and return
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """
    Write a to-do items list
    in the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_local)

