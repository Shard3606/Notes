import time
Notes = []
Selection = ""
Note1 = ["NoteName", "NoteText"]
Note2 = ["NoteName", "NoteText"]
Note3 = ["NoteName", "NoteText"]
Note4 = ["NoteName", "NoteText"]
Note5 = ["NoteName", "NoteText"]

def CreateNote():
    global Note1
    global Note2
    global Note3
    global Note4
    global Note5
    TempNoteName = input("What would you like the name of the note to be? Or input 'Back' to go back.")
    if TempNoteName = str("Back")
        Welcome()
    print(str(TempNoteName))
    print('\n')
    NoteText = input("Start writing!")
    if Note1 = ["NoteName", "NoteText"]
        Note1[1] = str(TempNoteName)
        Note1[2] = str(NoteText)
        print("Saving note...")
        time.sleep(3)
        Welcome()
    elif Note2 = ["NoteName", "NoteText"]
        Note2[1] = str(TempNoteName)
        Note2[2] = str(NoteText)
        print("Saving note...")
        time.sleep(3)
        Welcome()
    elif Note3 = ["NoteName", "NoteText"]
        Note3[1] = str(TempNoteName)
        Note3[2] = str(NoteText)
        print("Saving note...")
        time.sleep(3)
        Welcome()
    elif Note4 = ["NoteName", "NoteText"]
        Note4[1] = str(TempNoteName)
        Note4[2] = str(NoteText)
        print("Saving note...")
        time.sleep(3)
        Welcome()
    elif Note5 = ["NoteName", "NoteText"]
        Note5[1] = str(TempNoteName)
        Note5[2] = str(NoteText)
        print("Saving note...")
        time.sleep(3)
        Welcome()
    else:
        print("Out of space, please delete a note to continue.")
        time.sleep(3)
        Welcome()
    #Save Note Text to Database
    time.sleep(3)
    Welcome()

def EditNote():
    global NoteList
    global Note1
    global Note2
    global Note3
    global Note4
    global Note5
    Note1[1] = Note1Name
    Note2[1] = Note2Name
    Note3[1] = Note3Name
    Note4[1] = Note4Name
    Note5[1] = Note5Name
    print(str(Notes))
    TempNoteName = input("What note would you like to edit?")
    if Note1 != ["NoteName", "NoteText"]
        print(Note1[1])
    if Note2 != ["NoteName", "NoteText"]
        print(Note2[1])
    if Note3 != ["NoteName", "NoteText"]
        print(Note3[1])
    if Note4 != ["NoteName", "NoteText"]
        print(Note4[1])
    if Note5 != ["NoteName", "NoteText"]
        print(Note5[1])
    print("Please input the name of the note you would like to edit, or input 'Back' to go back.")
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
