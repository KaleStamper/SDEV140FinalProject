import tkinter as tk

# Validate that the string is a 12 digit number
def validate_tracking_number(tracking_number):
    if tracking_number.isdigit() and len(tracking_number) == 12:
        return True
    else:
        return False


# Save an entry from the list of widgets
def save_entry(entry_widget_list, error_widget, ls, listbox):

    tracking_widget, name_widget, address_widget = entry_widget_list
    tracking_number = tracking_widget.get()
    name = name_widget.get()
    address = address_widget.get()

    if validate_tracking_number(tracking_number):
        # Update error message
        error_widget.config(text=f"Successfully added entry with tracking number '{tracking_number}'.", fg="green")

        # add new dictionary entry and update the listbox
        new_entry = {"tracking_number":tracking_number, "name":name, "address":address}
        ls.append(new_entry)
        update_listbox(listbox, ls)

    else:
        error_widget.config(text = "Invalid tracking number. Tracking number must have 12 digits.", fg="red")


# Clears the text of a given entry widget
def clear_text(entry_widget):
    entry_widget.set("")

# Clears multiple widgets
def clear_all(entry_widget_list):
    for w in entry_widget_list:
        clear_text(w)


# Takes a search type (any, address, tracking number, name) and the text to serach for. Returns list of matches
def search_text(entry_list, search_type, search_text):
    matches = []
    search_text = search_text.lower()

    for entry in entry_list:
        # search thru all values if 'any' is used
        if search_type == "any":
            for val in entry.values():
                if search_text in val.lower():
                    matches.append(entry)
                    break
        # search thru specific search type (address, tracking number, name)
        elif search_text in entry[search_type].lower():
            matches.append(entry)

    return matches


# Update the list that's present in a listbox
def update_listbox(listbox, ls):
    list_variable = tk.Variable(value = ls)
    listbox.configure(listvariable = list_variable)


