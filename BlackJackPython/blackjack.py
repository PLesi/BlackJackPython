from tkinter import *
from random import *


root = Tk()
root.geometry('700x600')

c = Canvas(root,width=700,height=500,bg='#1D7828')
c.pack()

d=13
s=13
t=13
l= 13

scoreP1 = 0
scoreP2 = 0

coinsP1 = 500
bet = 0

cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
symbol = ['d','s','t','l']
usedCards = []
x = 0

endTurn = False
endAiTurn = False

win = False
AiWin = False

scorP1 = c.create_text(40,20,text='P1:  ',font='Arial 20 bold')
scorP2 = c.create_text(650,20,text='P2:  ',font='Arial 20 bold')
coinsP1Txt = c.create_text(350,20,text=('Coins:',coinsP1),font='Arial 20 bold',fill='yellow')


def reset():
    global cards,symbol,usedCards,d,s,t,l,scoreP1,scoreP2,coinsP1,bet,x,endTurn,scoreP1,coinsP1,scorP1,coinsP1Txt,endAiTurn,AiWin,win,Bt,scorP2,ox,oy
    c.delete('all')
    d=13
    s=13
    t=13
    l=13

    scoreP1 = 0
    scoreP2 = 0

    coinsP1 = 500
    bet = 0

    cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
    symbol = ['d','s','t','l']
    usedCards = []
    x = 0
    ox=0
    oy=0
    endTurn = False
    endAiTurn = False
    win = False
    AiWin = False

    scorP1 = c.create_text(40,20,text='P1:  ',font='Arial 20 bold')
    scorP2 = c.create_text(650,20,text='P2:  ',font='Arial 20 bold')

    coinsP1Txt = c.create_text(350,20,text=('Coins:',coinsP1),font='Arial 20 bold',fill='yellow')
    Bt.config(text=("BET:",bet))
    enab()
    getCard()
    getCard()
    backOfTheCard(110,250)
    FirstcardOfAi()
    
def newGame():
    global cards,symbol,usedCards,d,s,t,l,scoreP1,scoreP2,coinsP1,bet,x,endTurn,scoreP1,coinsP1,scorP1,coinsP1Txt,endAiTurn,AiWin,win,Bt,scorP2,ox,oy
    c.delete('all')
    d=13
    s=13
    t=13
    l=13
    scoreP1 = 0
    scoreP2 = 0
    bet = 0
    cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
    symbol = ['d','s','t','l']
    usedCards = []
    x = 0
    ox=0
    oy=0
    endTurn = False
    endAiTurn = True
    win = False
    AiWin = False

    scorP1 = c.create_text(40,20,text='P1:  ',font='Arial 20 bold')
    scorP2 = c.create_text(650,20,text='P2:  ',font='Arial 20 bold')

    coinsP1Txt = c.create_text(350,20,text=('Coins:',coinsP1),font='Arial 20 bold',fill='yellow')
    Bt.config(text=("BET:",bet))
    enab()
    getCard()
    getCard()
    backOfTheCard(110,250)
    FirstcardOfAi()

def kartaSrdce(x,y):
    c.create_rectangle(50+x,50+y,150+x,200+y,fill='white',width=3,outline='black')

    c.create_polygon(55+x,60+y,60+x,55+y,62.5+x,55+y,65+x,57+y,67.5+x,55+y,70+x,55+y,75+x,60+y,65+x,70+y,fill='red',width=2,outline='black')
    c.create_line(62.5+x,55+y,68+x,60+y,width=2,fill='black')

    c.create_polygon(55+x,185+y,60+x,180+y,62.5+x,180+y,65+x,182+y,67.5+x,180+y,70+x,180+y,75+x,185+y,65+x,195+y,fill='red',width=2,outline='black')
    c.create_line(62.5+x,180+y,68+x,185+y,width=2,fill='black')

    c.create_polygon(125+x,60+y,130+x,55+y,132.5+x,55+y,135+x,57+y,137.5+x,55+y,140+x,55+y,145+x,60+y,135+x,70+y,fill='red',width=2,outline='black')
    c.create_line(132.5+x,55+y,138+x,60+y,width=2,fill='black')

    c.create_polygon(125+x,185+y,130+x,180+y,132.5+x,180+y,135+x,182+y,137.5+x,180+y,140+x,180+y,145+x,185+y,135+x,195+y,fill='red',width=2,outline='black')
    c.create_line(132.5+x,180+y,138+x,185+y,width=2,fill='black')

    c.create_polygon(65+x,110+y,75+x,90+y,90+x,90+y,100+x,100+y,110+x,90+y,125+x,90+y,135+x,110+y,100+x,155+y,fill='red',width=2,outline='black')
    c.create_line(90+x,90+y,110+x,110+y,width=2,fill='black')

def kartaDiamant(x,y):
    c.create_rectangle(50+x,50+y,150+x,200+y,fill='white',width=3,outline='black')
    c.create_polygon(55+x,65+y,65+x,55+y,75+x,65+y,65+x,75+y,fill='red',width=2,outline='black')

    c.create_polygon(55+x,185+y,65+x,175+y,75+x,185+y,65+x,195+y,fill='red',width=2,outline='black')

    c.create_polygon(125+x,65+y,135+x,55+y,145+x,65+y,135+x,75+y,fill='red',width=2,outline='black')

    c.create_polygon(125+x,185+y,135+x,175+y,145+x,185+y,135+x,195+y,fill='red',width=2,outline='black')

    c.create_polygon(65+x,125+y,100+x,75+y,135+x,125+y,100+x,175+y,fill='red',outline='black',width=2)

def kartaList(x,y):
    c.create_rectangle(50+x,50+y,150+x,200+y,fill='white',width=3,outline='black')
    c.create_polygon(55+x,70+y,55+x,65+y,65+x,55+y,75+x,65+y,75+x,70+y,70+x,72.5+y,67+x,72.5+y,67+x,75+y,63+x,75+y,63+x,72.5+y,60+x,72.5+y,fill='black')

    c.create_polygon(55+x,190+y,55+x,185+y,65+x,175+y,75+x,185+y,75+x,190+y,70+x,192.5+y,67+x,192.5+y,67+x,195+y,63+x,195+y,63+x,192.5+y,60+x,192.5+y,fill='black')

    c.create_polygon(125+x,70+y,125+x,65+y,135+x,55+y,145+x,65+y,145+x,70+y,140+x,72.5+y,137+x,72.5+y,137+x,75+y,133+x,75+y,133+x,72.5+y,130+x,72.5+y,fill='black')

    c.create_polygon(125+x,190+y,125+x,185+y,135+x,175+y,145+x,185+y,145+x,190+y,140+x,192.5+y,137+x,192.5+y,137+x,195+y,133+x,195+y,133+x,192.5+y,130+x,192.5+y,fill='black')
    
    c.create_polygon(95+x,160+y,105+x,160+y,105+x,172.5+y,107+x,175+y,93+x,175+y,95+x,172.5+y,fill='black',width=2)
    c.create_polygon(65+x,150+y,65+x,120+y,100+x,75+y,135+x,120+y,135+x,150+y,120+x,165+y,80+x,165+y,fill='black',width=2)


def kartaTriList(x,y):
    c.create_rectangle(50+x,50+y,150+x,200+y,fill='white',width=3,outline='black')
    c.create_oval(55+x,65+y,65+x,72.5+y,fill='black',outline='black')
    c.create_oval(65+x,65+y,75+x,72.5+y,fill='black',outline='black')
    c.create_oval(60+x,55+y,70+x,67+y,fill='black',outline='black')
    c.create_rectangle(63+x,60+y,67+x,75+y,fill='black',outline='black')

    c.create_oval(55+x,185+y,65+x,192.5+y,fill='black',outline='black')
    c.create_oval(65+x,185+y,75+x,192.5+y,fill='black',outline='black')
    c.create_oval(60+x,175+y,70+x,187+y,fill='black',outline='black')
    c.create_rectangle(63+x,180+y,67+x,195+y,fill='black',outline='black')

    c.create_oval(125+x,65+y,135+x,72.5+y,fill='black',outline='black')
    c.create_oval(135+x,65+y,145+x,72.5+y,fill='black',outline='black')
    c.create_oval(130+x,55+y,140+x,67+y,fill='black',outline='black')
    c.create_rectangle(133+x,60+y,137+x,75+y,fill='black',outline='black')

    c.create_oval(125+x,185+y,135+x,192.5+y,fill='black',outline='black')
    c.create_oval(135+x,185+y,145+x,192.5+y,fill='black',outline='black')
    c.create_oval(130+x,175+y,140+x,187+y,fill='black',outline='black')
    c.create_rectangle(133+x,180+y,137+x,195+y,fill='black',outline='black')

    c.create_oval(65+x,110+y,100+x,145+y,fill='black',outline='black')
    c.create_oval(100+x,110+y,135+x,145+y,fill='black',outline='black')
    c.create_oval(82.5+x,80+y,117.5+x,130+y,fill='black',outline='black')
    c.create_rectangle(92.5+x,100+y,107.5+x,150+y,fill='black',outline='black')
    c.create_polygon(90+x,155+y,90+x,152+y,92.5+x,150+y,107.5+x,150+y,110+x,152+y,110+x,155+y,fill='black',outline='black')

ox=0
oy=0
backColor = ['blue','red']
def backOfTheCard(x,y):
    global ox,oy,backColor
    farba = choice(backColor)
    c.create_rectangle(50+x,50+y,150+x,200+y,fill='white',width=3,outline='black')
    c.create_rectangle(60+x,60+y,140+x,190+y,fill='white',width=3,outline=farba)
    for i in range(375):
        c.create_oval(60+x+ox,60+y+oy,70+x+ox,70+y+oy,width=1,outline=farba)
        ox+=5
        if ox == 75:
            ox = 0
            oy += 5

backOfTheCard(0,250)

def getCard():
    global cards,symbol,usedCards,d,s,t,l,x,scoreP1,scoreP2,endTurn,scorP1,coinsP1,bet,coinsP1Txt,endTurn,win,AiWin,endAiTurn
    farba = 'black'
    
    if endTurn == False:
        card = choice(cards)
        symb = choice(symbol)
        c.itemconfig(scorP1,text=('P1:',scoreP1+card))
        if symb == 'd':
            d -= 1
            kartaDiamant(x,0)
            if d == 0:
                symbol.remove(d)
            
        if symb == 's':
            s -= 1
            kartaSrdce(x,0)
            if s == 0:
                symbol.remove(s)

        if symb == 't':
            t -= 1
            kartaTriList(x,0)
            farba = 'white'
            if t == 0:
                symbol.remove(t)

        if symb == 'l':
            l -= 1
            kartaList(x,0)
            farba = 'white'
            if l == 0:
                symbol.remove(l)

        cards.remove(card)
        usedCards.append([card,symb])
        print(usedCards)

        c.create_text(100+x,125,text=card,fill=farba,font='Arial 20 bold')
        if not endTurn:
            x+=110
            scoreP1 += card
            if scoreP1 > 21:
                print('busted')
                c.create_rectangle(40,100,660,152,fill='grey',outline='black',width=5)
                c.create_text(350,125,text='B U S T E D',font='Arial 100 bold',fill='#951414')
                endTurn = True
                c.itemconfig(scorP1,fill='red')
                c.update()
                c.after(1000)
                c.update()
                newGame()
                endAiTurn = False
            elif scoreP1 == 21:
                print('blackjack')
                endTurn = True
                win = True
                coinsP1 += bet * 2
                c.itemconfig(coinsP1Txt,text=('Coins:',coinsP1))
                c.create_rectangle(40,100,660,152,fill='grey',outline='black',width=5)
                c.create_text(350,125,text='W I N N E R',font='Arial 100 bold',fill='#57CBFF')
                c.itemconfig(scorP1,fill='#5DFF57')
                c.update()
                c.after(1000)
                c.update()
                newGame()
                endAiTurn = False
                
            else:
                print('nič')
       
    
    
            
def betUp100():
    global coinsP1,bet,coinsP1Txt,c
    if coinsP1 >= 100:
        coinsP1 -= 100
        bet += 100
        Bt.config(text=('BET:',bet))
        c.itemconfig(coinsP1Txt,text=('Coins:',coinsP1))
    else:
        print("málo peňazí")

def betUp10():
    global coinsP1,bet,coinsP1Txt,c
    if coinsP1 >= 10:
        coinsP1 -= 10
        bet += 10
        Bt.config(text=('BET:',bet))
        c.itemconfig(coinsP1Txt,text=('Coins:',coinsP1))
    else:
        print("málo peňazí")

def betDown10():
    global coinsP1,bet,coinsP1Txt,c
    if bet >= 10:
        coinsP1 += 10
        bet -= 10
        Bt.config(text=('BET:',bet))
        c.itemconfig(coinsP1Txt,text=('Coins:',coinsP1))
    else:
        print("Nieje čo vrátiť")

def betDown100():
    global coinsP1,bet,coinsP1Txt,c
    if bet >= 100:
        coinsP1 += 100
        bet -= 100
        Bt.config(text=('BET:',bet))
        c.itemconfig(coinsP1Txt,text=('Coins:',coinsP1))
    else:
        print("Nieje čo vrátiť")

def end():
    root.destroy()

def Ai():
    global scoreP1,scoreP2,usedCards,cards,symbol,usedCards,d,s,t,l,endAiTurn,win,AiWin
    if scoreP2 > scoreP1 and scoreP2 < 22:
        endAiTurn = True
        AiWin = True
        c.create_rectangle(40,110+250,660,142+250,fill='grey',outline='black',width=5)
        c.create_text(350,125+250,text='W I N N E R',font='Arial 100 bold',fill='#57CBFF')
        c.update()
        c.after(2000)
        c.update()
        newGame()
    
    elif scoreP2 == 21:
        endAiTurn = True
        
        if scoreP2 == scoreP1:
            print("remíza")
    elif scoreP2 > 21: 
        endAiTurn = True
        win = True
        
    else:
        endAiTurn = False
def endOfTurn():
    global cards,symbol,usedCards,d,s,t,l,x,scoreP1,scoreP2,endTurn,scorP1,coinsP1,bet,coinsP1Txt,endTurn,win,AiWin,endAiTurn,scorP2
    endTurn=True
    endAiTurn = False
    y=250
    x=110
    while endAiTurn == False:
        if endAiTurn == False:
            Ai()
            farba = 'black'
            card = choice(cards)
            symb = choice(symbol)
            print('uwu')
            c.itemconfig(scorP2,text=('P2:',scoreP2+card))
            if symb == 'd':
                d -= 1
                kartaDiamant(x,y)
                if d == 0:
                    symbol.remove(d)
                
            if symb == 's':
                s -= 1
                kartaSrdce(x,y)
                if s == 0:
                    symbol.remove(s)

            if symb == 't':
                t -= 1
                kartaTriList(x,y)
                farba = 'white'
                if t == 0:
                    symbol.remove(t)

            if symb == 'l':
                l -= 1
                kartaList(x,y)
                farba = 'white'
                if l == 0:
                    symbol.remove(l)

            cards.remove(card)
            usedCards.append([card,symb])
            print(usedCards)
            c.create_text(100+x,125+y,text=card,fill=farba,font='Arial 20 bold')
            x+=110
            scoreP2 += card
            c.after(1000)
            c.update()
            Ai()
            if scoreP2 > 21:
                print('busted')
                c.create_rectangle(40,110+y,660,142+y,fill='grey',outline='black',width=5)
                c.create_text(350,125+y,text='B U S T E D',font='Arial 100 bold',fill='#951414')
                c.itemconfig(scorP2,fill='red')
                coinsP1 += bet*2
                endAiTurn = True
                c.itemconfig(coinsP1Txt,text=('Coins:',coinsP1))
                c.create_rectangle(40,110+y,660,142+y,fill='grey',outline='black',width=5)
                c.create_text(350,125+y,text='B U S T E D',font='Arial 100 bold',fill='#951414')
                c.update()
                c.after(1000)
                c.update()
                newGame()
            elif scoreP2 == 21:
                print('blackjack')
                c.create_text()
                endAiTurn = True
                c.create_rectangle(40,110+y,660,142+y,fill='grey',outline='black',width=5)
                c.create_text(350,125+y,text='W I N N E R',font='Arial 100 bold',fill='#57CBFF')
                c.update()
                c.after(1000)
                c.update()
                newGame()

            else:
                print('nič')
        
            

def FirstcardOfAi():
    global cards,symbol,usedCards,d,s,t,l,x,scoreP1,scoreP2,endTurn,scorP1,coinsP1,bet,coinsP1Txt,endTurn,win,AiWin,endAiTurn,scorP2
    y=250
    farba = 'black'
    card = choice(cards)
    symb = choice(symbol)
    print('uwu')
    c.itemconfig(scorP2,text=('P2:',scoreP2+card))
    if symb == 'd':
        d -= 1
        kartaDiamant(0,y)
        if d == 0:
            symbol.remove(d)
        
    if symb == 's':
        s -= 1
        kartaSrdce(0,y)
        if s == 0:
            symbol.remove(s)

    if symb == 't':
        t -= 1
        kartaTriList(0,y)
        farba = 'white'
        if t == 0:
            symbol.remove(t)

    if symb == 'l':
        l -= 1
        kartaList(0,y)
        farba = 'white'
        if l == 0:
            symbol.remove(l)

    cards.remove(card)
    usedCards.append([card,symb])
    print(usedCards)
    c.create_text(100,125+y,text=card,fill=farba,font='Arial 20 bold')

    scoreP2 += card

def exitWindow():
    ExitScreen = Toplevel(root)
    ExitScreen.title("Exit?")
    ExitScreen.geometry('200x100')
    endText = Label(ExitScreen,text='Do you realy want exit?',font='Arial 15 bold')
    yesBtn = Button(ExitScreen,text='YES',command=end)
    noBtn = Button(ExitScreen,text='NO',command=ExitScreen.destroy)
    endText.pack(pady=5)
    yesBtn.pack(side=LEFT,padx=10)
    noBtn.pack(side=RIGHT,padx=10)

getCard()
getCard()
FirstcardOfAi()
ox=0
oy=0
backOfTheCard(110,250)
btnBetUp100 = Button(root,text='⌃\n100€',foreground='black',width=2,height=5,command=betUp100)
btnBetUp10 = Button(root,text='⌃\n10€',foreground='black',width=2,height=5, command=betUp10)

btnBetDown10 = Button(root,text='10€\n⌵',foreground='black',width=2,height=5,command=betDown10)
btnBetDown100 = Button(root,text='100€\n⌵',foreground='black',width=2,height=5,command=betDown100)


btnStop = Button(root,width=5,height=5,text='Stop',font='Arial 20 bold',command=endOfTurn)


Bt = Label(root,width=20,height=5,text = 'BET:',background='white',foreground='black')
btnReset = Button(root,width=2,height=5,text='Reset',command=reset)
btnQuit = Button(root,width=2,height=5,text='X',command=exitWindow)

def dis():
    global btnBetDown10,btnBetDown100,btnBetUp10,btnBetUp100
    btnBetDown100.config(state=DISABLED)
    btnBetDown10.config(state=DISABLED)
    btnBetUp10.config(state=DISABLED)
    btnBetUp100.config(state=DISABLED)

    btnBetUp100.pack(side=LEFT)
    btnBetUp10.pack(side=LEFT)
    btnBetDown100.pack(side=RIGHT)
    btnBetDown10.pack(side=RIGHT)
    getCard()
def enab():
    global btnBetDown10,btnBetDown100,btnBetUp10,btnBetUp100
    btnBetDown100.config(state=NORMAL)
    btnBetDown10.config(state=NORMAL)
    btnBetUp10.config(state=NORMAL)
    btnBetUp100.config(state=NORMAL)

    btnBetUp100.pack(side=LEFT)
    btnBetUp10.pack(side=LEFT)
    btnBetDown100.pack(side=RIGHT)
    btnBetDown10.pack(side=RIGHT)



btnPlusCard = Button(root,width=5,height=5,text='+',font='Arial 20 bold',command=dis)
btnBetUp100.pack(side=LEFT)
btnBetUp10.pack(side=LEFT)
btnPlusCard.pack(side=LEFT)
btnQuit.pack(side=LEFT)

Bt.pack(side=LEFT)

btnBetDown100.pack(side=RIGHT)
btnBetDown10.pack(side=RIGHT)
btnStop.pack(side=RIGHT)
btnReset.pack(side=RIGHT)

root.mainloop()