import tkinter as tk
import keyboard

root = tk.Tk()
root.title("To-Do List")

canvas = tk.Canvas(root, width=400, height=400) # Change if needed
canvas.pack()

font_size = 11

tasks = []

task_location = tk.Frame(root)
task_location.place(x=0, y=25)

def updateloop():
    for widget in task_location.winfo_children():
        widget.destroy()
    tk.Label(task_location, text="Your Tasks:", font=("Helvetica", 12, "bold")).pack(anchor="w")
    for i, task in enumerate(tasks, 1):
        task_label = tk.Label(task_location, text=f"{i}. {task}", font=("Helvetica", 10), anchor="w")
        task_label.pack(fill="x", pady=2)

def add_task_to_list():
    task = text_box.get()
    if task.strip():
        tasks.append(task.strip())
        text_box.delete(0, tk.END)  # Clear box after user inputs
        updateloop()  # Update list to show new task

def addtask():
    global text_box
    text_window = tk.Toplevel(root)
    text_window.title("Add Your New Task")
    text_window.geometry("300x200")
    
    label = tk.Label(text_window, text="Enter your task:", font=("Helvetica", 10))
    label.pack(pady=10)
    
    text_box = tk.Entry(text_window, width=30, font=("Helvetica", 10))
    text_box.pack(pady=5)
    text_box.focus_set()
    
    add_task_button = tk.Button(text_window, text="Add Task to List", command=add_task_to_list)
    add_task_button.pack(pady=5)
    
    def close_window():
        text_window.destroy()
    
    close_button = tk.Button(text_window, text="Close", command=close_window)
    close_button.pack(pady=10)

def about():
    about_window = tk.Toplevel(root)
    about_window.title("About!")
    about_window.geometry("250x100")
    about_window.resizable(False, False)
    about_text = "Created by Michael Arend\nLibraries Used: Tkinter"
    about_label = tk.Label(about_window, text=about_text, padx=10, pady=10, font=("Helvetica", 10))
    about_label.pack()

def exit_app():
    root.destroy()

menu_bar = tk.Menu(root)

add_task_button = tk.Button(root, text="Add Task", command=addtask)
add_task_button.place(x=0, y=0)

about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About", command=about)
about_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="Menu", menu=about_menu)

trialmenu = tk.Menu(menu_bar, tearoff=0)

trial_var = tk.IntVar()
trial_var.set(1)
root.config(menu=menu_bar)


updateloop()
root.mainloop()