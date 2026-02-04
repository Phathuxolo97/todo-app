import FreeSimpleGUI as sg
from modules import functions

# google - pypi.org - 3rd part library /Modules . Instances of those buttons, textbox , windows
# pip install FreeSimpleGUI Create window , button
# layout is argument and be list and must connect the instances (Label ,InputText)
# Window is type and its instance ("My To-DO App")
# Read - Method display the window on the screen.

# read() - is a method that return value when click on add button
# values = window.read() - ("Add" , { 0 , "test1"}) = Tuple
# On textbox add key = todo -> ("Add" , { todo , "test1"}) = Tuple
# event , values = window.read() - event = Add ->label , values = { todo , "test1"} -> dictionary

# While loop keeps the window running as will always true
# new_todo = values["todo"] -> value of the key

# When click on the button after insert text : "Add" {todo:Test1} -> event , values (key & value)
# When click on the item in the Listbox : {'todo': '', 'todos_key': ['Test3\n']} so event , (key & values)

# On edit press button
# event = Edit
# values dictionary = {"todo" : "example" , "todos_key" : ["Test4\n"]}  - example new value & todos_key old value
# Values list - values["todos_key"] = ["Test4\n"]
# values["todos_key"][0] = Test4
# window["todos_key"].update(values=todos) #Refresh the screen in real time because old value remains until window close
# window is like the mother of instances (label , listbox , buttons etc) so we want the listbox
# update is method of the listbox so update values of the list

#Instances
label1 = sg.Text("Enter todo: ")
input_text = sg.InputText(tooltip="textbox" , key="todo") # add = key

list_box = sg.Listbox(values=functions.get_todos() , key="todos_key",
                      enable_events= True , size=[45,10])  # ListBox -> list ,keys ,enable_events and size


button1 = sg.Button("Add")
button2 = sg.Button("Edit")
button3 = sg.Button("Delete")
button4 = sg.Button("Exit")

window = sg.Window("My Todo App" ,
                   layout=[[label1 , input_text , button1] , [list_box , button2 , button3], [button4]] ,
                   font=("Helvetica", 10))

while True:   # Make the window not to close
    event ,values = window.read() # InpuText -> tuple read the value on the input text ("Add",{todo:"Test1"})
    print(event) # event -> Action return label "Add"
    print(values) # dictionary(key & value) ->{todo:Test1}

    match event :
        case "Add":
          todos = functions.get_todos()  # Will return list of todos
          new_todo = values["todo"] + "\n"  # Get value of the key todo same 0
          todos.append(new_todo)
          functions.write_todos(todos)
          window["todos_key"].update(values=todos) #Add todo to be added to screen in real time
        case "Edit":
          todo_edit = values["todos_key"][0]  # value from the list = {"todo" :"example","todos_key":["Test4\n"]}
          new_todo = values["todo"]   # value from the user = {"todo" : "example" , "todos_key" : ["Test4\n"]}

          todos = functions.get_todos()
          index = todos.index(todo_edit) # Replace old todo with new todo in list use an index
          todos[index] = new_todo # That index value replace with new value
          functions.write_todos(todos)
          window["todos_key"].update(values=todos) #Refresh the screen in real time
        case "Delete":

          todo_delete = values["todos_key"][0]
          todos = functions.get_todos()
          todos.remove(todo_delete)
          functions.write_todos(todos)
          window["todos_key"].update(values=todos)
          window["todo"].update(value=" ")# still on the delete on input box so use this statement
        case "todos_key":  # Event todo_key
          window["todo"].update(value=values["todos_key"][0]) # We want to show what is selected in list to textbox
          # update has argument value set the current value on selected list
        case "Exit":
          break
        case sg.WIN_CLOSED:
          # exit() - Stop the program complete
            break # - Stop the loop then prints (Bye)
# print(Bye)
window.close()