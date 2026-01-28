import FreeSimpleGUI as sg

label1 = sg.Text("Enter todo: ")
input_text = sg.InputText(tooltip="textbox")

button = sg.Button("Add")

window = sg.Window("My Todo App" , layout=[[label1 , input_text , button]])
window.read()
window.close()