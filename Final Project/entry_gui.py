Vmport helper

import tkinter as tk
from PIL import ImageTk, Image


def populate_entry_gui(root, saved_list):

    root.title("Address Entry")
    root.geometry("800x600")
    root.configure(bg="orange")

    image = ImageTk.PhotoImage(Image.open("Fedex-Logo.png"))
    image_label = tk.Label(root, image = image)
    image_label.pack()

    # INPUT
    tracking_label = tk.Label(root, text = "12 Digit Tracking Number:", bg="orange")
    tracking_label.pack()
    entry_tracking = tk.StringVar()
    tracking_bar = tk.Entry(root, textvariable=entry_tracking, width=30)
    tracking_bar.pack()

    name_label = tk.Label(root, text = "Name:", bg="orange")
    name_label.pack()
    entry_name = tk.StringVar()
    name_bar = tk.Entry(root, textvariable=entry_name, width=30)
    name_bar.pack()

    address_label = tk.Label(root, text = "Address:", bg="orange")
    address_label.pack()
    entry_address = tk.StringVar()
    address_bar = tk.Entry(root, textvariable=entry_address, width=30)
    address_bar.pack()

    # BUTTONS

    error_msg_label = tk.Label(root, text="", fg="red", bg="orange")
    error_msg_label.pack()

    saved_listvariable = tk.Variable(value=saved_list)
    list_box = tk.Listbox(root, listvariable = saved_listvariable)
    # https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
    save_button = tk.Button(root, text="Save", command= lambda: helper.save_entry([entry_tracking, entry_name, entry_address], error_msg_label, saved_list, list_box))
    save_button.pack()

    clear_button = tk.Button(root, text="Clear", command= lambda: helper.clear_all([entry_tracking, entry_name, entry_address]))
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

    # Testing for the Entry GUI
    root = tk.Tk()
    populate_entry_gui(root, saved_list)
    root.mainloop()