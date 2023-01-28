"""
    Create an item with a name and room that it unlocks
"""
class Item:

    def __init__(self, name, room_it_unlocks, back_to_start=False):
        """
            constructor method
        :param name: name of item
        :param description: text description for this room (str)
        """
        self.name = name
        self.room_it_unlocks = room_it_unlocks
        self.back_to_start = back_to_start


