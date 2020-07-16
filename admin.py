
# Import the json module to allow us to read and write data in JSON format.
import json
import ast
import os
# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
# CSP5110 Requirement: Also enforce a minimum value of 1. See assignment brief.
min_players,max_players,duration,min_age = 0,0,0,0
name = "";
def inputInt(inputString):
    inputData = int(input(inputString))
    return inputData

# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def inputSomething(inputString):
    inputTempData = input(inputString)
    inputData = inputTempData.strip()
    return inputData

# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def saveData():
    fileData = readData()
    if fileData == "":
        fileData = []
    fileData.append({'name':name,'min_players':min_players,'max_players':max_players,'duration':duration,'min_age':min_age})
    writeData(fileData)
    print("Game added.")
    return
    
def readData():
    readFile=open("data.txt","r")
    fileDataByLine=(readFile.read())
    fileData = ast.literal_eval(fileDataByLine)
    tempData = json.dumps(fileData)
    return json.loads(tempData)

def writeData(data):
    jsonFinalData = json.dumps(data)
    f=open("data.txt","w")
    f.write(str(jsonFinalData))
    f.close()
    return
        
# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Details of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Game Finder Admin Program.')
while True: 
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    fileData = readData()
    choice = input('> ').lower()
    if choice == 'a':
        # Add a new game.
        # See Point 3 of the "Details of admin.py" section of the assignment brief.
        name = inputSomething("Name of game: ")
        min_players = inputInt("Minimum number of players: ")
        max_players = inputInt("Maximum number of players: ")
        duration = inputInt("Average duration of game in minutes: ")
        min_age= inputInt("Minimum recommended player age: ")
        saveData()
                  
    elif choice == 'l':
        # List the current games.
        # See Point 4 of the "Details of admin.py" section of the assignment brief.
        if len(fileData) == 0:
            print("No Games Saved")
        else:
            print("List of games:")        
            for serialNumber,i in enumerate(fileData):
                print(str(serialNumber)+") "+i['name'])
                
    elif choice == 's':
        # Search the current games.
        # See Point 5 of the "Details of admin.py" section of the assignment brief.
        if len(fileData) == 0:
            print("No Games Saved")
        else:
            gameName=inputSomething("Type a game name to search for: ")
            print("Search results:")
            for number,i in enumerate (fileData):
                if gameName.lower() in i['name'].lower():
                    print(str(number)+") "+i['name'])
            
    elif choice == 'v':
        # View a game.
        # See Point 6 of the "Details of admin.py" section of the assignment brief.
         if len(fileData) == 0:
            print("No Games Saved")
         else:
            gameNumber = inputInt("Game number to view: ")
            for number,i in enumerate(fileData):
                if number == gameNumber:
                    print(i['name'])
                    print("Players: "+str(i['min_players'])+" - "+str(i['max_players']))
                    print("Duration: "+str(i['duration'])+" minutes")
                    print("Minimum Age: "+str(i['min_age']))
   
    elif choice == 'd':
        # Delete a game.
        # See Point 7 of the "Details of admin.py" section of the assignment brief.
        if len(fileData) == 0:
            print("No Games Saved")
        else:
            gameNumberToDelete=inputInt("Game number to delete: ")
            isBreak = False
            isGameFound = False
            for number,i in enumerate (fileData):
                if number == gameNumberToDelete:
                    del fileData[number]
                    writeData(fileData)
                    print("Game deleted.")
                    isBreak = True
                    isGameFound = True
                if isBreak == True:
                    break 
            if isGameFound == False:
                print("Invalid Index Number")
                            
    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Details of admin.py" section of the assignment brief.
        print("Goodbye!")
        os._exit(0)
    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Details of admin.py" section of the assignment brief.
        print("Please enter the valid choice.")
