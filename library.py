from tkinter import *
import backend

def get_selected_row(event): 
    try:

        global selected_tlist
        index = list1.curselection()[0]
        selected_tlist = list1.get(index)
        
        # Displays selected books info in entry fields
        e1.delete(0, END)
        e1.insert(END,selected_tlist[1])
        e2.delete(0, END)
        e2.insert(END,selected_tlist[2])
        e3.delete(0, END)
        e3.insert(END,selected_tlist[3])
        e4.delete(0, END)
        e4.insert(END,selected_tlist[4])
    except IndexError:
        pass
    



def view_command():
    list1.delete(0, END)
    for row in backend.all_Books():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(Title_text.get(), Year_text.get(), Author_text.get(), ISBN_text.get()):
        list1.insert(END, row)


def add_command():
    backend.add_Book(Title_text.get(), Year_text.get(), Author_text.get(), ISBN_text.get())
    list1.delete(0, END)
    list1.insert(END,(Title_text.get(), Year_text.get(), Author_text.get(), ISBN_text.get()))
    

def delete_command():
   
    backend.delete_Book(selected_tlist[0])

def update_command():
   
    backend.update_List(selected_tlist[0], Title_text.get(), Year_text.get(), Author_text.get(), ISBN_text.get())



window = Tk()

window.wm_title("Cj's Library")


# GUI UI LABELS

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Year")
l2.grid(row = 1, column = 0)

l3 = Label(window, text = "Author")
l3.grid(row = 0, column = 2)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)


#GUI ENTRIES 

Title_text = StringVar()
e1 = Entry(window, textvariable = Title_text)
e1.grid(row = 0, column = 1)

Year_text = StringVar()
e2 = Entry(window, textvariable = Year_text)
e2.grid(row = 1, column = 1)

Author_text = StringVar()
e3 = Entry(window, textvariable = Author_text)
e3.grid(row = 0, column = 3)

ISBN_text = StringVar()
e4 = Entry(window, textvariable = ISBN_text)
e4.grid(row = 1, column = 3)

# LISTBOX 

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

# SCROLLBAR

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6 )

list1.configure(yscrollcommand = sb1.set) # sets scrollbar to conrol listbox
sb1.configure(command = list1.yview) # slides the screen within listbox

list1.bind('<<ListboxSelect>>', get_selected_row) #selects row of book to delete

#BUTTONS

b1 = Button(window, text = "All Books", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add Book", width = 12, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update List", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete Book", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)


window.mainloop()