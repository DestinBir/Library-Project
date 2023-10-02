# ===============================================
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from datetime import datetime

from .function import *

# ===============================================

data = {'empty': 'empty'}
# ===============================================


def button(name, parent, command):
    btn = tk.Button(parent,
                    text=name,
                    font=('Bold', 12),
                    bg='#1877f2',
                    width=20,
                    height=2,
                    command=command)
    return btn


def choose_folder():
    browser_text.set('loading...')
    folder_path = askdirectory(parent=root, mustexist=True, initialdir='', title='Choose the folder')
    if folder_path:
        browser_text.set('start...')
        print('Folder is successfully choose')
    return folder_path


def command1():
    print(browser_text.get())
    if browser_text.get() == 'Choose the folder':
        path = choose_folder()
        global data
        data = createDataSet(path)
    else:
        start_btn.pack_forget()
        fen_1.pack()
        command3()


def command3():
    global tableau
    compt = 1
    tableau.delete(*tableau.get_children())
    for i in data.keys():
        tableau.insert(parent='', index='end', iid=compt, text=compt,
                       values=(i, str(datetime.today().date())))
        compt += 1


def return_cmd():
    browser_text.set('Choose the folder')
    fen_1.pack_forget()
    start_btn.pack(side=tk.BOTTOM, pady=250)


def return_cmd1():
    fen_2.pack_forget()
    fen_1.pack()


# ===============================================

root = tk.Tk()
root.geometry('900x600')
root.title('Bibliothéque')

main = tk.Frame(root)
main.pack(fill=tk.BOTH, expand=False)

browser_text = tk.StringVar()
title = tk.StringVar()

start_btn = tk.Button(root, textvariable=browser_text, font=('Bold', 12), bg='#1877f2', width=20, height=2,
                      command=lambda: command1())
browser_text.set('Choose the folder')
title.set('Book title')
start_btn.pack(side=tk.BOTTOM, pady=250)
# ++++++++++++++++++++++++++++++++++++++++++++++
fen_1 = tk.Frame(root)
fen_2 = tk.Frame(root)
title_1 = tk.Label(fen_1, text='BIBLIOTHEQUE', font=('Bold', 20))
title_1.grid(columnspan=2, row=0, pady=10, padx=0)
title_1 = tk.Label(fen_2, textvariable=title, font=('Bold', 20))
title_1.grid(columnspan=2, row=0, pady=10, padx=0)
# ---------------------------------------------
return_btn = tk.Button(fen_1, text='<--', font=('Bold', 12), bg='#1877f2', width=3, height=1,
                       command=lambda: return_cmd())
return_btn.grid(columnspan=2, row=5, pady=10, padx=30)
return_btn = tk.Button(fen_2, text='<--', font=('Bold', 12), bg='#1877f2', width=3, height=1,
                       command=lambda: return_cmd1())
return_btn.grid(columnspan=2, row=5, pady=10, padx=30)
# ---------------------------------------------
scroll = ttk.Scrollbar(fen_1)
# ---------------------------------------------
progress_b = ttk.Progressbar(main, orient="horizontal", length=300, mode='determinate')
# ---------------------------------------------
search = tk.Frame(fen_1)
en_1 = tk.Entry(search, font=('', 12))
en_1.grid(column=0, row=0, padx=10)
search_btn = tk.Button(search, text='search to read', font=('', 10), bg='#1877f2', width=17, height=1,
                       command=lambda: searchCmd())
search_btn.grid(column=1, row=0, padx=10)
search.grid(columnspan=2, row=3, pady=10)
# ---------------------------------------------
tableau = ttk.Treeview(fen_1, height=20, yscrollcommand=scroll.set)
tableau['columns'] = ('Titre', 'Last opened')
tableau.column('#0', anchor='center', width=70, minwidth=70)
tableau.column('Titre', anchor='w', width=400, minwidth=400)
tableau.column('Last opened', anchor='center', width=100, minwidth=100)
tableau.heading('#0', text='Numéro', anchor='center')
tableau.heading('Titre', text='Titre', anchor='center')
tableau.heading('Last opened', text='Last opened', anchor='center')

# tableau.bind('<ButtonRelease-1>', command2)



tableau.grid(column=1, row=4, pady=10)

scroll.config(command=tableau.yview)
scroll.grid(column=2, row=4, pady=10, sticky='ns')
# -----------------------------------------------
view_set = tk.Frame(fen_2, height=20)
view_set.grid(column=1, row=4, pady=10)
 
# -------------------------------------------------

root.mainloop()
