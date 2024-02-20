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
    if TempNoteName == str("Back"):
        Welcome()
    print(str(TempNoteName))
    print('\n')
    NoteText = input("Start writing!")
    if Note1 == ["NoteName", "NoteText"]:
        Note1[1] = str(TempNoteName)
        Note1[2] = str(NoteText)
        print("Saving note...")
    elif Note2 == ["NoteName", "NoteText"]:
        Note2[1] = str(TempNoteName)
        Note2[2] = str(NoteText)
        print("Saving note...")
    elif Note3 == ["NoteName", "NoteText"]:
        Note3[1] = str(TempNoteName)
        Note3[2] = str(NoteText)
        print("Saving note...")
    elif Note4 == ["NoteName", "NoteText"]:
        Note4[1] = str(TempNoteName)
        Note4[2] = str(NoteText)
        print("Saving note...")
    elif Note5 == ["NoteName", "NoteText"]:
        Note5[1] = str(TempNoteName)
        Note5[2] = str(NoteText)
        print("Saving note...")
    else:
        print("Out of space, please delete a note to continue.")
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
    if Note1 != ["NoteName", "NoteText"]:
        print(Note1[1])
    if Note2 != ["NoteName", "NoteText"]:
        print(Note2[1])
    if Note3 != ["NoteName", "NoteText"]:
        print(Note3[1])
    if Note4 != ["NoteName", "NoteText"]:
        print(Note4[1])
    if Note5 != ["NoteName", "NoteText"]:
        print(Note5[1])
    NoteSelection = input("Please input the name of the note you would like to edit, or input 'Back' to go back.")
    if NoteSelection == Note1Name:
        NewText = input(Note1[2])
        Note1[2] = NewText
    elif NoteSelection == Note2Name:
        NewText = input(Note2[2])
        Note2[2] = NewText
    elif NoteSelection == Note3Name:
        NewText = input(Note3[2])
        Note3[2] = NewText
    elif NoteSelection == Note4Name:
        NewText = input(Note4[2])
        Note4[2] = NewText
    elif NoteSelection == Note5Name:
        NewText = input(Note5[2])
        Note5[2] = NewText
    elif NoteSelection == "Back":
        Continue = ""
    else:
        print("Please make sure to write one of the valid note names.")
        time.sleep(3)
        EditNote()
    #Fetch Note list and note, print note, make editable
    time.sleep(3)
    Welcome()

def ViewNote():
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
    if Note1 != ["NoteName", "NoteText"]:
        print(Note1[1])
    if Note2 != ["NoteName", "NoteText"]:
        print(Note2[1])
    if Note3 != ["NoteName", "NoteText"]:
        print(Note3[1])
    if Note4 != ["NoteName", "NoteText"]:
        print(Note4[1])
    if Note5 != ["NoteName", "NoteText"]:
        print(Note5[1])
    NoteSelection = input("Please input the name of the note you would like to view, or input 'Back' to go back.")
    if NoteSelection == Note1Name:
        print(Note1[2])
        Back = input("Input anything when you are done viewing.")
    elif NoteSelection == Note2Name:
        print(Note2[2])
        Back = input("Input anything when you are done viewing.")
    elif NoteSelection == Note3Name:
        print(Note3[2])    
        Back = input("Input anything when you are done viewing.")
    elif NoteSelection == Note4Name:
        print(Note4[2])
        Back = input("Input anything when you are done viewing.")
    elif NoteSelection == Note5Name:
        print(Note5[2])
        Back = input("Input anything when you are done viewing.")
    elif NoteSelection == "Back":
        Continue = ""
    else:
        print("Please make sure to write one of the valid note names.")
        time.sleep(3)
        ViewNote()
    #Fetch Note list and note, print note
    time.sleep(3)
    Welcome()

def DeleteNote():
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
    if Note1 != ["NoteName", "NoteText"]:
        print(Note1[1])
    if Note2 != ["NoteName", "NoteText"]:
        print(Note2[1])
    if Note3 != ["NoteName", "NoteText"]:
        print(Note3[1])
    if Note4 != ["NoteName", "NoteText"]:
        print(Note4[1])
    if Note5 != ["NoteName", "NoteText"]:
        print(Note5[1])
    NoteSelection = input("Please input the name of the note you would like to delete, or input 'Back' to go back.")
    if NoteSelection == Note1Name:
        print(Note1[2])
        Sure = input("Are you sure you want to delete this note? Input N for no and Y for yes.")
        if Sure == "Y":
            Note1 = ["NoteName", "NoteText"]
            print("Deleting note...")
        elif Sure == "N":
            Continue = ""
    elif NoteSelection == Note2Name:
        print(Note2[2])
        Sure = input("Are you sure you want to delete this note? Input N for no and Y for yes.")
        if Sure == "Y":
            Note2 = ["NoteName", "NoteText"]
            print("Deleting note...")
        elif Sure == "N":
            Continue = ""
    elif NoteSelection == Note3Name:
        print(Note3[2])
        Sure = input("Are you sure you want to delete this note? Input N for no and Y for yes.")
        if Sure == "Y":
            Note3 = ["NoteName", "NoteText"]
            print("Deleting note...")
        elif Sure == "N":
            Continue = ""
    elif NoteSelection == Note4Name:
        print(Note4[2])
        Sure = input("Are you sure you want to delete this note? Input N for no and Y for yes.")
        if Sure == "Y":
            Note4 = ["NoteName", "NoteText"]
            print("Deleting note...")
        elif Sure == "N":
            Continue = ""
    elif NoteSelection == Note5Name:
        print(Note5[2])
        Sure = input("Are you sure you want to delete this note? Input N for no and Y for yes.")
        if Sure == "Y":
            Note5 = ["NoteName", "NoteText"]
            print("Deleting note...")
        elif Sure == "N":
            Continue = ""
    elif NoteSelection == "Back":
        Continue = ""
    else:
        print("Please make sure to write one of the valid note names.")
        time.sleep(3)
        ViewNote()
    #Fetch Note list and note, print note
    time.sleep(3)
    Welcome()

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