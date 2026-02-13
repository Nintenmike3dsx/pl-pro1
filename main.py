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
tasks = [] # Holds task name
taskdone = [] # Holds is done/not done

task_location = tk.Frame(root)
tk.Label(task_location, text="To-Do:", font=("Helvetica", 12, "bold")).pack(anchor='w') # create header on boot
task_location.place(x=0, y=25) # adjust later if needed

#Main loop for updating the list
def updateloop():
    # Refresh list
    for widget in task_location.winfo_children():
        widget.destroy()
    # remake header after destroy
    tk.Label(task_location, text="To-Do:", font=("Helvetica", 12, "bold")).pack(anchor='w')
    # Maintain check state
    while len(taskdone) < len(tasks):
        taskdone.append(tk.IntVar())
    # Create all task rows from task limit variable
    for i, task in enumerate(tasks):
        row = tk.Frame(task_location)
        row.pack(fill='x', pady=1)  # Adjust padding if needed later
        # Check mark / text / delete properties
        tk.Checkbutton(row, variable=taskdone[i], command=sound_check).pack(side='left')
        tk.Label(row, text=f"{i+1}. {task}", font=("Helvetica", 10)).pack(side='left', padx=5)
        tk.Button(row, text="Remove", command=lambda idx=i: delete_task(idx)).pack(side='right', padx=5)

# Removes the task and re-runs the main updateloop 
def delete_task(index):
    sound_delete()
    tasks.pop(index) # remove from list
    taskdone.pop(index) # remove check 
    updateloop()

# Adding a task to the list
def add_task_to_list():
    task = text_box.get() # Store input
    if len(tasks) >= 15:  # Limit of 15 tasks
        return
    if len(task) > 27:    # Limit of 27 characters for task name
        return
    tasks.append(task) # Add to list
    text_box.delete(0, 'end') # Clear box after user inputs
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
    clear_data_window = tk.Toplevel(root)
    clear_data_window.title("Caution!")
    clear_data_window.geometry("350x100")
    clear_data_window.resizable(False,False)
    label = tk.Label(clear_data_window, text="THIS WILL PERMANENTLY YEET ALL SAVED TASKS!", font=("Helvetica", 10))
    label.pack(pady=10)
    clear_button = tk.Button(clear_data_window, text="DELETE DATA", command=clear_data_button)
    clear_button.pack(pady=10)

def clear_data_button():
    if os.path.exists("tasks.txt"):
        os.remove("tasks.txt")
    else:
        pass
    tasks.clear()
    taskdone.clear()
    updateloop()

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
    text_window.title("Exit")
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
export_button.place(x=235, y=0)
buttoncolor(export_button, "#068831", "SystemButtonFace")

# Top menu bar
menu_bar.add_cascade(label="Exit", command=exit_window)
menu_bar.add_cascade(label="About", command=about)
menu_bar.add_cascade(label="Clear Data", command=clear_data)
root.config(menu=menu_bar)

load_tasks() # will pull tasks but if not formatted right will get odd results
root.mainloop()