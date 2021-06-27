#  STONE PAPER SCISSORS   #
import random
from tkinter import *
root =  Tk()
root.configure(bg="black")
root.geometry('+0+0')
root.title("STONE-PAPER-SCISSOR")
root.resizable(width=False, height=True)

# IMAGES IN THE APP
# CHOICES IMAGE
rockHandphoto = PhotoImage(file = "Images/rock1.gif")
paperHandPhoto = PhotoImage(file = "Images/paper1.gif")
scissorHandphoto = PhotoImage(file = "Images/scissor1.gif")

# graphical images
rockWinPhoto = PhotoImage(file="Images/rock2.gif")
paperWinPhoto = PhotoImage(file= "Images/paper.gif")
scissorWinPhoto = PhotoImage(file="Images/scissor.gif")

rockLosePhoto = PhotoImage(file="Images/rocksad.gif")
paperLosePhoto = PhotoImage(file="Images/papersad.gif")
scissorLosePhoto = PhotoImage(file="Images/scissorsad.gif")


# RESULT IMAGE
winPhoto = PhotoImage(file ="Images/win.gif")
losePhoto = PhotoImage(file ="Images/lose.gif")
tiePhoto = PhotoImage(file ="Images/tie.gif")

# initialization of button
rockHandButton = " "
paperHandButton = " "
scissorHandButton = " "

# decision button
result = PhotoImage(file ="Images/result.gif") 


resultButton = Button(root, image= result )

click =  True

def play():
    global rockHandButton, paperHandButton, scissorHandButton
     #setting image and command for button
    rockHandButton = Button(root, image = rockHandphoto, command= lambda:youPick("ROCK"))
    paperHandButton = Button(root, image = paperHandPhoto, command= lambda:youPick("PAPER"))
    scissorHandButton = Button(root, image = scissorHandphoto, command= lambda:youPick("SCISSOR"))


    rockHandButton.grid(row = 0, column=0 )
    paperHandButton.grid(row = 0, column=1)
    scissorHandButton.grid(row = 0, column=2 )

    root.grid_rowconfigure(1, minsize=50)

    resultButton.grid(row=2, column=0, columnspan=5)

def ComputerPick():
    choice = random.choice(["ROCK","PAPER","SCISSOR"])
    return choice

def youPick(yourchoice):
    global click

    compPick = ComputerPick()

    if click==True:
        if yourchoice=="ROCK":
            
            if compPick=="ROCK":
                rockHandButton.configure(image=rockLosePhoto)
                paperHandButton.configure(image=rockLosePhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                #play()
                click = False
            elif compPick=="PAPER":
                rockHandButton.configure(image=rockLosePhoto)
                paperHandButton.configure(image = paperWinPhoto)
                resultButton.configure(image=losePhoto ) 
                scissorHandButton.grid_forget()
                #play()
                click=False 
            elif compPick=="SCISSOR":
                rockHandButton.configure(image=rockWinPhoto)
                paperHandButton.configure(image=scissorLosePhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                #play()
                click= False      
        elif yourchoice=="PAPER":
            
            if compPick=="ROCK":
                rockHandButton.configure(image=paperWinPhoto)
                paperHandButton.configure(image=rockLosePhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=winPhoto)
                #play()
                click=False
            elif compPick=="PAPER":
                rockHandButton.configure(image=paperLosePhoto)
                paperHandButton.configure(image=paperLosePhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=tiePhoto)
                #play()
                click=False
            elif compPick=="SCISSOR":
                rockHandButton.configure(image=paperLosePhoto)
                paperHandButton.configure(image=scissorWinPhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=losePhoto)
                #play()
                click = False

        if yourchoice=="SCISSOR":
            
            if compPick =="ROCK":
                rockHandButton.configure(image=scissorLosePhoto)
                paperHandButton.configure(image=rockWinPhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=losePhoto)
                #play()
                click = False
            elif compPick=="PAPER":
                rockHandButton.configure(image=scissorWinPhoto)
                paperHandButton.configure(image=paperLosePhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=winPhoto)
                #play()
                click =False
            elif compPick=="SCISSOR":
                rockHandButton.configure(image=scissorLosePhoto)
                paperHandButton.configure(image=scissorLosePhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image= tiePhoto)
                #play()
                click = False
    else: 
        if yourchoice=="ROCK" or yourchoice=="PAPER" or yourchoice=="SCISSOR":
            rockHandButton.configure(image=rockHandphoto)
            paperHandButton.configure(image=paperHandPhoto)
            scissorHandButton.configure(image=scissorHandphoto) 
            resultButton.configure(image= result)

            #scissorHandButton.grid(row=0, column=2)
            click = True 
            play()
play()
root.mainloop()            

             