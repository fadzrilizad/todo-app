import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo: ")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

structure = [
                [label],
                [input_box, add_button]
            ]

window = sg.Window("My To-Do App", layout=structure)
window.read()
window.close()

