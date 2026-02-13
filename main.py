# By Michael Arend - see readme for all sources
import tkinter as tk
import os
import winsound

root = tk.Tk()
root.title("To-Do List")
canvas = tk.Canvas(root, width=300, height=500) # Change if needed for more than 15 tasks
root.resizable(False, False) # Leave lock on x x axis, maybe unlock y if needed
canvas.pack()

# Optional Enhancement 1 - button color
def buttoncolor(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

# Optional Enhancement 2 - Button Audio
def sound_check():
    winsound.PlaySound('yay.wav', winsound.SND_ASYNC)

def sound_delete():
    winsound.PlaySound('gone.wav', winsound.SND_ASYNC)

#background_image = tk.PhotoImage(file="background.png")     Add back in later if possible
#background_image_id = canvas.create_image(400, 400, image=background_image)

# font_size = 11 not needed anymore defined size individually
tasks = [] # Need to limit to 15
taskdone = []

task_location = tk.Frame(root)
task_location.place(x=0, y=25)

#Main loop for updating the list
def updateloop():
    for widget in task_location.winfo_children():
        widget.destroy()

    # List properties - edit later with different font and sizes
    tk.Label(task_location, text="Your Tasks:", font=("Helvetica", 12, "bold")).pack(anchor="w")
    for i, task in enumerate(tasks, 1):
        task_row = tk.Frame(task_location)  
        task_row.pack(anchor="w", fill="x", pady=2)
        
        # Left side - checkbox
        if i-1 < len(taskdone): #fix for bug that resets checkmarks when a task is deleted
            var = taskdone[i-1]
        else:
            var = tk.IntVar()
            taskdone.append(var)
        checkbox = tk.Checkbutton(task_row, variable=taskdone[i-1], command=sound_check) # added new audio
        checkbox.pack(side="left")
        
        # Middle - label
        task_label = tk.Label(task_row, text=f"{i}. {task}", font=("Helvetica", 10), anchor="w")
        task_label.pack(side="left", padx=(5, 0))
        
        # Right side - delete
        delete_button = tk.Button(task_row, text="Remove", command=lambda idx=i-1: delete_task(idx))
        delete_button.pack(side="right", padx=(0, 10))

# Removes the task and re-runs the main updateloop 
def delete_task(index):
    sound_delete()
    tasks.pop(index)
    taskdone.pop(index) 
    updateloop()

# Adding a task to the list
def add_task_to_list():
    task = text_box.get() # Store input
    if len(tasks) >= 15:  # Limit of 15 tasks
        return
    if len(task) > 27:    # Limit of 27 characters for task name
        return
    tasks.append(task) # Add to list
    text_box.delete(0, 'end') # Clear box after user inputs, test this more
    updateloop()

# UI to add a task
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

# Optional Enhancement 3 - Task exporting
def save_tasks():
    with open("tasks.txt", "w") as file:
        file.write("\n".join(tasks))

# Optional Enhancement 4 - Task loading
def load_tasks():
    if os.path.exists("tasks.txt"):
        tasks[:] = open("tasks.txt").read().splitlines()
        updateloop()
    else:
        pass
    # this is really simple, may want to add a file check prompt to user

# Optional Enhancement 5 - Data Clearing, will delete any existing tasks.txt
def clear_data():
    if os.path.exists("tasks.txt"):
       os.remove("tasks.txt")
    else:
        pass

def about():
    about_window = tk.Toplevel(root)
    about_window.title("About!")
    about_window.geometry("250x100")
    about_window.resizable(False, False)
    about_text = "Created by Michael Arend\nLibraries Used: Tkinter\nSources in README\nAudio From myinstants.com"
    about_label = tk.Label(about_window, text=about_text, padx=10, pady=10, font=("Helvetica", 10))
    about_label.pack()

def exit_window():
    global text_box
    text_window = tk.Toplevel(root)
    text_window.title("Are You Sure You Want to Close?")
    text_window.geometry("200x100")
    
    label = tk.Label(text_window, text="Save Your Tasks Before Exiting!", font=("Helvetica", 10))
    label.pack(pady=10)
    close_button = tk.Button(text_window, text="Close Application", command=exit_app)
    close_button.pack(pady=10)

def exit_app():
    root.destroy()

# Button property code
menu_bar = tk.Menu(root)
add_task_button = tk.Button(root, text="Add Task", command=addtask, bg="SystemButtonFace")
add_task_button.place(x=0, y=0)
buttoncolor(add_task_button, "#CEBB0F", "SystemButtonFace")

export_button = tk.Button(root, text="Save Tasks", command=save_tasks, bg="SystemButtonFace")
export_button.place(x=110, y=0)
buttoncolor(export_button, "#068831", "SystemButtonFace")

import_button = tk.Button(root, text="Load Tasks", command=load_tasks, bg="SystemButtonFace")
import_button.place(x=224, y=0)
buttoncolor(import_button, "#553FFE", "SystemButtonFace")

# Top menu bar
menu_bar.add_cascade(label="Exit", command=exit_window)
menu_bar.add_cascade(label="About", command=about)
menu_bar.add_cascade(label="Clear Data", command=clear_data)
root.config(menu=menu_bar)

load_tasks() # will pull tasks but if not formatted right will get odd results
root.mainloop()

# Bugs needing to be fixed:

# Fix text not fully clearing
# Update sound plugin as mp3player is not supported on python 3
# Chcekmarks are cleared when a task is deleted
# If no tasks.txt app does not launch, need to add a if pass statement

# Optional features added:
# Audio when task is complete / deleted
# Button hover effects
# Export tasks into txt file
# Load any saved tasks on startup
# Clear saved tasks.txt file 