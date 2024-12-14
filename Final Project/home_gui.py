
from entry_gui import populate_entry_gui
from search_gui import populate_search_gui

import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Home")
root.geometry("1200x860")
root.configure(bg="purple")

saved_list = [
    {
    "tracking_number": "123456789012",
    "name": "Kale Stamper",
    "address": "308 Negra Arroyo Lane"
    },
    {
    "tracking_number": "123456733012",
    "name": "Bale Hamper",
    "address": "13 River Street"
    },
    {
    "tracking_number": "123456342012",
    "name": "Male Lamper",
    "address": "308 Beach Cove"
    },
    {
    "tracking_number": "123456789012",
    "name": "Stale Damper",
    "address": "328 Negra Arroyo Street"
    },
    {
    "tracking_number": "123456789022",
    "name": "Shale Camper",
    "address": "3038 Blanco Arroyo Lane"
    }
]

#Image and Label
image = ImageTk.PhotoImage(Image.open("FedexHomeWindowPNG.png"))
image_label = tk.Label(root, image = image)
image_label.pack(side = 'top')

#Button to Enter User into Entry Window
def open_entrygui():
    #Take User to Data Entry Window
    entrygui_window = tk.Toplevel()
    entrygui_window.title("Data Entry")

    populate_entry_gui(entrygui_window, saved_list)

button = tk.Button(root, text="Open Entry Window", command=open_entrygui)
button.pack()

#Button to Enter User into Search Window
def open_searchgui():
    #Take User to Search Window
    searchgui_window = tk.Toplevel()
    searchgui_window.title("Search Entries")

    populate_search_gui(searchgui_window, saved_list)
    

button = tk.Button(root, text="Open Search Window", command=open_searchgui)
button.pack()

root.mainloop()

