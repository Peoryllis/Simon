import tkinter as tk
import random
import time

root = tk.Tk()
root['bg'] = '#E6E6FA'
root.geometry('600x600')

class Gameboard(tk.Frame):
    '''Gameboard
    creates the Simon gameboard
    '''

    def __init__(self, master):
        '''Gameboard(self, master)
        master: tkinter.Tk() or tkinter.Frame
        creates the Simon gameboard'''

        tk.Frame.__init__(self, master, bg=master['bg'])
        self.pack(fill='both', expand=1)

        self.fontstyle = ['Bodoni 72 Oldstyle', 18, 'bold']


        self.title = tk.Label(self, text='Simon!', bg='white', fg='black', font=['Bodoni 72 Oldstyle', 60, 'bold'])
        self.title.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1, anchor='n')
        
        self.score = 0

#keep track of score
        self.scoreboard = tk.Label(
            self, 
            text='score: 0', 
            bg='white', 
            fg='black', 
            font=self.fontstyle, 
            borderwidth=2, 
            relief='groove'
            )
        
        self.scoreboard.place(relx=0, rely=0, relwidth=0.25, relheight=0.05) 

#easy access to specific shades of colors
        self.colors = {
            'yellow': ['#bda800', '#ffe200'],
            'blue': ['#0129bf', '#88c5fc'],
            'red': ['#7b0000', '#ff0000'],
            'green': ['#137413', '#60e528']
        }

        self.buttonsFrame = tk.Frame(self, bg=self['bg'])
        self.buttonsFrame.place(relx=0, rely=0.13, relwidth=1, relheight=0.9)


### Create red button 
        self.redbutton = tk.Label(
            self.buttonsFrame, 
            bg=self.colors['red'][0], 
            borderwidth=5,
            relief='raised'
            )
        
        self.redbutton.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)
        self.redbutton.bind('<Button>', lambda e: self.color_selected('r'))


## create yellow button
        
        self.yellowbutton = tk.Label(
            self.buttonsFrame, 
            bg=self.colors['yellow'][0], 
            borderwidth=5,
            relief='raised'
            )
        
        self.yellowbutton.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)
        self.yellowbutton.bind('<Button>', lambda e: self.color_selected('y'))


    def color_selected(self, color):
        '''
        Gameboard.color_selected(color)
        color: 'r', 'g', 'b', or 'y'
        performs actions based on color selected
        '''
        if color == 'r':
            print(3)
            
            self.redbutton.configure(
                bg=self.colors['red'][1],
                relief='sunken'
                )
            self.master.update()

            time.sleep(0.25)

            self.redbutton.configure(
                bg=self.colors['red'][0],
                relief='raised'
                )
            self.master.update()

        if color == 'y':
            print(3)
            
            self.yellowbutton.configure(
                bg=self.colors['yellow'][1],
                relief='sunken'
                )
            self.master.update()

            time.sleep(0.25)

            self.yellowbutton.configure(
                bg=self.colors['yellow'][0],
                relief='raised'
                )
            self.master.update()
        





simon = Gameboard(root)

root.mainloop()