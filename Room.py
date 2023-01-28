"""
    Create a room described "description". Initially, it has
no exits. 'description' is something like 'kitchen' or
'an open court yard'.

    Below is a subclass of Room for which the inherited getExits
method has been overwritten to hide exits from user.

"""


class Room:

    def __init__(self, name, description, requirements, unlocked=True):
        """
            Constructor method
        :param description: text description for this room
        :param requirements: text requirements for this entering room
        :param unlocked: boolean value for whether room unlocked or not
        """
        self.name = name
        self.description = description
        self.exits = {}     # Dictionary
        self.items = []
        self.characters = []
        self.requirements = requirements
        self.unlocked = unlocked

    def setExit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room)
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour
        return True

    def placeItem(self, item):
        """
            Adds an item to the room and then the item is stored in a list
        :param item: The item object to be stored
        :return: True
        """
        self.items.append(item)
        return True

    def placeCharacter(self, character):
        """
            Adds a character to the room and then the character is stored in a list
        :param character: The character object to be stored
        :return: True
        """
        self.characters.append(character)
        return True

    def getLongDescription(self):
        """
            Fetch a long description including available exits, items and characters present
        :return: text description
        """
        return f'\n{self.description}\n Exits: {self.getExits()}'

    def getCharacterByName(self, name):
        """
            Provides a method to call a character object by name
        :param name: The name of the character
        :return: character object
        """
        list_characters = [character.name for character in self.characters]
        index1 = list_characters.index(name)
        return self.characters[index1]

    def getAllRoomCharacters(self):
        """
            Provides a list of all characters in the room
        :return: character list
        """
        list_characters = [character.name for character in self.characters]
        return list_characters

    def getAllRoomItems(self):
        """
            Provides a list of all items in the room
        :return: item list
        """
        list_items = [item.name for item in self.items]
        return list_items

    def getItemByName(self, name):
        """
            Provides a method to call an item object by name
        :param name: The name of the item
        :return: item object
        """
        list_items = [item.name for item in self.items]
        i = list_items.index(name)
        return self.items.pop(i)

    def unlockRoom(self):
        """
            unlocks room by setting unlocked parameter to True
        :return: None
        """
        self.unlocked = True

    def getExits(self):
        """
            Fetch all available exits as a list
        :return: list of all available exits
        """
        allExits = self.exits.keys()
        return list(allExits)

    def getExit(self, direction):
        """
            Fetch an exit in a specified direction
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None


class noExitsRoom(Room):

    def __init__(self, name, description, requirements, unlocked):
        """
            Constructor method (inherits from Room super class)
        """
        super().__init__(name, description, requirements, unlocked)

    def getExits(self):
        """
            overwrites superclass method of fetching all available exits as a list
        :return: list of text that informs you exits for this room are hidden
        """
        return "The exits for this room have been hidden.\n Ask around to find out where to go next"


