
#-------------------------------------------Date Feature---------------------------------------------------
# import time - There is no date() function available in the global space
# import time is located in python directory written by developers and has functions
# strftime - means string from time
# %b - Month , %d - day , %Y - Year , %H - hour , %M - Minutes
# Doc String - Triple quotes

import time
from modules import functions

date_time = time.strftime("%d %b %Y %H:%M:%S")  # Can google different formats-> date formats
print(f"Today's date {date_time}")

while True:
#
        user_action = input("Type add, show, edit, delete,exit:")
        user_action = user_action.strip()
        if user_action.startswith("add"):
            todo = user_action[4:]
            todos = functions.get_todos()  # read = default argument : todos.txt  but it's declared as default parameter
            todos.append(todo + "\n")

            functions.write_todos(todos) # don't have to declare todos.txt as its default parameter

        elif user_action.startswith("show"):
             todos = functions.get_todos()

             for i , k in enumerate(todos):
                 k = k.strip("\n")
                 print(f"{i + 1}-{k}")

        elif user_action.startswith("edit"):
            try:
                number = int(user_action[5:])
                number = number -1
                todos = functions.get_todos()
                new_todo = input("Enter new todo: ")
                todos[number] = new_todo + "\n"

                functions.write_todos(todos)
            except ValueError:
                print("Your command is not valid")

                continue
        elif user_action.startswith("delete"):
            try:
                number = int(user_action[7:])

                todos = functions.get_todos()
                index = number -1
                todo_removed = todos[index].strip("\n")
                todos.pop(index)
                functions.write_todos(todos)
                message = f"Todo {todo_removed} was removed from the list"
                print(message)
            except IndexError:
                print("There is no item with that number")
                continue
        elif user_action.startswith("exit"):
                break
        else:
             print("You have entered wrong command")

print("Bye")


