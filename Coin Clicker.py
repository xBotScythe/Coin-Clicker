# Start: 1/31/23, End: 2/22/23
# Cookie Clicker-esque game
from turtle import *
from tkinter import * 
import tkinter as tkin
from PIL import Image, ImageTk

# window setup
sWidth = 500
sHeight = 700
bgColor = "#161c24"
# user data
clicks = 0
coins = 0
coinsPerClick = 1
clickTime = 1500
acLvl = 1
isDblBought = FALSE
dblDisabled = FALSE
trplDisabled = FALSE
autoDisabled = FALSE
isAutoClickEnabled = FALSE
userPowers = []
# pre-stored data values
powerList = ["DoubleCoins", "TripleCoins", "AutoClick"]
coinTargets = [100, 1000, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 750000, 1000000]

# creates window
root = Tk()
root.geometry("500x700")
root.resizable(width=False, height=False)
root.title("Money Clicker")

# creates background color
canvas = Canvas(root, width=sWidth, height=sHeight)
canvas.pack()
canvas['background']=bgColor

# generates passive coins every 15 seconds
def passiveMoney(): 
     whenClicked()
     print("passive money activated")
     root.after(15000, passiveMoney)

# main button method, checks if button is clicked, updates count, and checks to see if target is met
def whenClicked():
    global clicks
    global coins
    global coinsPerClick
    global coinTargets
    clicks = clicks + 1
    coins = coins + coinsPerClick
    print("coin clicked!")
    print(clicks)
    updateCount()
    if(coinTargets[0] <= coins):
        coinsPerClick *= 2
        updateClickCount()
        coinTargets.pop(0)
        print("target reached!")

# creates shop window, checks what is already bought, and displays shop
def shopButtonClicked(): 
    global dblClick
    global trplClick
    global autoClickB
    global autoClickBL2
    global shopWindow
    global autoClickBL3
    global autoClickBL4
    shopWindow = Toplevel(root)
    shopWindow.title("Shop")
    shopWindow.geometry("200x350")
    dblClick = Button(shopWindow, text="Double Coins - 800", command=buyDblClick)
    trplClick = Button(shopWindow, text="Triple Coins - 1,200", command=buyTrplClick)
    autoClickB = Button(shopWindow, text="Buy Autoclicker - 500", command=buyAutoClick)
    autoClickBL2 = Button(shopWindow, text="Autoclicker Lvl 2 - 2,500", command=lambda: autoClickLevelUp(2500)) 
    autoClickBL3 = Button(shopWindow, text="Autoclicker Lvl 3 - 10,000", command=lambda: autoClickLevelUp(10000))
    autoClickBL4 = Button(shopWindow, text="Autoclicker Lvl 4 - 50,000", command=lambda: autoClickLevelUp(50000))
    autoClickB.pack(side=TOP)
    buttonUpdate()
    if(acLvl == 1):
        autoClickBL2.pack(side=TOP)
        buttonUpdate()   
    elif(acLvl == 2):
        autoClickBL3.pack(side=TOP)
        buttonUpdate()
    elif(acLvl == 3):
        autoClickBL4.pack(side=TOP)
        buttonUpdate()
    dblClick.pack(side=TOP)
    buttonUpdate()
    trplClick.pack(side=TOP)
    buttonUpdate()
           
# checks what level you are, checks if you have enough coins, and adjusts the autoclicker speed
def autoClickLevelUp(reqCoins):
    global acLvl
    global clickTime
    global coins
   #  global autoClickBL2
    if coinCheck(reqCoins) == TRUE:
        coins -= reqCoins
        acLvl += 1
        updateCount()
    if(acLvl == 2): #autoclicker lvl 2
            clickTime = 1000
            print(clickTime)
            autoClickBL2.config(state=tkin.DISABLED)
            autoClickBL3.pack(side=TOP)
    elif(acLvl == 3): # autoclicker lvl 3
            clickTime = 500
            print(clickTime)
            autoClickBL3.config(state=tkin.DISABLED)
            autoClickBL4.pack(side=TOP)
    elif(acLvl == 4): # autoclicker lvl 4
            clickTime = 250
            print(clickTime)
            autoClickBL4.config(state=tkin.DISABLED)

# buy method for double click
def buyDblClick():
    if(isDblBought == FALSE):
        global coinsPerClick
        global coins
        global dblDisabled
        if coinCheck(800) == TRUE:
            coins -= 800
            userPowers.append(powerList[0])
            coinsPerClick *= 2
            print(userPowers)
            updateCount()
            dblDisabled = TRUE
            buttonUpdate()
            
# buy method for triple click 
def buyTrplClick():
    global coinsPerClick
    global coins
    global trplDisabled
    if coinCheck(1200) == TRUE:
        coins -= 1200
        userPowers.append(powerList[1])
        coinsPerClick *= 3
        print(userPowers)
        updateCount()
        trplDisabled = TRUE
        buttonUpdate()
       
# buy auto click 
def buyAutoClick():
    global coins
    global isAutoClickEnabled
    global autoDisabled
    # global autoClickBL2
    if coinCheck(500) == TRUE:
        coins -= 500
        print("bought auto click!")
        userPowers.append(powerList[2])
        powerList.remove("AutoClick")
        isAutoClickEnabled = TRUE
        acBtn.place(relx=.9, rely=.865, anchor=E)
        autoClick()
        autoDisabled = TRUE
        buttonUpdate()
        autoClickBL2.pack(side=TOP)
        
# uses tkinter after() method and recursion to click automatically
def autoClick():
    global coins
    global clickTime
    if(isAutoClickEnabled == TRUE):
        print(str(clickTime) + " / " + str(acLvl)) 
        whenClicked()
        root.after(clickTime, autoClick)

# updates coin counter label
def updateCount():
    global coins
    updateClickCount()
    coinCounter.config(text=coins)

# updates click count label
def updateClickCount():
    global coinsPerClick
    clickCoinCounter.config(text=coinsPerClick)

# checks if you have enough coins  
def coinCheck(cBal):
    if(coins < cBal):
        tkin.messagebox.showwarning(title="Coin Check", message="Not enough coins.")
    else:
        return TRUE
   
# enables and disables auto clicker     
def autoClickToggle():
    global isAutoClickEnabled
    isAutoClickEnabled = not isAutoClickEnabled
    if(isAutoClickEnabled == TRUE):
        acBtn.config(image=ac_imageE)
        autoClick()
    else:
        acBtn.config(image=ac_image)
    
# updates shop buttons if they are bought    
def buttonUpdate():
    global dblDisabled
    global trplDisabled
    global autoDisabled
    if(dblDisabled == TRUE):
        dblClick.config(state=tkin.DISABLED)
    if(trplDisabled == TRUE):
        trplClick.config(state=tkin.DISABLED)
    if(autoDisabled == TRUE):
        autoClickB.config(state=tkin.DISABLED)
        
        
    
# creates a coin button
coin = PhotoImage(file = "Create Task\coinButton.png") 
coinBtn = Button(root, image = coin)
coinBtn.config(bg=bgColor, activebackground=bgColor, borderwidth=0, command=whenClicked)
coinBtn.place(relx=.5, rely=.075, anchor=N)
   
# creates dynamic counter
coinText = Label(text="Coins:", bg=bgColor,  fg='WHITE',font=('Comic Sans MS', 22))
coinText.place(relx=.5, rely=.5, anchor=CENTER)
coinCounter = Label(text=coins, bg=bgColor,  fg='WHITE',font=('Comic Sans MS', 22), justify=RIGHT)
coinCounter.place(relx=.50, rely=.55, anchor=CENTER)

# creates coins per click text & counter
clickCoinTxt = Label(text="Coins per Click:", bg=bgColor, fg='WHITE', font=('Comic Sans MS', 22))
clickCoinTxt.place(relx=.655, rely=.625, anchor=CENTER)
clickCoinCounter = Label(text=coinsPerClick, bg=bgColor, fg='WHITE', font=('Comic Sans MS', 22), justify=RIGHT)
clickCoinCounter.place(relx=.655, rely=.69, anchor=CENTER)

# creates shop button
shop = PhotoImage(file = "Create Task\shopButton.png")
shopBtn = Button(root, image = shop)
shopBtn.config(bg=bgColor, activebackground=bgColor, borderwidth=0, command=shopButtonClicked) # finish <---
shopBtn.place(relx=.09, rely=.775, anchor=W)

# creates but doesn't place autoclicker button
ac_image = PhotoImage(file = 'Create Task\clicker.png')
ac_imageE = PhotoImage(file = 'Create Task\clickerenabled.png')
acBtn = Button(root, image = ac_imageE)
acBtn.config(bg=bgColor, activebackground=bgColor, borderwidth=0, command=autoClickToggle)

root.after(10000, passiveMoney)
root.mainloop()