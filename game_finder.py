# The "pass" command tells Python to "do nothing".  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import json

from tkinter import *

class ProgramGUI:
   
    ticketInformation = ""
    def __init__(self):
        
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of game_finder.py" section of the assignment brief.
        global no_player
        global time_available
        global age_player
        global gameNameVar

        root = Tk()
        root.title("Game Finder")
        root.geometry('310x200+350+320')
        gameNameVar = StringVar()
        
        heading = Label(root , text="Constraints :",fg="blue",font=14)
        no_player = Label(root, text="Number of players :")
        time_available = Label(root, text="Time available (mins) :")
        age_player = Label(root, text="Age of youngest player :")
        
        heading.grid(row=0 , column=1)
        no_player.grid(row=1,column=0)
        time_available.grid(row=2,column=0)
        age_player.grid(row=3,column=0)

        no_player = Entry(root)
        time_available = Entry(root)
        age_player = Entry(root)

        no_player.grid(row=1, column=1 ,ipadx="5")
        time_available.grid(row=2, column=1, ipadx="5")
        age_player.grid(row=3, column=1, ipadx="5")

        submit = Button(root,text = "Submit" ,command =self.findGames)
        submit.grid(row=8, column=1)

        # -------- Button -------   
            
        heading1 = Label(root , text="Matching Games:",fg="blue",font=14)
        heading1.grid(row=10 , column=1)
        
        gameName = Button(root,text = "Game name" ,width=20, textvariable=gameNameVar )
        gameName.grid(row=11, column=1)
        ticketToRide = Button(root,text = "Ticket to Ride" ,width=20,command =self.ticketToRideMessage)
        ticketToRide.grid(row=12, column=1)
        root.mainloop()
  
    def findGames(self):
        read_file=open("data.txt","r")
        self.data1=(read_file.read())
        self.data=json.loads(self.data1)

        global ticketInformation
        
        if (no_player.get() == "" and time_available.get() == "" and age_player.get() == ""):
            print("empty input")
        else:
            playerCount,gameDuration,gameMinAge=int(no_player.get()),int(time_available.get()),int(age_player.get())
            for ele,i in enumerate(self.data):
                if (playerCount > int(i['min_players']) and playerCount < int(i['max_players'])):
                    if int(i['duration']) <= gameDuration:
                        if int(i['min_age']) <= gameMinAge:
                            gameNameVar.set(i['name'])
                            #print(i['name'])
                            ticketInformation = "Ticket to Ride\nPlayer: "+str(i['min_players'])+" - "+str(i['max_players'])+"\nDuration: "+str(i['duration'])+"\nMinimum Age: "+str(i['min_age'])
                        break
    def close(self):
        ProgrameGUI().destroy()
        self.entry.delete(0, 'end')
   
    def ticketToRideMessage(self):
        global ticketInformation
        #print(ticketInformation)
        tkinter.messagebox.showinfo("Ticket to Ride",ticketInformation)
   
        # This method finds and displays games matching the criteria entered by the user.
        # See the "The findGames() Method of the GUI Class of game_finder.py" section of the assignment brief.
         
# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
