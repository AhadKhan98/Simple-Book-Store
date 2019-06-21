from tkinter import *
import backend



def create_ui():
    """
    Sets up the GUI
    """
    def viewall_command():
        listbox.delete(0,END)
        for item in backend.view():
            listbox.insert(END,item)

    def search_command():
        listbox.delete(0,END)
        for item in backend.search(entry_title_value.get(),entry_author_value.get(),entry_year_value.get(),entry_isbn_value.get()):
            listbox.insert(END,item)

    def add_command():
        backend.insert(entry_title_value.get(),entry_author_value.get(),entry_year_value.get(),entry_isbn_value.get())
        listbox.delete(0,END)
        listbox.insert(END,(entry_title_value.get(),entry_author_value.get(),entry_year_value.get(),entry_isbn_value.get()))

    def delete_command():
        entry_isbn.delete(0,END)
        entry_year.delete(0,END)
        entry_title.delete(0,END)
        entry_author.delete(0,END)
        backend.delete(selected_item[0])
        viewall_command()

    def update_command():
        backend.update(selected_item[0],entry_title_value.get(),entry_author_value.get(),entry_year_value.get(),entry_isbn_value.get())
        viewall_command()

    def get_selected_row(event):
        try:
            global selected_item
            index = listbox.curselection()[0]
            selected_item = listbox.get(index)
            entry_title.delete(0,END)
            entry_title.insert(END,selected_item[1])
            entry_author.delete(0,END)
            entry_author.insert(END,selected_item[2])
            entry_year.delete(0,END)
            entry_year.insert(END,selected_item[3])
            entry_isbn.delete(0,END)
            entry_isbn.insert(END,selected_item[4])
        except IndexError:
            pass


    window = Tk()

    window.wm_title("Simple Book Store")

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

    listbox.bind('<<ListboxSelect>>',get_selected_row)

    viewall_button = Button(window,text="View All",width=12,command=viewall_command)
    viewall_button.grid(row=2,column=3)

    search_button = Button(window,text="Search Entry",width=12,command=search_command)
    search_button.grid(row=3,column=3)

    add_button = Button(window,text="Add Entry",width=12,command=add_command)
    add_button.grid(row=4,column=3)

    update_button = Button(window,text="Update Selection",width=12,command=update_command)
    update_button.grid(row=5,column=3)

    delete_button = Button(window,text="Delete Selection",width=12,command=delete_command)
    delete_button.grid(row=6,column=3)

    close_button = Button(window,text="Close",width=12,command=window.destroy)
    close_button.grid(row=7,column=3)

    window.mainloop()
