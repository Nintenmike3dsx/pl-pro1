import tkinter as tk
import keyboard

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")  #MAKE LARGER IF NEEDED

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

font_size = 11

tasks = []

tasks_frame = tk.Frame(root)
tasks_frame.place(x=0, y=25)

def updateloop():
    for widget in tasks_frame.winfo_children():
        widget.destroy()

    tk.Label(tasks_frame, text="Your Added Tasks:", font=("Helvetica", 10, "bold")).pack(anchor="w")
    
    for i, task in enumerate(tasks, 1):
        task_label = tk.Label(tasks_frame, text=f"{i}. {task}", font=("Helvetica", 10), anchor="w")
        task_label.pack(fill="x", pady=2)

def addtask():
    task = text_box.get()
    if task.strip():
        tasks.append(task.strip())
        text_box.delete(0, tk.END)  #Clears the box of the past input
        updateloop()  #Updateloop to appear on home menu

def open_text_window():
    global text_box
    text_window = tk.Toplevel(root)
    text_window.title("Add Your New Task")
    text_window.geometry("300x200")
    
    label = tk.Label(text_window, text="Enter your task:", font=("Helvetica", 10))
    label.pack(pady=10)
    
    text_box = tk.Entry(text_window, width=30, font=("Helvetica", 10))
    text_box.pack(pady=5)
    text_box.focus_set()

    add = tk.Button(text_window, text="Add Task to List", command=addtask)
    add.pack(pady=5)
    
    def close():
        text_window.destroy()
    
    close = tk.Button(text_window, text="Close", command=close)
    close.pack(pady=10)

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

addtaskbutton = tk.Button(root, text="Add Task", command=addtask)
addtaskbutton.place(x=0, y=0)

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