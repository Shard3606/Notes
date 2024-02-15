import time
Notes = []
Selection = ""

def CreateNote():
    TempNoteName = input("What would you like the name of the note to be?")
    print(str(TempNoteName))
    print('\n')
    NoteText = input("Start writing!")
    #Save Note Text to Database
    time.sleep(3)
    Welcome()

def EditNote():
    global NoteList
    print(str(Notes))
    TempNoteName = input("What note would you like to edit?")
    #Fetch Note list and note, print note, make editable
    time.sleep(3)
    Welcome()

def ViewNote():
    global NoteList
    print(str(Notes))
    TempNoteName = input("What note would you like to view?")
    #Fetch Note list and note, print note

def DeleteNote():
    global NoteList
    print(str(Notes))
    TempNoteName = input("What note would you like to delete?")
    #Fetch Note list and note, print note
    Delete = input("Are you sure you want to delete this note? Write 'Y' if yes and 'N' if no.")
    if Delete == "Y":
        #Delete the note from the database
        print("Deleting...")
        time.sleep(3)
        print("Done!")
        time.sleep(3)
        Welcome()
    elif Delete == "N":
        time.sleep(3)
        Welcome()
    else:
        print("Please make sure you inputted one of the options.")
        time.sleep(3)
        DeleteNote()

def Logout():
    print("Come back soon!")
    time.sleep(3)
    import Passkey

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