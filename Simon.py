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
        self.fontname = 'Bodoni 72 Oldstyle'


        self.title = tk.Label(self, text='Simon!', bg='white', fg='black', font=(self.fontname, 60, 'bold'))
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

# keep track of high score
        self.highScore = 0
        self.highScoreBoard = tk.Label(
            self, 
            text='high score: 0', 
            bg='white', 
            fg='black', 
            font=self.fontstyle, 
            borderwidth=2, 
            relief='groove'
            )
        self.highScoreBoard.place(relx=0, rely=0.05, relwidth=0.25, relheight=0.05)

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

#create the green button
        self.greenbutton = tk.Label(
            self.buttonsFrame, 
            bg=self.colors['green'][0], 
            borderwidth=5,
            relief='raised'
            )
        
        self.greenbutton.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)
        self.greenbutton.bind('<Button>', lambda e: self.color_selected('g'))

        self.bluebutton = tk.Label(
            self.buttonsFrame, 
            bg=self.colors['blue'][0], 
            borderwidth=5,
            relief='raised'
            )
        
        self.bluebutton.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
        self.bluebutton.bind('<Button>', lambda e: self.color_selected('b'))

        self.master.update()

        self.computer_sequence = []

        self.player_sequence = []

        self.playerTurn = False
        self.playerWinning = True

    def red_selected(self):
        '''
        Gameboard.red_selected()
        actions for when red button is selected
        '''

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
    
    def yellow_selected(self):
        '''
        Gameboard.yellow_selected()
        actions for when yellow button is selected
        '''
            
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

    def green_selected(self):
        '''
        Gameboard.green_selected()
        actions for when green button is selected
        '''
            
        self.greenbutton.configure(
        bg=self.colors['green'][1],
        relief='sunken'
            )
        self.master.update()

        time.sleep(0.25)

        self.greenbutton.configure(
            bg=self.colors['green'][0],
            relief='raised'
            )
        self.master.update()
    
    def blue_selected(self):
        '''
        Gameboard.blue_selected()
        actions for when blue button is selected
        '''
            
        self.bluebutton.configure(
        bg=self.colors['blue'][1],
        relief='sunken'
            )
        self.master.update()

        time.sleep(0.25)

        self.bluebutton.configure(
            bg=self.colors['blue'][0],
            relief='raised'
            )
        self.master.update()

    def color_selected(self, color):
        '''
        Gameboard.color_selected(color)
        color: 'r', 'g', 'b', or 'y'
        performs actions based on color selected
        '''

        if not self.playerTurn:
            return None
        
        if color == 'r':
            self.red_selected()
            self.player_sequence.append(0)
        elif color == 'y':
            self.yellow_selected()
            self.player_sequence.append(1)
        elif color == 'g':
            self.green_selected()
            self.player_sequence.append(2)
        elif color == 'b':
            self.blue_selected()
            self.player_sequence.append(3)

        if self.computer_sequence[:len(self.player_sequence)] != self.player_sequence:
            self.playerWinning = False

    def computer_turn(self):
        '''
        Gameboard.computer_turn
        the computer picks the sequence for Simon
        '''

        time.sleep(0.5)

        self.title.configure(
            text='Computer turn',
            font=['Bodoni 72 Oldstyle', 40, 'bold']
        )
        

        self.master.update()

        time.sleep(0.5)

        choices = {
            0: self.red_selected,
            1: self.yellow_selected,
            2: self.green_selected,
            3: self.blue_selected
        }

        if len(self.computer_sequence) > 0:
            for item in self.computer_sequence:
                choices[item]()
                time.sleep(0.5)

        self.computer_sequence.append(random.randrange(4))
        choices[self.computer_sequence[-1]]()
        

    def update_scores(self):
        self.score = len(self.player_sequence)

        if self.score > self.highScore:
            self.highScore = self.score
        
        self.scoreboard.configure(
            text=f'score: {self.score}'
        )
        
        self.highScoreBoard.configure(
            text=f'high score: {self.highScore}'
        )

        self.master.update()

    def game_over(self):
        '''
        Gameboard.game_over
        gives a game over screen
        '''

        gameOverFrame = tk.Frame(
            self,
            bg='white'
        )

        gameOverFrame.place(
            relx=0.5,
            rely=0.5,
            relwidth=0.5,
            relheight=0.5,
            anchor='center'
        )

        gameOverTitle = tk.Label(
            gameOverFrame,
            text='GAME OVER',
            font=(self.fontname, 60, 'bold'),
        )

        gameOverTitle.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        instructions = tk.Label(
            gameOverFrame,
            text = 'Select whether you would like to go again or not',
            font=(self.fontname, 18, 'bold')
        )

        instructions.place(relx=0, rely=0.1, relwidth=1, relheight=0.05)

        







    def play_game(self):
        '''
        Gameboard.play_game
        Plays a game of simon
        '''

        self.score = 0
        self.computer_sequence = []
        self.playersequence = []

        while self.playerWinning:

            print(len(self.computer_sequence), len(self.player_sequence))

            if len(self.player_sequence) != len(self.computer_sequence):
                self.title.configure(
                    text='Your turn'
                )  

                self.master.update()

                self.playerTurn = True
            else:
                self.update_scores()
                self.player_sequence = []
                self.playerTurn = False
                self.computer_turn()





simon = Gameboard(root)
simon.play_game()

root.mainloop()