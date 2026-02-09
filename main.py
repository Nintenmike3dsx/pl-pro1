import tkinter as tk
import keyboard


root = tk.Tk()
root.title("Crater: Lego Ship ")

canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

font_size = 11

def about():
    about_window = tk.Toplevel(root)
    about_window.title("About!")
    about_window.geometry("250x150")
    about_window.resizable(False, False)
    about_text = "Team Crater Lego Ship Lander!\nCreated By:\n Michael Arend (Front End)\n David Born (Programmer)\n Sam Tavani (Back End)\n Daniel Randall (Programmer)\nLibraries Used: Tkinter and Pyodbc"
    about_label = tk.Label(about_window, text=about_text, padx=10, pady=10, font=("Helvetica", 10))
    about_label.pack()


def exit_app():
    root.destroy()


menu_bar = tk.Menu(root)

about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="Trial 1: Lightest Weight, Instruments Only!")
about_menu.add_command(label="Trial 2: Medium Weight, Instruments & Astronaut!")
about_menu.add_command(label="Trial 3: Heaviest Weight, Instruments, Astronaut, and Rover!")
about_menu.add_separator()
about_menu.add_command(label="About", command=about)
about_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="Menu", menu=about_menu)

trialmenu = tk.Menu(menu_bar, tearoff=0)

trial_menu = tk.Menu(trialmenu, tearoff=0)
trial_menu.add_command(label="Trial 1")
trial_menu.add_command(label="Trial 2")
trial_menu.add_command(label="Trial 3")
trial_menu.add_cascade(label="Trials", menu=trial_menu)

trial_var = tk.IntVar()
trial_var.set(1)
root.config(menu=menu_bar)

root.mainloop()