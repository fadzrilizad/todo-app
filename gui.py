import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

structure = [
                [label],
                [input_box, add_button]
            ]

font_size = ("Helvetica", 12)

window = sg.Window("My To-Do App",
                   layout=structure,
                   font=font_size)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()

