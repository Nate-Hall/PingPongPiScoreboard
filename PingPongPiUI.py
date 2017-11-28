from tkinter import *
from tkinter import ttk
from tkinter import font
from PingPongPiScoreboard import *
from datetime import datetime

pScores = [0, 0]

def assignVars():
	pScores = getScores()
	playerScore0.set(str(pScores[0]))
	playerScore1.set(str(pScores[1]))

	server = getServer()
	if(server > -1):
		if(server == 0):
			f0.configure(underline = True)
			f1.configure(underline = False)
		elif(server == 1):
			f0.configure(underline = False)
			f1.configure(underline = True)
	else:
		f0.configure(underline = False)
		f1.configure(underline = False)

root = Tk()
root.title("Ping Pong Pi")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

playerName0 = StringVar()
playerName1 = StringVar()
playerScore0 = StringVar()
playerScore1 = StringVar()

playerName0.set("Player 1")
playerName1.set("Player 2")
playerScore0.set("0")
playerScore1.set("0")

f = font.Font(size = int(mainframe.winfo_screenwidth()/30))
f0 = font.Font(size = int(mainframe.winfo_screenwidth()/10))
f1 = font.Font(size = int(mainframe.winfo_screenwidth()/10))

playerName0Label = ttk.Label(mainframe, textvariable=playerName0, font=f)
playerName1Label = ttk.Label(mainframe, textvariable=playerName1, font=f)
playerScore0Label = ttk.Label(mainframe, textvariable=playerScore0, font=f0)
playerScore1Label = ttk.Label(mainframe, textvariable=playerScore1, font=f1)

playerName0Label.grid(column=2, row=2)
playerName1Label.grid(column=4, row=2)
playerScore0Label.grid(column=2, row=4)
playerScore1Label.grid(column=4, row=4)

playerName0Label.place(relx=0.5, rely=0.5, anchor=CENTER)
playerName1Label.place(relx=0.5, rely=0.5, anchor=CENTER)
playerScore0Label.place(relx=0.5, rely=0.5, anchor=CENTER)
playerScore1Label.place(relx=0.5, rely=0.5, anchor=CENTER)

for child in mainframe.winfo_children(): child.grid_configure(padx=mainframe.winfo_screenwidth()/6, pady=mainframe.winfo_screenheight()/6)

root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

def mainTasks():
    checkButtons()
    root.after(20, assignVars)

    if(checkWinner() != False):
        if(getScores()[0] > getScores()[1]):
        	playerName0Label.configure(background='blue')
        else:
        	playerName1Label.configure(background='red')
    else:
    	playerName0Label.configure(background=root.cget("background"))
    	playerName1Label.configure(background=root.cget("background"))

    root.after(20, mainTasks)

root.after(20, mainTasks)
root.mainloop()