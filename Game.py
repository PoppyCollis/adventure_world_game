from Room import *
from Item import Item
from Player import Player
from Characters import *
import logging

"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game. Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, create an instance of this class and call the "play"
    method.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game.  It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage.
    
    This game has been further extended to a scenario where you play 
    a character in a medieval castle looking for the king.
"""


class Game:

    def __init__(self):
        """
            Constructor method
        Initialises the game by calling methods to create rooms, characters, items and player and log
        """
        self.createRooms()
        self.createItems()
        self.createCharacters()
        self.currentRoom = self.castle_grounds
        self.player = Player()

        # User log
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        file_handler = logging.FileHandler('logs.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def createRooms(self):
        """
            Sets up all room assets
        :return: None
        """

        # creates room objects
        self.castle_grounds = Room("castle_grounds", "You are in the castle grounds", None)
        self.gatehouse = Room("gatehouse", "You are at the gatehouse", None)
        self.courtyard = Room("courtyard", "You are in the courtyard",
                              "You have to win over the guard before you can get to the courtyard.", False)
        self.chapel = Room("chapel", "You are in the royal chapel", None)
        self.cellar = Room("cellar", "You are in the cellar",
                           "It's very dark down here, you'll need something substantial to light your way \nbefore you can enter the cellars.", False)
        self.undercroft = Room("undercroft", "You are in the undercroft", None)
        self.armoury = Room("armoury", "You are in the armoury", None)
        self.kitchens = Room("kitchens", "You are in the royal kitchens",
                             "You have to win over the guard before you can get to the kitchens", False)
        self.banquet_hall = noExitsRoom("banquet_hall", "You are in the great banquet hall",
                                        "There is a royal feast going on in the banquet hall next door. \nTry searching for something that will pass you off as one of the waiting staff.", False)
        self.cabinet = Room("cabinet", "You are in the royal cabinet rooms", None)
        self.corridor = Room("corridor", "You are in the east wing corridors of the King's private quarters", None)
        self.solar = Room("solar", "You are in the solar room in the castle's private wing", None)
        self.bedchamber = Room("bedchamber", "You are in the King's master bedroom",
                               "You need to convince to doorward to get in here...", False)

        # sets the exits for rooms
        self.castle_grounds.setExit("north", self.gatehouse)
        # self.castle_grounds.setExit("end", self.solar)
        self.castle_grounds.setExit("west", self.chapel)
        self.gatehouse.setExit("north", self.courtyard)
        self.courtyard.setExit("south", self.gatehouse)
        self.gatehouse.setExit("south", self.castle_grounds)
        self.chapel.setExit("east", self.castle_grounds)
        self.chapel.setExit("west", self.cellar)
        self.cellar.setExit("east", self.chapel)
        self.cellar.setExit("north", self.armoury)
        self.armoury.setExit("south", self.cellar)
        self.armoury.setExit("east", self.undercroft)
        self.armoury.setExit("north", self.kitchens)
        self.undercroft.setExit("west", self.armoury)
        self.kitchens.setExit("east", self.banquet_hall)
        self.kitchens.setExit("south", self.armoury)
        self.banquet_hall.setExit("west", self.kitchens)
        self.banquet_hall.setExit("hiddenbookcase", self.cabinet)
        self.cabinet.setExit("bookcase", self.banquet_hall)
        self.cabinet.setExit("west", self.corridor)
        self.corridor.setExit("east", self.cabinet)
        self.corridor.setExit("north", self.bedchamber)
        self.corridor.setExit("west", self.solar)
        self.solar.setExit("east", self.corridor)
        self.bedchamber.setExit("south", self.corridor)

    def createItems(self):
        """
            Sets up all item assets
        :return: None
        """
        # creates item objects
        self.bible = Item("bible", None)
        self.candle = Item("candle", None)
        self.torch = Item("torch", self.cellar)
        self.rope = Item("rope", None, True)
        self.platter = Item("platter", self.banquet_hall)
        self.spoon = Item("spoon", None)
        self.goblet = Item("goblet", None, True)
        self.dress = Item("dress", self.bedchamber)

        # places the items in relevant rooms
        self.chapel.placeItem(self.bible)
        self.chapel.placeItem(self.candle)
        self.cellar.placeItem(self.rope)
        self.kitchens.placeItem(self.goblet)
        self.kitchens.placeItem(self.platter)
        self.kitchens.placeItem(self.spoon)

    def createCharacters(self):
        """
            Sets up all character assets
        :return: None
        """
        # creates character objects
        self.sentry = Guard("Sentry", "a guard of the gatehouse",
                            "Mmmm I'll make you a deal. If we roll the same number on the die, I'll let you through.",
                            True, None, False)
        self.priest = Priest("Priest", "but a humble priest",
                             "confess to me your sins and I can see if the lord can be of service", True, self.torch)
        self.soldier = Guard("Soldier", "...uhhh..*hiccough*... a member of the royal ..yeh ..guards",
                             "Let me strike you a deal you fool.. *hiccough*  ...if we roll the same number on the die, I'll ...*burp* ...let you through.", True, None, True)
        self.nobleman = NoInteraction("Nobleman", "a dull and arrogant Earl.",
                                      "Nothing I can do for you, lowly servant.", False, None)
        self.page = NoInteraction("Page", "a royal servant serving at the feast",
                                  "I am not sure I can help you I am just a lowly servant", False, None)
        self.jester = Jester("Jester", "the court jester", "Answer this riddle and I shall tell you where to go next.",
                             True, None)
        self.princess = NoInteraction("Princess", "the daughter of the king",
                                      "My father is a hard person to pin down, I would suggest talking to the royal fool - he's has a keen eye for the other people's affairs...", False, None)
        self.musician = LutePlayer("Musician", "the lute player of the royal court",
                                   "Let me sing you a song, perhaps it will enlighten you.", True, None)
        self.chancellor = NoInteraction("Chancellor", "the keeper of the privy seal and advisor to the king",
                                        "I'm very busy right now. I'm up to my head in work - the king's royal coffers are a mess! Foreign campaign after foreign campaign.. If only he were more frugal...blah blah blah...", False, None)
        self.doorward = Doorward("Doorward", "the guard of the King's bedchamber",
                                 "The only people allowed in this room are the queen and the lady in waiting. It's very gloomy in this corridor, step towards this light so I can see who you are.", True, None)
        self.countess = Countess("Countess", "the queen's lady in waiting",
                                 "Well I won't ask why. He's a miserable old trout and I'd gladly help anyone in there no questions asked. You need to disguise yourself and then the doorward might let you in. Let me give you a spare dress and this plastic crown", True, self.dress)

        # places the characters in relevant rooms
        self.gatehouse.placeCharacter(self.sentry)
        self.chapel.placeCharacter(self.priest)
        self.armoury.placeCharacter(self.soldier)
        self.banquet_hall.placeCharacter(self.musician)
        self.banquet_hall.placeCharacter(self.nobleman)
        self.banquet_hall.placeCharacter(self.princess)
        self.banquet_hall.placeCharacter(self.jester)
        self.banquet_hall.placeCharacter(self.page)
        self.cabinet.placeCharacter(self.chancellor)
        self.corridor.placeCharacter(self.doorward)
        self.solar.placeCharacter(self.countess)

    def printWelcome(self):
        """
            Displays a backstory welcome message as a string
        :return: message (str)
        """
        # writes to log file that new game has started
        self.logger.info(f'NEW GAME: User started app')
        self.msg = \
            f'You are a blacksmith living in the local village. The king has recently visited your forge to commission a new axe for his latest foreign campaign. However, you suspect him of stealing your favourite teddy bear during his visit.\n' \
            f'You decide to go on a mission to confront him of his crime. This requires breaking into the castle and finding the king.'
        return self.msg

    def printHelp(self):
        """
            Displays a help message with game rules
        :return: message (str)
        """
        self.msg = f"You\'re objective is to find the king.\n"\
        "To move rooms, type the direction you want to go in.\n"\
        "['north', 'south', 'east', west']\n"\
        "You can interact with characters in the room by clicking on them \n"\
        "You can also pick up objects in the room by clicking on them."
        return self.msg

    def doGoCommand(self, command):
        """
            Performs the GO command moving player through rooms
        :param command: the direction the player wishes to travel in
        :return: message depending on whether command calls an exit that exists (str)
        """
        opposites = {"north": "south", "south": "north", "west": "east", "east": "west"}

        try:
            nextRoom = self.currentRoom.getExit(command)
            self.oldRoom = self.currentRoom
            self.currentRoom = nextRoom
            # check you are allowed in next room
            if self.currentRoom.unlocked:
                # writes to log file that new room has been entered
                self.logger.info(f'User entered a new room: {self.currentRoom.name}.')
                self.msg = self.currentRoom.getLongDescription()
                return self.msg
            # if you are not allowed in the next room...
            else:
                # writes to log file that new room could not be entered
                self.logger.info(f'User attempted to enter a locked room: {self.currentRoom.name}.')
                self.msg = f'Mmmm...looks like you can\'t enter this next room \n{self.currentRoom.requirements}\n'
                # you are sent back to the previous room
                nextRoom = self.currentRoom.getExit(opposites[command])
                self.currentRoom = nextRoom
                return self.msg + f'{self.currentRoom.getLongDescription()}'

        except AttributeError:
            directionList = ["NORTH", "SOUTH", "EAST", "WEST", "HIDDENBOOKCASE", "END"]
            if command.upper() not in directionList:
                # writes to log file that invalid direction entered
                self.logger.info(f'User typed {command} which is not a valid direction')
                self.msg = f'This is not a valid direction. \nPlease check spelling.'
                self.currentRoom = self.oldRoom
                return self.msg + " " + self.currentRoom.getLongDescription()
            else:
                # writes to log file that invalid exit attempted
                self.logger.info(f'User attempted to exit {command} but current room does not have this exit')
                self.msg = f'An exit in this direction does not exist! \nTry a different direction.'
                self.currentRoom = self.oldRoom
                return self.msg + " " + self.currentRoom.getLongDescription()

    def doTalkCommand(self, characterName):
        """
            Gets the character's conversation message
        :param characterName: the character name the player is going to talk to
        :return: characters message (str)
        """
        # initiates conversation
        character = self.currentRoom.getCharacterByName(characterName)
        intro = characterName + ": Hello there, I am " + character.description
        convo = str(character.makeConversation())
        self.msg = intro + convo
        # writes to log file that conversation made with character
        self.logger.info(f'User spoke to a character ({characterName}).')
        return self.msg, character.canInteract

    def doInteractionCommand(self, character):
        """
            Initiates the interaction method with a character object
        :param character: the character object the player wishes to interact with
        :return: character's response to the interaction (str)
        """
        room_sequence = {self.gatehouse: self.courtyard, self.chapel: self.cellar, self.armoury: self.kitchens,
                         self.banquet_hall: self.cabinet, self.solar: self.corridor, self.corridor: self.bedchamber}
        # call the character's interaction method
        self.msg, item = character.interact(room_sequence[self.currentRoom])
        # writes to log file that interaction peformed with character
        self.logger.info(f'User chose to continue interaction with character ({character.name}).')
        # if the character does not return an item after the interaction, then just print location
        if item is None:
            return self.msg
        # if the character does return an item after the interaction, place item in the room before printing location
        else:
            self.currentRoom.placeItem(item)
            return self.msg

    def doGetItemCommand(self, item):
        """
            Executes the player's picking up of an item and sends player back to start depending on item attribute
        :param item: the item object the player wishes to pick up
        :return: if wrong item was picked up then message (str) otherwise None
        """
        # otherwise, pick up the item
        item_to_get = self.currentRoom.getItemByName(item)
        self.player.pickUpItem(item_to_get)
        # if item is one that sends you back to start then do this and return appropriate message
        if item_to_get.back_to_start:
            self.currentRoom = self.castle_grounds
            # writes to log file that player picked up wrong item
            self.logger.info(f'User picked up a wrong item ({item}) and was sent back to the start')
            return f'Whoops! You\'ve picked up the wrong item. \nYou look suspicious and the King\'s guards have booted\
             you back outside the castle.'
        else:
            # writes to log file that player picked up an item
            self.logger.info(f'User picked up an item ({item})')
            # unlock room if item unlocks a room
            self.room_it_unlocks = item_to_get.room_it_unlocks
            if self.room_it_unlocks is not None:
                self.room_it_unlocks.unlockRoom()
            return None

    def quit(self):
        """
            writes to log that the game has been quit early
        :return: None
        """
        # writes to log file that player has ended game
        self.logger.info(f'User quit game early.\n')

    def printEnding(self):
        """
            Prints ending sequence message
        :return: end message (str)
        """
        self.msg = \
            "There he is - the thief - curled up in bed with your teddy!\n"
        # writes to log file that player has completed game
        self.logger.info(f'User completed game.\n')
        return self.msg

