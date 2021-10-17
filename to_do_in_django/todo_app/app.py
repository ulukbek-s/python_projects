from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('todo')
root.geometry('500x500')

my_font = Font(
    family='Bell MT',
    size=30,
    weight="bold",
)

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(
    my_frame,
    font=my_font,
    width=25,
    height=5,
    bg='Grey',
    fg="#464646",
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
)
my_list.pack(side=LEFT, fill=BOTH)

stuff = ['wash', 'clean']
for item in stuff:
    my_list.insert(END, item)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=('Bell MT', 30))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

delete_buttton = Button(button_frame, text='Delete item', command=delete_item)
add_buttton = Button(button_frame, text='Add item', command=add_item)

delete_buttton.grid(row=0, column=0)
add_buttton.grid(row=0, column=1, padx=20)

root. mainloop()