"""
    Player class in order to allow user to pick up
and store items from the game
"""


class Player:

    def __init__(self):
        """
            Constructor method
        """
        self.backpack = []

    def pickUpItem(self, item):
        """
            Puts item in backpack
        :param: item object
        :return: True
        """
        self.backpack.append(item)
        return True

    def showBackpackItems(self):
        """
            Shows items in backpack
        :return: items names for each item in backpack (list)
        """
        return [item.name for item in self.backpack]
