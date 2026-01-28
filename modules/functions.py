#-------------------------------------Using a function------------------------------------------------
FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):            # todos.txt - default parameter
    """
    Read a text file and return the list of to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath =FILEPATH):  # todos_arg not parameter and must start with it
    """
        Write a text file and return the list of to-do items.
        """
    with open(filepath, "w") as file_write:
        file_write.writelines(todos_arg)

