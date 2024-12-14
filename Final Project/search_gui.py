
import helper

import tkinter as tk
from PIL import ImageTk, Image


def populate_search_gui(root, saved_list):

    root.title("Search Entries")
    root.geometry("800x600")
    root.configure(bg="orange")

    image = ImageTk.PhotoImage(Image.open("Fedex-Logo.png"))
    image_label = tk.Label(root, image = image)
    image_label.pack()

    # INPUT
    search_label = tk.Label(root, text = "Search:", bg="orange")
    search_label.pack()
    entry_text = tk.StringVar()
    entry_bar = tk.Entry(root, textvariable=entry_text, width=30)
    entry_bar.pack()

    # https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter
    type_variable = tk.StringVar(root)
    type_variable.set("any")
    type_menu = tk.OptionMenu(root, type_variable, "any", "name", "address", "tracking number")
    type_menu.pack()

    # BUTTONS

    saved_listvariable = tk.Variable(value=saved_list)
    list_box = tk.Listbox(root, listvariable = saved_listvariable)


    search_button = tk.Button(root, text="Search", command= lambda: helper.update_listbox(list_box, helper.search_text(saved_list, type_variable.get(), entry_text.get())))
    search_button.pack()

    clear_button = tk.Button(root, text="Clear", command= lambda: helper.clear_text(entry_text))
    clear_button.pack()

    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack()


    # DISPLAY - saved_list
    list_box.pack(fill='x', expand=1)



if __name__ == "__main__":

    print("Run 'home_gui.py' for the main program.")

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
    }
    ]

    # Testing for the Search GUI
    root = tk.Tk()
    populate_search_gui(root, saved_list)
    root.mainloop()
