from tkinter import *

def create_ui():
    """
    Sets up the GUI
    """

    window = Tk()

    label_title = Label(window,text="Title")
    label_title.grid(row=0,column=0)

    label_author = Label(window,text="Author")
    label_author.grid(row=0,column=2)

    label_year = Label(window,text="Year")
    label_year.grid(row=1,column=0)

    label_isbn = Label(window,text="ISBN")
    label_isbn.grid(row=1,column=2)

    entry_title_value = StringVar()
    entry_title = Entry(window,textvariable=entry_title_value)
    entry_title.grid(row=0,column=1)

    entry_author_value = StringVar()
    entry_author = Entry(window,textvariable=entry_author_value)
    entry_author.grid(row=0,column=3)

    entry_year_value = StringVar()
    entry_year = Entry(window,textvariable=entry_year_value)
    entry_year.grid(row=1,column=1)

    entry_isbn_value = StringVar()
    entry_isbn = Entry(window,textvariable=entry_isbn_value)
    entry_isbn.grid(row=1,column=3)

    listbox = Listbox(window,height=6,width=35)
    listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

    scrollbar = Scrollbar(window)
    scrollbar.grid(row=2,column=2,rowspan=6)

    # Connecting scrollbar to control listbox's y axis
    listbox.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=listbox.yview)

    viewall_button = Button(window,text="View All",width=12)
    viewall_button.grid(row=2,column=3)

    search_button = Button(window,text="Search Entry",width=12)
    search_button.grid(row=3,column=3)

    add_button = Button(window,text="Add Entry",width=12)
    add_button.grid(row=4,column=3)

    update_button = Button(window,text="Update",width=12)
    update_button.grid(row=5,column=3)

    delete_button = Button(window,text="Delete",width=12)
    delete_button.grid(row=6,column=3)

    close_button = Button(window,text="Close",width=12)
    close_button.grid(row=7,column=3)

    window.mainloop()
