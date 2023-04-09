import pandas as pd
import datetime




def save(notes):
    cond = input('To save push 1, else push 0: ')
    if (cond == '1'):
        notes.to_csv('notes/notes.csv')
        print('Saved')
    else:
        print('Exit')


def del_by_id(notes):
    if notes.empty == False:
        id = int(input('id: '))
        print('Delete: ')
        print(notes.iloc[id])
        notes = notes.drop(index = id)
        notes.to_csv('notes/notes.csv')
    else:
        print('empty')


def del_by_title(notes):
    if notes.empty == False:
        title = input('Title: ')
        id = notes[notes['Title'] == title].index
        notes.drop(index = id)
        notes.to_csv('notes/notes.csv')
    else:
        print('empty')



def create(notes):
    print('------Create new note-----')
    title = input("Title: ")
    core = input("Text: ")
    nt = {'Title': title, 'Text': core, 'Time': pd.to_datetime(datetime.datetime.now())}
    if notes.empty:
        note = pd.DataFrame(nt, index=[0])
        save(note)
    else:
        notes = notes.append(nt, ignore_index=True)
        save(notes)


def edit_data(notes, id):
    if notes.empty == False:
        new_text = input("new text: ")
        notes[id, 2] = new_text
        notes[id, 3] = pd.to_datetime(datetime.datetime.now())
        save(notes)
    else:
        print('empty')



def edit_title (notes, id):
    if notes.empty == False:
        new_title = input(('new title:'))
        notes[id, 1] = new_title
        notes[id, 3] = pd.to_datetime(datetime.datetime.now())
        save(notes)
    else:
        print('empty')


def id_reader(notes):
    if notes.empty == False:
        id = int(input('id: '))
        print(notes.iloc[id])
    else:
        print('empty')


def title_reader(notes):
    if notes.empty == False:
        title = input('Title: ')
        print(notes.loc[notes['Title'] == title])
    else:
        print('empty')


