#from functions import get_todos,write_todos
import functions
import time



while True:
    user_action = input("Type action: add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()
        
        #Another way to strip the newline from output
        # new_todos = []
        # for item in todos:
        #     item.strip('\n')
        #     new_todos.append(item)
        #
        # for index,item in enumerate(new_todos):
        #     row = f"{index + 1}-{item}"
        #     print(row)
        #Another way is thru list comprehensions
        # new_todos = [item.strip() for item in todos]
        # for index,item in enumerate(new_todos):
        #     row = f"{index + 1}-{item}"
        #     print(row,end='')

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos =functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your task is invalid. Try again")
            continue

    elif user_action.startswith('completed'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {index + 1} {todo_to_remove} was removed from list!"
            print(message)
        except IndexError:
            print("There's no task number like that. Try again")
            continue
            
    elif 'exit' in user_action:
        break

    else:
        print("Task is not one of my options,pls recheck.")
print("Bye!")





