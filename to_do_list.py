import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = tasks_list.curselection()
    if selected_task:
        tasks_list.delete(selected_task)

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

tasks_list = tk.Listbox(root)
tasks_list.pack()

root.mainloop()





