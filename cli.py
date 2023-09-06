import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_input = input("Type add, show, edit, complete, exit: ")
    user_input = user_input.strip()

    todos = functions.get_todos()

    if user_input.startswith('add'):
        todo = user_input[4:]
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_input.startswith('show'):
        for i, item in enumerate(todos):
            item = item.strip('\n').capitalize()
            print(f"{i + 1}-{item}")

    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            number = number - 1

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])
            index = number - 1
            removed = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"todo {removed}, has been remove"
            print(message)

        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item in that number")
            continue

    elif user_input.startswith('exit'):
        break
    else:
        print("command is not valid")

print("bye")
