# By Michael Arend - see readme for all sources
import tkinter as tk
import keyboard
import os 
import winsound

root = tk.Tk()
root.title("To-Do List")
canvas = tk.Canvas(root, width=300, height=500) # Change if needed
canvas.pack()

font_size = 11

tasks = []
taskdone = []

task_location = tk.Frame(root)
task_location.place(x=0, y=25)

def sound():
    winsound.PlaySound('yay.wav', winsound.SND_ASYNC)

def updateloop():
    for widget in task_location.winfo_children():
        widget.destroy()
    taskdone.clear()

    # List properties - edit later with different font and sizes
    tk.Label(task_location, text="Your Tasks:", font=("Helvetica", 12, "bold")).pack(anchor="w")
    for i, task in enumerate(tasks, 1):
        task_row = tk.Frame(task_location)  
        task_row.pack(anchor="w", fill="x", pady=2)
        
        # Left side - checkbox
        var = tk.IntVar()
        taskdone.append(var)
        checkbox = tk.Checkbutton(task_row, variable=var, command=sound)
        checkbox.pack(side="left")
        
        # Middle - label
        task_label = tk.Label(task_row, text=f"{i}. {task}", font=("Helvetica", 10), anchor="w")
        task_label.pack(side="left", padx=(5, 0))
        
        # Right side - delete
        delete_button = tk.Button(task_row, text="Delete Task", command=lambda idx=i-1: delete_task(idx))
        delete_button.pack(side="right", padx=(0, 10))
# Removes the task and re-runs the main updateloop 
def delete_task(index):
    tasks.pop(index)
    updateloop()
    # Buggggg - this removes any tasks that were currently checked as it loops everything, look into a solution later

def add_task_to_list():
    task = text_box.get()
    if task.strip():
        tasks.append(task.strip())
        text_box.delete(0, tk.END)  # Clear box after user inputs
        updateloop()  # Update list to show new task with checkbox and delete button

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


def export_tasks():
    with open("tasks.txt", "w") as file:
        file.write("\n".join(tasks))

def about():
    about_window = tk.Toplevel(root)
    about_window.title("About!")
    about_window.geometry("250x100")
    about_window.resizable(False, False)
    about_text = "Created by Michael Arend\nLibraries Used: Tkinter\nSources in README"
    about_label = tk.Label(about_window, text=about_text, padx=10, pady=10, font=("Helvetica", 10))
    about_label.pack()

def exit_app():
    root.destroy()


#
def buttoncolor(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

menu_bar = tk.Menu(root)

add_task_button = tk.Button(root, text="Add Task", command=addtask, bg="SystemButtonFace")
add_task_button.place(x=0, y=0)
buttoncolor(add_task_button, "#FEEB3F", "SystemButtonFace")

export_button = tk.Button(root, text="Export Tasks", command=export_tasks, bg="SystemButtonFace")
export_button.place(x=85, y=0)
buttoncolor(export_button, "#FE3F3F", "SystemButtonFace")

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