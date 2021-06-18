from tkinter import *
from tkinter import Radiobutton
from tkinter import messagebox
import random
import time

win = Tk()
window = ""

cghighscore = 0
qghighscore = 0
wthighscore = 0

def Animation(variable, xpos, ypos, endx, endy, steps):
    for i in range(0,steps,1):
        xchange = (endx-xpos)/15
        xpos += round(xchange,2)
        ychange = (endy-ypos)/15
        ypos += round(ychange,2)
        variable.place(x=xpos, y=ypos)
        variable.update()
        time.sleep(0.01)
    variable.place(x=endx, y=endy)

def quizgame():
    global QnA, qi, nq, score, window
    window = "QuizGame"
    QnA = [["1.When was Minecraft released?", "1. 2005", "2. 2009", "3. 2011", "4. 2013", 2], ["2.When was Undertale released?", "1. 2013", "2. 2014", "3. 2015", "4. 2016", 3],["3.What are the latest Windows?", "1. 9", "2. 10", "3. 11", "4. 12", 2],["4.Which of the following is the worst?", "1. Windows", "2. Mac", "3. Linux", "4. None of the above", 2],["What number is this question?", "1. 3", "2. 4", "3. 5", "4. 6", 3]]
    qi = 0
    nq = True
    score = 0
    win.title("Quiz Game")
    Screen("Clear")

    def DeleteWindowQ(f):
        global question, answer1, answer2, answer3, answer4, lblscore, backbtn, highscorelbl, playagainbtn

        question.destroy()
        answer1.destroy()
        answer2.destroy()
        answer3.destroy()
        answer4.destroy()
        lblscore.destroy()
        backbtn.destroy()
        playagainbtn.destroy()
        highscorelbl.destroy()

        if f == 0:
            Screen("Home")
        elif f == 1:
            quizgame()

    def SetUpScreen():
        global question, answer1, answer2, answer3, answer4, lblscore, image, answer, highscorelbl, qghighscore, progressbar, style, progr
        question = Label(win, font=("Comic Sans", 20))
        question.grid(column=0, row=2, columnspan=2)
        answer = IntVar()
        progr = IntVar()
        progr.set(0)
        answer1 = Radiobutton(win, font=("Comic Sans", 20),  value=1, variable= answer)
        answer1.grid(column=0, row=3, columnspan=2)
        answer2 =Radiobutton(win, font=("Comic Sans", 20),  value=2, variable= answer)
        answer2.grid(column=0, row=4, columnspan=2)
        answer3 = Radiobutton(win, font=("Comic Sans", 20),  value=3, variable= answer)
        answer3.grid(column=0, row=5, columnspan=2)
        answer4 = Radiobutton(win, font=("Comic Sans", 20),  value=4, variable= answer)
        answer4.grid(column=0, row=6, columnspan=2)
        lblscore = Label(win, text="Score: " + str(score), font=("Comic Sans", 20))
        lblscore.grid(column=0, row=1)
        #progressbar = Progressbar(win, length = 5, style = 'black.Horizontal.TProgressbar', variable = progr)
        #progressbar.grid(column=0, row=0)
        highscorelbl = Label(text="HighScore:" + str(qghighscore), font=("Comic Sans", 20))
        highscorelbl.grid(column=1, row=1)

    SetUpScreen()

    def CheckAnswer(*args):
        global QnA, qi, nq, score, answer, highscorelbl, qghighscore, backbtn, playagainbtn, progressbar, progr
        a = answer.get()
        if qi < 5:
            if a == QnA[qi][5]:
                nq = True
                score += 5
                qi += 1
                progr.set(qi)
            elif score > 0:
                    score -= 1
            lblscore.config(text="Score: " + str(score), font=("Comic Sans", 20))
            Mainloop()
        if qi == 5:
            question.destroy()
            answer1.destroy()
            answer2.destroy()
            answer3.destroy()
            answer4.destroy()
            #progressbar.destroy()
            if score > qghighscore:
                qghighscore = score
                highscorelbl.config(text="HighScore:" + str(qghighscore), font=("Comic Sans", 20))
            backbtn = Button(win, text="Back", bg="red", fg="cyan", width=15)
            Animation(backbtn, 200, 500, 200, 300, 100)
            playagainbtn = Button(win, text="Play Again", bg="yellow", fg="green", width=15)
            Animation(playagainbtn, 200, 500, 200, 265, 100)
            backbtn.config(command= lambda: DeleteWindowQ(0))
            playagainbtn.config(command= lambda: DeleteWindowQ(1))

    def SetUpQuestion(*args):
        global qi, question, answer1, answer2, answer3, answer4, answer
        answer.set(0)
        question.configure(text=QnA[qi][0])
        answer1.configure(text=QnA[qi][1])
        answer2.configure(text=QnA[qi][2])
        answer3.configure(text=QnA[qi][3])
        answer4.configure(text=QnA[qi][4])

    def Mainloop(*args):
        global nq, answer, qi
        if nq == True:
            if qi < 5:
                SetUpQuestion()
                nq = False

    answer.trace("w", CheckAnswer)
    Mainloop()

def colourgame():
    global score, timeleft, colours, nextcolorlock, playing, window
    window = "ColourGame"
    Screen("Clear")
    score = 0
    timeleft = 30
    colours = ["Red", "Green", "Blue", "Purple", "Pink", "Black", "Lime", "White", "Yellow", "Orange"]
    nextcolorlock = False
    win.title("Colour Game")
    playing = False

    def DeleteWindowC(f):
        global ruleslbl, scorelbl, timelbl, backbtn, highscorelbl, playagainbtn, playing

        playing = False
        ruleslbl.destroy()
        scorelbl.destroy()
        timelbl.destroy()
        backbtn.destroy()
        playagainbtn.destroy()
        highscorelbl.destroy()

        if f == 0:
            Screen("Home")
        elif f == 1:
            colourgame()

    def SetUpScreen():
        global ruleslbl, scorelbl, timelbl, wordlbl, answertxt, highscorelbl
        ruleslbl = Label(win, text="Write the colour of the text, not the word.", font=("Comic Sans", 20))
        scorelbl = Label(win, text="Press Enter to Begin!", font=("Comic Sans", 20))
        highscorelbl = Label(win, text="HighScore:"+str(cghighscore), font=("Comic Sans", 20))
        timelbl = Label(win, text="Time left: " + str(timeleft), font=("Comic Sans", 20))
        wordlbl = Label(win, text="", font=("Comic Sans", 60))
        answertxt = Entry(win, width=30)
        ruleslbl.grid(column=0, row=0)
        scorelbl.grid(column=0, row=1)
        highscorelbl.grid(column=0, row=2)
        timelbl.grid(column=0, row=3)
        wordlbl.grid(column=0, row=4)
        answertxt.grid(column=0, row=5)

    def CountDown():
        global timeleft, answertxt, wordlbl, score, cghighscore, backbtn, highscorelbl, playagainbtn
        timeleft -= 0.1
        timeleft = round(timeleft, 2)
        timelbl.configure(text="Time left: " + str(timeleft))

        if round(timeleft+0.5) <= 0:
            wordlbl.destroy()
            answertxt.destroy()
            if score > cghighscore:
                cghighscore = score
                highscorelbl.config(text="HighScore:" + str(cghighscore), font=("Comic Sans", 20))
            backbtn = Button(win, text="Back", bg="red", fg="cyan", width=15)
            Animation(backbtn, 200, 500, 200, 300, 100)
            playagainbtn = Button(win, text="Play Again", bg="yellow", fg="green", width=15)
            Animation(playagainbtn, 200, 500, 200, 265, 100)
            backbtn.config(command= lambda: DeleteWindowC(0))
            playagainbtn.config(command= lambda: DeleteWindowC(1))
        else:
            CheckAnswer()
            timelbl.after(100, CountDown)

    def Shuffle():
        global nextcolorlock, score, timeleft
        if nextcolorlock == False:
            nextcolorlock = True
            scorelbl.configure(text="Score: " + str(score))
            random.shuffle(colours)
            wordlbl.configure(fg=str(colours[1]), text=str(colours[0]))

    def CheckAnswer():
        global timelbl, answertxt, score, nextcolorlock

        text = answertxt.get()

        if text.lower() == colours[1].lower():
            nextcolorlock = False
            score += 1
            answertxt.delete(0, 'end')
            Shuffle()

    def Delete(*args):
            answertxt.delete(0, 'end')

    def StartGame(*args):
        global playing
        if playing == False:
            playing = True
            Shuffle()
            timelbl.after(100, CountDown)

    SetUpScreen()
    win.bind("<Return>", StartGame)
    win.bind("<BackSpace>", Delete)

def wordtyper():
    global words, score, timeleft, words, nextwordlock, playing, window, timer, usablewords, wordcount
    window = "WordTyper"
    Screen("Clear")
    score = 0
    timeleft = 30
    words = ["Education", "Since", "When", "Were", "You", "The", "One", "In", "Control", "Hello", "Human", "Life", "Death", "Depth", "Water", "Lava", "Fire", "Ice", "Wear", "Weapons", "Materials", "Sword", "Machine", "Program", "Run", "Check", "Space", "Type", "Extend", "Execute"]
    usablewords = []
    nextwordlock = False
    win.title("Word Typer")
    playing = False
    timer = 0

    def DeleteWindowW(f):
        global ruleslbl, scorelbl, timelbl, backbtn, highscorelbl, playagainbtn, playing

        playing = False
        ruleslbl.destroy()
        scorelbl.destroy()
        timelbl.destroy()
        backbtn.destroy()
        playagainbtn.destroy()
        highscorelbl.destroy()

        if f == 0:
            Screen("Home")
        elif f == 1:
            wordtyper()

    def SetUpScreen():
        global ruleslbl, scorelbl, timelbl, wordlbl, answertxt, highscorelbl
        ruleslbl = Label(win, text="Write the letter you see on screen.", font=("Comic Sans", 20))
        scorelbl = Label(win, text="Press Enter to Begin!", font=("Comic Sans", 20))
        highscorelbl = Label(win, text="HighScore:"+str(wthighscore), font=("Comic Sans", 20))
        timelbl = Label(win, text="Time left: " + str(timeleft), font=("Comic Sans", 20))
        wordlbl = Label(win, text="", font=("Comic Sans", 60))
        answertxt = Entry(win, width=30)
        ruleslbl.grid(column=0, row=0)
        scorelbl.grid(column=0, row=1)
        highscorelbl.grid(column=0, row=2)
        timelbl.grid(column=0, row=3)
        wordlbl.grid(column=0, row=4)
        answertxt.grid(column=0, row=5)

    def CountDown():
        global timeleft, answertxt, wordlbl, score, cghighscore, backbtn, highscorelbl, playagainbtn, timer
        timer += 0.1
        timeleft -= ((round(timer / 20))+1)/10
        timeleft = round(timeleft, 2)
        timelbl.configure(text="Time left: " + str(timeleft))

        if round(timeleft+0.5) <= 0:
            timelbl.configure(text="Time left: 0")
            wordlbl.destroy()
            answertxt.destroy()
            if score > cghighscore:
                cghighscore = score
                highscorelbl.config(text="HighScore:" + str(cghighscore), font=("Comic Sans", 20))
            backbtn = Button(win, text="Back", bg="red", fg="cyan", width=15)
            Animation(backbtn, 200, 500, 200, 300, 100)
            playagainbtn = Button(win, text="Play Again", bg="yellow", fg="green", width=15)
            Animation(playagainbtn, 200, 500, 200, 265, 100)
            backbtn.config(command= lambda: DeleteWindowW(0))
            playagainbtn.config(command= lambda: DeleteWindowW(1))
        else:
            CheckAnswer()
            timelbl.after(100, CountDown)

    def Shuffle():
        global nextwordlock, score, timeleft, usablewords, words
        if nextwordlock == False:
            nextwordlock = True
            scorelbl.configure(text="Score: " + str(score))
            if usablewords.__len__() == 0:
                usablewords = ["Education", "Since", "When", "Were", "You", "The", "One", "In", "Control", "Hello", "Human", "Life", "Death", "Depth", "Water", "Lava", "Fire", "Ice", "Wear", "Weapons", "Materials", "Sword", "Machine", "Program", "Run", "Check", "Space", "Type", "Extend", "Execute"]
            random.shuffle(usablewords)
            wordlbl.configure(text=str(usablewords[0]))

    def CheckAnswer():
        global timelbl, answertxt, score, nextwordlock, timeleft, usablewords, words

        text = answertxt.get()

        if text.lower() == usablewords[0].lower():
            nextwordlock = False
            score += 5
            timeleft += 3
            usablewords.remove(usablewords[0])
            answertxt.delete(0, 'end')
            Shuffle()

    def Delete(*args):
        global score, timeleft, playing
        if playing == True:
            answertxt.delete(0, 'end')
            if score-2 >= 0:
                score -= 2
            timeleft -= 1

    def StartGame(*args):
        global playing
        if playing == False:
            playing = True
            Shuffle()
            timelbl.after(100, CountDown)

    SetUpScreen()
    win.bind("<Return>", StartGame)
    win.bind("<BackSpace>", Delete)

def Checkname(testname):
    global lblname, name
    if len(testname) < 3:
        lblname.config(text="Your name must be longer than 2 characters", font=("Comic Sans", 18))
        win.geometry('500x500')
    elif len(testname) > 11:
        lblname.config(text="Your name must be shorter than 12 characters", font=("Comic Sans", 17))
        win.geometry('500x500')
    else:
        name = testname
        Screen("Home")

def Screen(type):
    global lblname, entname, btnname, name, homewelcome, homebtncg, homebtnqg, homebtnwt, homebtnexit, image, logo, imagelbl, window
    if type == "Clear":
        homewelcome.destroy()
        homebtncg.destroy()
        homebtnqg.destroy()
        homebtnwt.destroy()
        homebtnexit.destroy()
        image.destroy()
        imagelbl.destroy()
    elif type == "NameSelect":
        window = "NameSelect"
        win.title("Logging in")
        win.geometry('500x500')
        entname = Entry(win, width=23, font=("Comic Sans", 30))
        entname.grid(column=0, row=0)
        lblname = Label(win, text="Type your name here", font=("Comic Sans", 25))
        lblname.grid(column=0, row=1, rowspan=2)
        btnname = Button(win, text="Apply", command=lambda: Checkname(entname.get()), font=("Comic Sans", 15), width=20)
        btnname.grid(column=0, row=3)
    elif type == "Home":
        window = "Home"
        win.title("Home Screen")
        win.geometry('500x500')
        lblname.destroy()
        entname.destroy()
        btnname.destroy()
        homewelcome = Label(win, text="Welcome, "+str(name), font=("Comic Sans", 30))
        homewelcome.place(x=375/len(name),y=5)
        homebtncg = Button(win, text="Colour Game", width=10)
        Animation(homebtncg, 0, 500, 150, 300, 75)
        homebtnqg = Button(win, text="Quiz Game", width=10)
        Animation(homebtnqg, 500, 500, 300, 300, 75)
        homebtnwt = Button(win, text="Word Typer", width=10)
        Animation(homebtnwt, 250, 500, 225, 270, 75)
        homebtnexit = Button(win, text="Exit", width=10, command= lambda: messagebox.showerror("No Permission", "You are lacking the permission to execute this command. ;)"))
        Animation(homebtnexit, 225, 500, 225, 350, 75)
        logo = PhotoImage(file="pikachu.png")
        image = Label(win, image=logo)
        Animation(image, 400, 500, 400, 400, 75)
        imagelbl = Label(win, text="Made by: Herosteve198G")
        Animation(imagelbl, 275, 500, 275, 450, 75)
        homebtnqg.config(command= quizgame)
        homebtncg.config(command= colourgame)
        homebtnwt.config(command=wordtyper)

Screen("NameSelect")
win.mainloop()