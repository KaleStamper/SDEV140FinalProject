# SDEV140FinalProject
## Final Project for SDEV 140
## User Manual: 

This GUI application allows a user to enter or search for an address, tracking number, and name. They can be looked up through any of the three through key phrases or letters. 

## Home Window:
This is the default window that the user is entered into. This window has two buttons: the entry button (takes the user to the entry GUI) and the search entry (takes user to the search GUI). The buttons direct the user to a new window, either the entry window or the search window.

## Entry Window:
This is for entering a name, address, or tracking number. The tracking number must be 12 digits or the user will be prompted with an error message. If the user opts to enter a name, the user must make sure there are spaces and is not blank or an error message will pop up. The user can look up the information on the search bar that they entered. There is no address validation as addresses are far too difficult to verify and validate (addresses can have names as numbers, can be 1-? digits, and the street itself, like avenue, street, and court, can make an address difficult to validate). The entry can be saved and stored, the text can be cleared, or the user can exit the window. 

## Search Window:
The user is prompted to search with a drop-down menu. The drop down menu is defaulted to any and can look up key phrases. For example, in the example data in the GUI, if you look up "ale", it will return all entries with the letters "ale" if the name option is selected. If the user selects an address and searches a name, no results will be given. The user can use the "any" option to look for key phrases through all three options of searches (tracking number, name, or address). The text can be cleared and the window can be exited with the use of the buttons provided.
