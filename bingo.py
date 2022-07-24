import tkinter as tk
import random

buzzword_List = [
    'Synergy',
    'AI/ML',
    'Big Data',
    'Cloud',
    'Shift',
    'APT',
    'Digital\nTransformation',
    'NextGen',
    'Ransomware',
    'Threat Actor',
    'SIEM',
    'OSINT',
    'Low\nHanging\nFruit',
    'Fault\nTolerance',
    'Risk\nAppetite',
    'IOT',
    'Legacy',
    'Threat\nLandscape',
    '0-Day',
    'Adversary',
    'Bug',
    'Cloud',
    'EDR',
    'Mitre',
    'Backup',
]
buzzwords_used = []

def buzzwordRandomizer():
    buzzwords = random.sample(buzzword_List, 24)
    for buzzword in buzzwords:
        buzzwords_used.append(buzzword)

def buzzwordPlacementrandomizer():
    buzzword = random.choice(buzzwords_used)
    buzzwords_used.remove(buzzword)
    return buzzword


class CyberBingo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("Cyber Bingo")
        self.pack()
        buzzwordRandomizer()
        self.createWidgets()
        
    def createWidgets(self):
        self.buttons = {}
        xPos = 0
        yPos = 0
        for i in range(25):
            if(xPos == 5):
                yPos += 1
                xPos = 0
            if(xPos == 2 ) and (yPos == 2):
                self.buttons['free'] = tk.Button(self, text='Free', font='Sans 14 bold', height=5, width=10, command = lambda b='free': self.pressed(b), highlightbackground = "black")
                self.buttons['free'].grid(row=yPos, column=xPos)
                xPos += 1
                continue
            else:
                buzzword = buzzwordPlacementrandomizer()
                self.buttons[buzzword] = tk.Button(self, text=buzzword, font='Sans 14 bold', height=5, width=10, command = lambda b=buzzword: self.pressed(b), highlightbackground = "black")
                self.buttons[buzzword].grid(row=yPos, column=xPos)
                xPos += 1
    
    def pressed(self, index):
        if self.buttons[index].cget('highlightbackground') == 'black':
            self.buttons[index].configure(highlightbackground = "green", fg='green')
        else:
            self.buttons[index].configure(highlightbackground = "black", fg='black')

root = tk.Tk()
app = CyberBingo(master=root)
app.mainloop()
