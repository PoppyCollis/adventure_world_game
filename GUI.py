import tkinter as tk
from Game import Game
from tkinter import messagebox
from tkinter import PhotoImage
import random
from tkinter.simpledialog import askstring


class App:

    # Creates a Frame for the application
    # and populates the GUI ...
    def __init__(self, root):
        """
            constructor method setting building frames and buttons
        :param root: window object
        return None
        """
        self.root = root
        self.game = Game()

        # Now we add two menu options to the window ...
        menubar = tk.Menu()
        menubar.add_command(label="Quit", command=self.quitGame)
        menubar.add_command(label="Help", command=self.showHelp)
        menubar.add_command(label="Inventory", command=self.showInventory)
        root.config(menu=menubar)

        # WIDGETS
        self.frame1 = tk.Frame(root, width=600, height=150, pady=10, bg='BlACK', borderwidth=2)
        self.frame1.pack_propagate(False)  # Prevents resizing

        self.frame3 = tk.Frame(root, width=800, height=80, pady=10, bg='BlACK', borderwidth=2)
        self.frame3.pack_propagate(False)  # Prevents resizing

        # ROOMS
        self.currentFrame = tk.Frame(root, width=800, height=350, bg='BlACK', borderwidth=2)
        self.currentFrame.grid_propagate(False)

        bg = PhotoImage(file="images/armoury.png")
        self.label1 = tk.Label(self.currentFrame, image=bg)
        self.label1.image = bg  # keep a reference!
        self.label1.pack()

        # this packs all frames into the root window ...
        self.frame1.pack()
        self.currentFrame.pack()
        self.frame3.pack()

        # grid config for current frame
        self.currentFrame.rowconfigure(0, pad=10)
        self.currentFrame.rowconfigure(1, pad=10)
        self.currentFrame.rowconfigure(2, pad=10)
        self.currentFrame.rowconfigure(3, pad=10)
        self.currentFrame.rowconfigure(4, pad=10)

        self.currentFrame.columnconfigure(0, pad=80)
        self.currentFrame.columnconfigure(1, pad=80)
        self.currentFrame.columnconfigure(2, pad=80)
        self.currentFrame.columnconfigure(3, pad=80)
        self.currentFrame.columnconfigure(4, pad=80)

        # add some useful widgets ...
        # text area
        txt_bg = PhotoImage(file="images/parch2.png")
        self.textArea1 = tk.Label(self.frame1, image=txt_bg,  width=600, text='', compound="center")
        self.textArea1.image = txt_bg
        self.textArea1.pack()

        # command area
        self.cmdArea = tk.Entry(self.frame3, text='')
        self.cmdArea.pack()
        self.buildGUI()

        # creating a PhotoImage object for characters
        photo_sentry = PhotoImage(file="images/sentry.png").subsample(10, 10)
        photo_priest = PhotoImage(file="images/priest.png").subsample(10, 10)
        photo_soldier = PhotoImage(file="images/soldier.png").subsample(10, 10)
        photo_nobleman = PhotoImage(file="images/nobleman.png").subsample(5, 5)
        photo_page = PhotoImage(file="images/page.png").subsample(10, 10)
        photo_jester = PhotoImage(file="images/jester.png").subsample(10, 10)
        photo_princess = PhotoImage(file="images/princess.png").subsample(10, 10)
        photo_musician = PhotoImage(file="images/musician.png").subsample(20, 20)
        photo_chancellor = PhotoImage(file="images/chancellor.png").subsample(15, 15)
        photo_doorward = PhotoImage(file="images/doorward.png").subsample(2, 2)
        photo_countess = PhotoImage(file="images/countess.png").subsample(5, 5)

        # all character buttons
        self.sentry = tk.Button(self.currentFrame, text='sentry', image=photo_sentry,
                                command=lambda: self.doTalkCommand("Sentry"))
        self.sentry.image = photo_sentry  # keep a reference!
        self.priest = tk.Button(self.currentFrame, text='priest', image=photo_priest,
                                command=lambda: self.doTalkCommand("Priest"))
        self.priest.image = photo_priest  # keep a reference!
        self.soldier = tk.Button(self.currentFrame, text='soldier', image=photo_soldier,
                                 command=lambda: self.doTalkCommand("Soldier"))
        self.soldier.image = photo_soldier  # keep a reference!
        self.nobleman = tk.Button(self.currentFrame, text='nobleman', image=photo_nobleman,
                                  command=lambda: self.doTalkCommand("Nobleman"))
        self.nobleman.image = photo_nobleman  # keep a reference!
        self.page = tk.Button(self.currentFrame, text='page', image=photo_page,
                              command=lambda: self.doTalkCommand("Page"))
        self.page.image = photo_page  # keep a reference!
        self.jester = tk.Button(self.currentFrame, text='jester', image=photo_jester,
                                command=lambda: self.doTalkCommand("Jester"))
        self.jester.image = photo_jester  # keep a reference!
        self.princess = tk.Button(self.currentFrame, text='princess', image=photo_princess,
                                  command=lambda: self.doTalkCommand("Princess"))
        self.princess.image = photo_princess  # keep a reference!
        self.musician = tk.Button(self.currentFrame, text='musician', image=photo_musician,
                                  command=lambda: self.doTalkCommand("Musician"))
        self.musician.image = photo_musician  # keep a reference!
        self.chancellor = tk.Button(self.currentFrame, text='chancellor', image=photo_chancellor,
                                    command=lambda: self.doTalkCommand("Chancellor"))
        self.chancellor.image = photo_chancellor  # keep a reference!
        self.doorward = tk.Button(self.currentFrame, text='doorward', image=photo_doorward,
                                  command=lambda: self.doTalkCommand("Doorward"))
        self.doorward.image = photo_doorward  # keep a reference!
        self.countess = tk.Button(self.currentFrame, text='countess', image=photo_countess,
                                  command=lambda: self.doTalkCommand("Countess"))
        self.countess.image = photo_countess  # keep a reference!

        # all characters dict
        self.characterDict = {"Priest": self.priest, "Sentry": self.sentry, "Soldier": self.soldier,
                              "Nobleman": self.nobleman, "Page": self.page, "Musician": self.musician,
                              "Jester": self.jester, "Princess": self.princess,
                              "Chancellor": self.chancellor, "Doorward": self.doorward, "Countess": self.countess}

        # Creating a PhotoImage object for items
        photo_bible = PhotoImage(file="images/bible.png").subsample(10, 10)
        photo_candle = PhotoImage(file="images/candle.png").subsample(10, 10)
        photo_torch = PhotoImage(file="images/torch.png").subsample(5, 5)
        photo_rope = PhotoImage(file="images/rope.png").subsample(3, 3)
        photo_platter = PhotoImage(file="images/platter.png").subsample(5, 5)
        photo_spoon = PhotoImage(file="images/spoon.png").subsample(5, 5)
        photo_goblet = PhotoImage(file="images/goblet.png").subsample(15, 15)
        photo_dress = PhotoImage(file="images/dress.png").subsample(5, 5)

        # all item buttons
        self.bible = tk.Button(self.currentFrame, text='bible', image=photo_bible,
                               command=lambda: self.pickUpItem("bible"))
        self.bible.image = photo_bible  # keep a reference!

        self.candle = tk.Button(self.currentFrame, text='candle', image=photo_candle,
                                command=lambda: self.pickUpItem("candle"))
        self.candle.image = photo_candle  # keep a reference!

        self.torch = tk.Button(self.currentFrame, text='torch', image=photo_torch,
                               command=lambda: self.pickUpItem("torch"))
        self.torch.image = photo_torch  # keep a reference!

        self.rope = tk.Button(self.currentFrame, text='rope', image=photo_rope, command=lambda: self.pickUpItem("rope"))
        self.rope.image = photo_rope  # keep a reference!

        self.platter = tk.Button(self.currentFrame, text='platter', image=photo_platter,
                                 command=lambda: self.pickUpItem("platter"))
        self.platter.image = photo_platter  # keep a reference!

        self.spoon = tk.Button(self.currentFrame, text='spoon', image=photo_spoon,
                               command=lambda: self.pickUpItem("spoon"))
        self.spoon.image = photo_spoon  # keep a reference!

        self.goblet = tk.Button(self.currentFrame, text='goblet', image=photo_goblet,
                                command=lambda: self.pickUpItem("goblet"))
        self.goblet.image = photo_goblet  # keep a reference!

        self.dress = tk.Button(self.currentFrame, text='dress', image=photo_dress,
                               command=lambda: self.pickUpItem("dress"))
        self.dress.image = photo_dress  # keep a reference!

        # all items dict
        self.itemDict = {"bible": self.bible, "candle": self.candle, "torch": self.torch, "rope": self.rope,
                         "platter": self.platter, "spoon": self.spoon, "goblet": self.goblet, "dress": self.dress}

    def quitGame(self):
        """
            Quits the game and then destroys the GUI window
        :return: None
        """
        self.game.quit()
        self.root.destroy()

    def speechBox(self, character, msg):
        """
        :param character: the name of the character speaking
        :param msg: the message the character says (str)
        :return: True
        """
        messagebox.showinfo(f'{character}', msg)
        return True

    def buildGUI(self):
        """
            builds the GUI by packing buttons and setting up the text area to print welcome from game class
        :return: True
        """
        self.doCmd = tk.Button(self.frame3, text='GO',
                               fg='black', bg='blue',
                               command=self.doCommand)
        self.doCmd.pack()
        self.speechBox("Welcome", self.game.printWelcome())
        self.textArea1.configure(text=self.game.currentRoom.getLongDescription())
        return True

    def showHelp(self):
        """
            gets help message from game and displays it in the help message box
        :return: None
        """
        msg = self.game.printHelp()
        messagebox.showinfo("Help", msg)

    def showInventory(self):
        """
            gets all backpack items from player class and displays in info box
        :return: None
        """
        msg = self.game.player.showBackpackItems()
        messagebox.showinfo("Inventory", msg)

    def changeFrame(self, currentRoom):
        """
            resets current frame by forgetting buttons and reloading only those in current room
        :param currentRoom: the room the player is currently in
        :return: None
        """
        # forget buttons within frame
        for char in self.characterDict.values():
            char.grid_forget()
        for object in self.itemDict.values():
            object.grid_forget()
        # make new buttons
        items = currentRoom.getAllRoomItems()
        characters = currentRoom.getAllRoomCharacters()
        # if in king's bedroom, change background image
        if self.game.currentRoom.name == "bedchamber":
            self.label1.pack_forget()
            bg = PhotoImage(file="images/bedroom.png")
            self.label1 = tk.Label(self.currentFrame, image=bg)
            self.label1.image = bg  # keep a reference!
            self.label1.pack()
            response = messagebox.showinfo("You have found him!", self.game.printEnding() +
                                           "Press 'ok' to grab the teddy and end game")
            if response == "ok":
                self.root.destroy()
        # character buttons
        if characters is not None:
            for i, char in enumerate(characters):
                x = random.randint(0, 2)
                self.characterDict[char].grid(row=x, column=i+1)
        # item buttons
        if items is not None:
            for i, item in enumerate(items):
                self.itemDict[item].grid(row=i, column=i+2)

    def interactBox(self, character):
        """
            displays the interaction conversation with character after user indicates whether they'd like to continue
        :param character: character being interacted with
        :return: None
        """
        char = self.game.currentRoom.getCharacterByName(character)
        ans = messagebox.askquestion("Keep interacting", "Would you like to continue?")
        if ans == 'yes':
            # execute the interaction command
            msg = self.game.doInteractionCommand(char)
            self.speechBox(character, msg)

    def jesterInteractBox(self, character):
        """
            displays the interaction conversation with jester and allows user to input guess answer to riddle question
        :param character:
        :return:
        """
        char = self.game.currentRoom.getCharacterByName(character)
        ans = messagebox.askquestion("Keep interacting", "Would you like to continue interacting with this person?")
        if ans == 'yes':
            # execute the jester interaction command
            msg = self.game.doInteractionCommand(char)
            self.speechBox("Jester", msg)
            ans2 = askstring('Guess', 'What is your answer?')
            output = self.game.jester.answer(ans2)
            self.speechBox("Jester", output)

    def pickUpItem(self, item):
        """
            displays information about the item that the player has picked up
        :param item: item that is to be picked up
        :return: None
        """
        result = self.game.doGetItemCommand(item)
        if result is not None:
            self.speechBox("Whoops!", result)
            self.textArea1.configure(text=self.game.currentRoom.getLongDescription())
        self.changeFrame(self.game.currentRoom)

    def doTalkCommand(self, character):
        """
            displays conversation with character in a messagebox and calls correct interaction box if appropriate
        :param character: character being talked to
        :return: None
        """
        msg, canInteract = self.game.doTalkCommand(character)
        self.speechBox(character, msg)
        if canInteract:
            if character == 'Jester':
                self.jesterInteractBox(character)
            else:
                self.interactBox(character)
                self.changeFrame(self.game.currentRoom)

    def doCommand(self):
        """
            gets command from the text prompt area and clears it and then calls process command on it
        :return: None
        """
        command = self.cmdArea.get()  # Returns a 2-tuple
        self.processCommand(command)
        self.clearTextBox()

    def clearTextBox(self):
        """
            clears the text prompt box so user can input the next command easily
        :return: None
        """
        self.cmdArea.delete(0, tk.END)

    def getCommandString(self, inputLine):
        """
            Fetches a command (borrowed from old TextUI)
        :return: a string
        """
        if inputLine == "":
            return None
        else:
            return str(inputLine)

    def processCommand(self, command):
        """
            processes the command by checking it's not None and executing the game class's doGoCommand
        :param command: command word (str)
        :return: None
        """
        commandWord = self.getCommandString(command)
        if commandWord is not None:
            msg = self.game.doGoCommand(commandWord)
            self.textArea1.configure(text=msg)
            self.changeFrame(self.game.currentRoom)
        else:
            # Unknown command ...
            self.textArea1.configure(text="Please specify a direction \nyou would like to go in.")


def main():

    win = tk.Tk()  # Create a window
    win.configure(bg='BLACK')
    win.title("Adventure World with GUI")  # Set window title
    win.geometry("800x600")  # Set window size
    win.resizable(False, False)  # Both x and y dimensions ...

    # Create the GUI as a Frame
    # and attach it to the window ...
    App(win)

    # Call the GUI mainloop ...
    win.mainloop()


if __name__ == "__main__":
    main()


