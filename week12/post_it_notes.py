import tkinter as tk
import sqlite3 as sql
from datetime import date
from tkinter import messagebox

def main():
    
    createDB()
    create_table()

    # Create the Tk root object.    
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Pin Your Note")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def createDB():
    try:
        con = sql.connect('pin_your_note.db')
        con.commit()
        con.close()
    except:
        print("Connected to table of database")

def create_table():    
    try:
        con = sql.connect('pin_your_note.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE notes_table
                        (date DATETIME, notes_title text, notes text)''')
        con.commit()
        con.close()
    except:
        print("Connected to table of database")

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
                    
    # Create the Add Notes widgets.
    lbl_notes_title = tk.Label(frm_main, text="Notes title:")
    lbl_notes = tk.Label(frm_main, text="Notes:")    
    ent_notes_title = tk.Entry(frm_main, width=50)
    ent_notes = tk.Text(frm_main, width=38, height=5)
    btn_add_notes = tk.Button(frm_main, text="Add Notes")
    btn_view_notes = tk.Button(frm_main, text="View Notes")
    btn_delete_notes = tk.Button(frm_main, text="Delete Notes")
    btn_update_notes = tk.Button(frm_main, text="Update Notes")
    btn_add = tk.Button(frm_main, text="Add")
    btn_cancel = tk.Button(frm_main, text="Cancel")    
    
    # Display the below buttons in the grid.
    btn_add_notes.grid(row=0, column=0, padx=3, pady=3, sticky='W')
    btn_view_notes.grid(row=0, column=1, padx=3, pady=3, sticky='W')
    btn_delete_notes.grid(row=0, column=2, padx=3, pady=3, sticky='W')
    btn_update_notes.grid(row=0, column=3, padx=3, pady=3, sticky='W')                

    # Creating a function for removing widgets from the grid
    def remove_add_note_widgets():
        """Remove a given widget."""
        lbl_notes_title.grid_remove()
        ent_notes_title.grid_remove()
        lbl_notes.grid_remove()
        ent_notes.grid_remove()
        btn_add.grid_remove()
        btn_cancel.grid_remove()

    # Creating a function for making all add note widgets visible
    def display_add_note_widgets(lbl_notes_title, 
                                 ent_notes_title, 
                                 lbl_notes, 
                                 ent_notes,
                                 btn_add,
                                 btn_cancel):
        lbl_notes_title.grid(row=1, column=0, padx=3, pady=3, sticky='W') 
        ent_notes_title.grid(row=2, column=0, columnspan=4, padx=3, pady=3, sticky='W')
        lbl_notes.grid(row=3, column=0, columnspan=4, padx=3, pady=3, sticky='W')
        ent_notes.grid(row=4, column=0, columnspan=4, padx=3, pady=3, sticky='W')
        btn_add.grid(row=5, column=0, padx=3, pady=3, sticky="W")
        btn_cancel.grid(row=5, column=3, padx=3, pady=3, sticky="E")

    def clear_note_entries():
        """Clear all entries."""
        ent_notes_title.delete(0, 'end')
        ent_notes.delete('1.0', 'end')
        ent_notes_title.focus()    

    def add_notes():
        con = sql.connect('pin_your_note.db')
        cur = con.cursor()

        #Get input values
        today = date.today()       
        notes_title = ent_notes_title.get()
        notes = ent_notes.get("1.0", "end-1c")
        #Raise a prompt for missing values
        if (len(notes_title)<=0) & (len(notes)<=1):
            messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
        else:            
            clear_note_entries()
            #Insert into the table
            cur.execute("INSERT INTO notes_table VALUES ('%s','%s','%s')" %(today, notes_title, notes))
            messagebox.showinfo(message="Note added")            
            #Commit to preserve the changes
            con.commit()    

    # Display all widges related to Add Notes when Add Notes button is clicked.
    btn_add_notes.config(command=lambda: display_add_note_widgets(
                                            lbl_notes_title, 
                                            ent_notes_title,
                                            lbl_notes, 
                                            ent_notes,
                                            btn_add,
                                            btn_cancel))
    
    btn_add.config(command=lambda: add_notes())

    btn_cancel.config(command=lambda: remove_add_note_widgets())

if __name__ == "__main__":
    main()
