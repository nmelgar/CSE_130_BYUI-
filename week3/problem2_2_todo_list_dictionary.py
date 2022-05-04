todo_list = ["play soccer", "go swimming",
             "pool party", "buy milk", "do homework"]
type_of_task = ["to-do", "to-do", "event", "to-do", "to-do"]

print("Things to do: ")
counter = 1
for todo_item, task_type in zip(todo_list, type_of_task):
    if task_type == "to-do":
        print(f"{counter}. {todo_item}")
        counter += 1
