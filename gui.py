import FreeSimpleGUI as sg
from modules import functions

# google - pypi.org - 3rd part library /Modules . Instances of those buttons, textbox , windows
# pip install FreeSimpleGUI Create window , button
# layout is argument and be list and must connect the instances (Label ,InputText)
# Window is type and its instance ("My To-DO App")
# Read - Method display the window on the screen.

label1 = sg.Text("Enter todo: ")
input_text = sg.InputText(tooltip="textbox" , key="todo") # add = key

button = sg.Button("Add")

window = sg.Window("My Todo App" ,
                   layout=[[label1 , input_text , button]] ,
                   font=("Helvetica", 10))

while True:   # Make the window not to close
    event ,values = window.read() # InpuText -> tuple Read the value on the input text ("Add",{todo:"Test1"})
    print(event) # event -> Action return label "Add"
    print(values) # dictionary(key & value) ->{todo:Test1}

    match event :
        case "Add":
          todos = functions.get_todos()  # Will return list of todos
          new_todo = values["todo"] + "\n"  # Get value of the key todo
          todos.append(new_todo)
          functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break
window.close()