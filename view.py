import funcs
import pandas as pd

import os
if os.stat('notes/notes.csv').st_size == 0:
    notes = pd.DataFrame
else:
    notes = pd.read_csv('notes/notes.csv')

def view(notes=notes):
    action = input('chose action: read_all  read   create   remove   edit   \n')
    if action == 'create': 
        funcs.create(notes)

    elif action == 'read':
        search = input('Search by id or Title? ')
        if search =='id':
            funcs.id_reader(notes)
        elif search =='Title':
            funcs.title_reader(notes)
        else: 
            print('Error')

    elif action == 'remove': 
        search = input('remove by id or Title? ')
        if search =='id':
            funcs.del_by_id(notes)
        elif search =='Title':
            funcs.del_by_title(notes)
        else: 
            print('Error')

    elif action =='edit': 
        act = input('Change Text or Title? ')
        search = input('What id of note? ')
        if act =='Text':
            funcs.edit_data(notes, search)
        elif act =='Title':
            funcs.edit_title(notes, search)
        else: 
            print('Error')

    elif action == 'read_all':
        print(notes)

    else: 
        print('Hello')