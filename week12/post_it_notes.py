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
        print("Database already created")

def create_table():    
    try:
        con = sql.connect('pin_your_note.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE notes_table
                        (date DATETIME, notes_title text, notes text)''')
        con.commit()
        con.close()
    except:
        print("Notes table already created")

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
    btn_update = tk.Button(frm_main, text="Update")
    btn_cancel = tk.Button(frm_main, text="Cancel")    
    
    # Create the Search Notes widgets.
    lbl_enter_note_title = tk.Label(frm_main, text="Enter note title:")
    ent_search_note_title = tk.Entry(frm_main, width=37)
    btn_search = tk.Button(frm_main, text="Search")

    # Create the Update Notes widget
    lbl_enter_note_to_update_title = tk.Label(frm_main, text="Enter note title to update:")
    ent_search_note_to_update_title = tk.Entry(frm_main, width=37)
    btn_search_note_to_update = tk.Button(frm_main, text="Search")

    # Create the Delete Notes widget
    ent_delete_note_title = tk.Entry(frm_main, width=37)
    btn_delete = tk.Button(frm_main, text="Delete")
    btn_delete_all = tk.Button(frm_main, text="Delete All")

    # Display the below buttons in the grid.
    btn_add_notes.grid(row=0, column=0, padx=3, pady=3, sticky='W')    
    btn_view_notes.grid(row=0, column=1, padx=3, pady=3, sticky='W')
    btn_delete_notes.grid(row=0, column=2, padx=3, pady=3, sticky='W')
    btn_update_notes.grid(row=0, column=3, padx=3, pady=3, sticky='W')                
    
    def remove_add_note_widgets():
        """
        Remove all the widgets related to Add Notes feature.        
        Return: nothing
        """ 
        lbl_notes_title.grid_remove()
        ent_notes_title.grid_remove()
        lbl_notes.grid_remove()
        ent_notes.grid_remove()
        btn_add.grid_remove()
        btn_cancel.grid_remove()
        btn_update.grid_remove()
        lbl_enter_note_to_update_title.grid_remove()
        ent_search_note_to_update_title.grid_remove()
        btn_search_note_to_update.grid_remove()

    def remove_search_widgets():
        """
        Remove all the widgets related to Search Notes feature.        
        Return: nothing
        """ 
        lbl_enter_note_title.grid_remove()
        ent_search_note_title.grid_remove()
        btn_search.grid_remove()   

    def remove_delete_widgets():
        """
        Remove all the widgets related to Delete Notes feature.        
        Return: nothing
        """ 
        lbl_enter_note_title.grid_remove()
        ent_delete_note_title.grid_remove()
        btn_delete.grid_remove()
        btn_delete_all.grid_remove()

    def remove_update_widgets():
        """
        Remove all the widges related to Update Notes feature.        
        Return: nothing
        """ 
        lbl_enter_note_to_update_title.grid_remove()
        ent_search_note_to_update_title.grid_remove()
        btn_search_note_to_update.grid_remove()
        btn_update.grid_remove()
    
    def clear_note_entries():
        """Clear all entries."""
        ent_notes_title.delete(0, 'end')
        ent_notes.delete('1.0', 'end')
        ent_notes_title.focus()

    def display_add_note_widgets():
        """
        Make all the widges related to Add Notes feature visible.        
        Return: nothing
        """ 
        remove_search_widgets()
        remove_delete_widgets()
        remove_update_widgets()
        lbl_notes_title.grid(row=1, column=0, padx=3, pady=3, sticky='W') 
        ent_notes_title.grid(row=2, column=0, columnspan=4, padx=3, pady=3, sticky='W')
        lbl_notes.grid(row=3, column=0, columnspan=4, padx=3, pady=3, sticky='W')
        ent_notes.grid(row=4, column=0, columnspan=4, padx=3, pady=3, sticky='W')
        btn_add.grid(row=5, column=0, padx=3, pady=3, sticky="W")
        btn_cancel.grid(row=5, column=3, padx=3, pady=3, sticky="E")
    
    def display_search_widgets():
        """
        Make all the widges related to Search Notes feature visible.        
        Return: nothing
        """ 
        remove_delete_widgets()
        lbl_enter_note_title.grid(row=1, column=0, columnspan=2, padx=3, pady=3, sticky='W')
        ent_search_note_title.grid(row=2, column=0, columnspan=3, padx=3, pady=3, sticky='W')
        btn_search.grid(row=2, column=3, padx=3, pady=3, sticky='W')        
        
    def display_delete_note_widgets():
        """
        Make all the widges related to Delete Notes feature visible.        
        Return: nothing
        """ 
        remove_search_widgets()
        remove_add_note_widgets()
        lbl_enter_note_title.grid(row=1, column=0, columnspan=2, padx=3, pady=3, sticky='W')
        ent_delete_note_title.grid(row=2, column=0, columnspan=3, padx=3, pady=3, sticky='W')        
        btn_delete.grid(row=2, column=3, padx=3, pady=3, sticky='E')
        btn_delete_all.grid(row=2, column=4, padx=3, pady=3, sticky='E')
    
    def display_update_note_widgets():
        """
        Make all the widges related to Update Notes feature visible.        
        Return: nothing
        """ 
        remove_search_widgets()
        remove_delete_widgets()        
        lbl_enter_note_to_update_title.grid(row=1, column=0, columnspan=2, padx=3, pady=3, sticky='W')
        ent_search_note_to_update_title.grid(row=2, column=0, columnspan=3, padx=3, pady=3, sticky='W')
        btn_search_note_to_update.grid(row=2, column=3, padx=3, pady=3, sticky='W')
                 
        lbl_notes_title.grid(row=3, column=0, padx=3, pady=3, sticky='W') 
        ent_notes_title.grid(row=4, column=0, columnspan=4, padx=3, pady=3, sticky='W')
        lbl_notes.grid(row=5, column=0, columnspan=4, padx=3, pady=3, sticky='W')
        ent_notes.grid(row=6, column=0, columnspan=4, padx=3, pady=3, sticky='W')        
        btn_update.grid(row=7, column=0, padx=3, pady=3, sticky="W")
        btn_cancel.grid(row=7, column=3, padx=3, pady=3, sticky="E")

    def display_view_notes_widgets():
        """
        Make all the widges related to View Notes feature visible.        
        Return: nothing
        """ 
        remove_add_note_widgets()
        display_search_widgets()    


    def add_notes():
        """
        Retrieve the data from Add Notes entries and save it to the DB        
        Return: nothing
        """ 
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
    
    def delete_note():
        """
        Retrieve the data from Delete Notes entries and delete it from DB        
        Return: nothing
        """ 
        con = sql.connect('pin_your_note.db')
        cur = con.cursor()

        #Obtain input values
        notes_title = ent_delete_note_title.get()
        
        if (len(notes_title)<=0): 
            #Raise error for no inputs
            messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
            return
        else:
            sql_statement = "DELETE FROM notes_table where notes_title ='%s'" %(notes_title)
            ent_delete_note_title.delete(0, 'end')
        
        #Execute the query
        cur.execute(sql_statement)
        messagebox.showinfo(message="Note(s) Deleted")
        con.commit()

    def delete_all_notes():
        """
        Delete all notes from DB
        Return: nothing
        """ 
        con = sql.connect('pin_your_note.db')
        cur = con.cursor()

        #Ask if user wants to delete all notes
        choice = messagebox.askquestion(message="Do you want to delete all notes?")
        #If yes is selected, delete all
        if choice == 'yes':
            sql_statement = "DELETE FROM notes_table"         
        
        #Execute the query
        cur.execute(sql_statement)
        messagebox.showinfo(message="All Notes Deleted")
        con.commit()

    def search_notes():
        """
        Delete all notes from DB
        Return: nothing
        """ 
        con = sql.connect('pin_your_note.db')
        cur = con.cursor()

        #Obtain all the user input
        notes_title = ent_search_note_title.get()
        #If no input is given, retrieve all notes
        if (len(notes_title)<=0):
            messagebox.showerror(message = "ENTER NOTE TITLE" )              
        elif (len(notes_title)>0):
            sql_statement = "SELECT * FROM notes_table where notes_title ='%s'" %notes_title       
              
        #Execute the query
        cur.execute(sql_statement)
        #Obtain all the contents of the query
        row = cur.fetchall()
        #Check if none was retrieved
        if len(row)<=0:
            messagebox.showerror(message="No note found")
        else:
            #Print the notes
            for i in row:
                messagebox.showinfo(message="Date: "+i[0]+"\nTitle: "+i[1]+"\nNotes: "+i[2])
        cur.execute(sql_statement)
        con.commit()
    
    def search_note_to_update():
        con = sql.connect('pin_your_note.db')
        cur = con.cursor()

        #Obtain all the user input
        notes_title = ent_search_note_to_update_title.get()
        #If no input is given, retrieve all notes
        if (len(notes_title)<=0):
            messagebox.showerror(message = "ENTER NOTE TITLE" )              
        elif (len(notes_title)>0):
            sql_statement = "SELECT * FROM notes_table where notes_title ='%s'" %notes_title       
              
        #Execute the query
        cur.execute(sql_statement)
        #Obtain all the contents of the query
        row = cur.fetchall()                
        #Check if none was retrieved
        if len(row)<=0:
            messagebox.showerror(message="No note found")
        else:            
            note_title = row[0][1]
            note = row[0][2]                                    
            ent_notes_title.insert(0, note_title)
            ent_notes.insert(tk.END, note)        
        cur.execute(sql_statement)
        con.commit()
            
    def update_notes():
        con = sql.connect('pin_your_note.db')
        cur = con.cursor()
        today = date.today()
        note_title_to_update = ent_search_note_to_update_title.get()
        note_title = ent_notes_title.get()
        notes = ent_notes.get("1.0", "end-1c")
        #Check if input is given by the user
        if (len(note_title)<=0) & (len(notes)<=1):
            messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
        #update the note
        else:
            sql_statement = "UPDATE notes_table SET notes = '%s', date = '%s', notes_title = '%s' where notes_title ='%s'" %(notes,today,note_title,note_title_to_update)
            ent_search_note_to_update_title.delete(0, "end")
            clear_note_entries()
        cur.execute(sql_statement)
        con.commit()
        messagebox.showinfo(message="Note Updated")
        

    # Display all widges related to Add Notes when Add Notes button is clicked.
    btn_add_notes.config(command=lambda: display_add_note_widgets())
    btn_view_notes.config(command=lambda: display_view_notes_widgets())    
    btn_delete_notes.config(command=lambda: display_delete_note_widgets())
    btn_update_notes.config(command=lambda: display_update_note_widgets())    

    btn_add.config(command=lambda: add_notes())

    btn_cancel.config(command=lambda: remove_add_note_widgets())

    btn_search.config(command=lambda: search_notes())
    btn_search_note_to_update.config(command=lambda: search_note_to_update())
    btn_delete.config(command=lambda: delete_note())

    btn_delete_all.config(command=lambda: delete_all_notes())

    btn_update.config(command=lambda: update_notes())

if __name__ == "__main__":
    main()
