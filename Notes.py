import time
import Passkey
Notes = []
Selection = ""

def CreateNote():
    TempNoteName = input("What would you like the name of the note to be?")
    print(str(TempNoteName))
    print('\n')
    NoteText = input("Start writing!")
    #Save Note Text to Database
    Welcome()

def EditNote():
    global NoteList
    print(str(Notes))
    TempNoteName = input("What note would you like to edit?")
    #Fetch Note
    print(str(NoteText))

def ViewNote():
    global NoteList
    print(str(Notes))
    TempNoteName = input("What note would you like to view?")

def DeleteNote():
    global NoteList
    print(str(Notes))
    TempNoteName = input("What note would you like to delete?")

def Logout():
    print("Come back soon!")
    Passkey.run(["python", "other.py"])

def Welcome():
    global Selection
    print("Welcome to your Notes!")
    Selection = input("Write 'C' if you would like to create a note," '\n'
                  "write 'E' if you would like to edit an existing note," '\n'
                  "write 'V' if you would like to view an existing note," '\n'
                  "write 'D' if you would like to delete an existing note," '\n'
                  "or write 'L' if you would like to log out.")
    if Selection == "C":
        CreateNote()
    elif Selection == "E":
        EditNote()
    elif Selection == "V":
        ViewNote()
    elif Selection == "D":
        DeleteNote()
    elif Selection == "L":
        Logout()
    else:
        "Please make sure to input one of the available options."
        time.sleep(3)
        Welcome()

Welcome()