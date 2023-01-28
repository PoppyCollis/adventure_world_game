import random
"""
    This class is the Character class for creating characters that can be placed
within rooms in the game. Create a character by defining name, description,
conversation, canInteract, item.

    Below are some subclasses of character that have specific interaction methods
defined.

"""


class Character:

    def __init__(self, name, description, conversation, canInteract, item):
        """
            Constructor method
        :param name: name for this character (str)
        :param description: text description for this character (str)
        :param conversation: first line of conversation when you talk to this character (str)
        :param canInteract: value indicating whether player can interact with character or not (bool)
        :param item: item in characters possession
        """
        self.name = name
        self.description = description
        self.conversation = conversation
        self.canInteract = canInteract
        self.item = item

    def makeConversation(self):
        """
            returns the conversation with character
        :return: character's message (str)
        """
        # returns a different message depending on whether player can interact or not
        if self.canInteract:
            self.msg = f'\nYou: I am looking for the king\n{self.name}: {self.conversation}'
            return self.msg
        else:
            self.msg = f'\nOh ...it\'s you again! Go away.'
            return self.msg


class Guard(Character):

    def __init__(self, name, description, conversation, canInteract, item, drunk):
        """
            Constructor method (Inherits from Character super class)
        :param name: name for this character (str)
        :param description: text description for this character (str)
        :param conversation: first line of conversation when you talk to this character (str)
        :param canInteract: value indicating whether player can interact with character or not (bool)
        :param item: item in characters possession
        :param drunk: value of whether the guard is drunk or not (bool)
        """
        super().__init__(name, description, conversation, canInteract, item)
        self.drunk = drunk

    def roll_dice(self):
        """
            Executes dice game with guard character
        :return: result (str) and text response (str)
        """
        # pick a random integer between 1 and 3 for your roll
        self.your_go = random.randint(1, 3)
        # when guard is not drunk you will always lose the game
        if not self.drunk:
            # always add a random value between 1 and 3 to your go for guards go
            self.guards_go = self.your_go + random.randint(1, 3)
            if self.your_go == self.guards_go:
                result = "won"
            else:
                result = "lost"
            return result, f'You rolled a {self.your_go}\nThe guard rolled a {self.guards_go}'

        # when guard is drunk you have 50/50 chance of winning the game
        else:
            # either a 1 or 0 is added to your go for guards go
            self.guards_go = self.your_go + random.randint(0, 1)
            if self.your_go == self.guards_go:
                result = "won"
            else:
                result = "lost"
            return result, f'You rolled a {self.your_go}\nThe guard rolled a {self.guards_go}'

    def interact(self, room):
        """
            Executes character interaction based on dice game result
        :param: room object that character can unlock
        :return: tuple of message of character response (str) and the item in character's possession
        """
        game_result, string_ans = self.roll_dice()
        # return different message depending on game result
        if game_result == 'won':
            room.unlocked = True
            self.canInteract = False
            msg = string_ans + '\nYou\'ve won! The guard reluctantly unlocks the door for you.'
            return msg, self.item
        # if you lost return different message depending on whether drunk or not
        else:
            if self.drunk:
                msg = string_ans + '\nSorry you\'ve lost. But try talking to the guard again and have another go. He\'s\
                 so drunk he might not remember who you are'
                return msg, self.item
            else:
                self.canInteract = False
                msg = string_ans + '\nOh dear, you\'ve lost the bet. The guard won\'t let you in.'
                return msg, self.item


class Priest(Character):

    def __init__(self, name, description, conversation, canInteract, item):
        """
            Constructor method
        :param name: name for this character (str)
        :param description: text description for this character (str)
        :param conversation: first line of conversation when you talk to this character (str)
        :param canInteract: value indicating whether player can interact with character or not (bool)
        :param item: item in characters possession
        """
        super().__init__(name, description, conversation, canInteract, item)

    def interact(self, room):
        """
            Executes character interaction
        :param: room object that character can unlock (redundant)
        :return: characters message (str) and item in possession
        """
        # note: room not used but means that Game class can call interact consistently regardless of character
        self.msg = 'You: forgive me father for I have si-\n'\
                   'Priest: Yeh yeh great, what do you want?\n'\
                   'You: To find the king?\n'\
                   'Priest: Cool, I\'ll leave this {} here in the chapel for you\n'\
                   'You: Ok..thanks'.format(self.item.name)
        # make sure character can't interact next time
        self.canInteract = False
        return self.msg, self.item


class LutePlayer(Character):

    def __init__(self, name, description, conversation, canInteract, item):
        """
            Constructor method
        :param name: name for this character (str)
        :param description: text description for this character (str)
        :param conversation: first line of conversation when you talk to this character (str)
        :param canInteract: value indicating whether player can interact with character or not (bool)
        :param item: item in characters possession
        """
        super().__init__(name, description, conversation, canInteract, item)

    def interact(self, room):
        """
            Executes character interaction
        :param: room object that character can unlock (redundant)
        :return: characters message (str) and item in possession
        """
        # note: room not used but means that Game class can call interact consistently regardless of character
        self.msg = \
            f'*dreadful music ensues*\n'\
            'Alas my love you do me wrong\n'\
            'To cast me off discourteously;\n'\
            'And I have loved you oh so long\n'\
            'Delighting in your company.\n'\
            'Greensleeeeeeves was my delight,\n'\
            'Greensleeeeeeeeves...\n'\
            'You: Good lord please stop that\'s horrible\n'\
            'Musician: You ungrateful pig!\n'
        # make sure character can't interact next time
        self.canInteract = False
        return self.msg, self.item


class Jester(Character):

    def __init__(self, name, description, conversation, canInteract, item):
        """
            Constructor method
        :param name: name for this character (str)
        :param description: text description for this character (str)
        :param conversation: first line of conversation when you talk to this character (str)
        :param canInteract: value indicating whether player can interact with character or not (bool)
        :param item: item in characters possession
        """
        super().__init__(name, description, conversation, canInteract, item)

    def interact(self, room):
        """
            Executes character interaction
        :param: room object that character can unlock
        :return: characters message (str) and item in possession
        """
        # note: room not used but means that Game class can call interact consistently regardless of character
        self.msg = \
            f'Jester: I\'m tall when I\'m young, and I\'m short when I\'m old. What am I?\n'\
            '[type \'hint\' if you need a clue]'
        return self.msg, self.item

    def answer(self, user_input):
        """
        :param user_input: which is user's guess of riddle answer (str)
        :return: character's response depending on input (str)
        """
        # analyse user input
        if user_input.upper() == "A CANDLE" or user_input.upper() == "CANDLE":
            # make sure character can't interact once user gets answer right
            self.canInteract = False
            return f'Right answer well done. Try the hiddenbookcase...'
        elif user_input.upper() == 'HINT':
            return f'I am made of wax'
        else:
            return f'Try coming back to me with a better answer'


class NoInteraction(Character):

    def __init__(self, name, description, conversation, canInteract, item, hasInteracted=False):
        """
            Constructor method
        :param name: name for this character (str)
        :param description: text description for this character (str)
        :param conversation: first line of conversation when you talk to this character (str)
        :param canInteract: value indicating whether player can interact with character or not (bool)
        :param item: item in characters possession
        :param hasInteracted: value indicating whether character has already interacted or not (bool)

        """
        super().__init__(name, description, conversation, canInteract, item)
        self.hasInteracted = hasInteracted

    def makeConversation(self):
        """
            Prints the conversation with character depending on value of hasInteracted
        :return: character's message (str)
        """
        if not self.hasInteracted:
            # if character has not already interacted once
            self.msg = f'\nYou: I am looking for the king \n{self.name}: {self.conversation}'
            self.hasInteracted = True
            return self.msg
        else:
            # if character has already interacted once
            self.msg = f'\nOh ...it\'s you again! Go away.'
            return self.msg


class Countess(Character):

    def __init__(self, name, description, conversation, canInteract, item):
        """
            Constructor method (Inherits from Character super class)
        :param name: name for this character (str)
        :param description: text description for this character (str)
        :param conversation: first line of conversation when you talk to this character (str)
        :param canInteract: value indicating whether player can interact with character or not (bool)
        :param item: item in characters possession
        """
        super().__init__(name, description, conversation, canInteract, item)

    def interact(self, room):
        """
            Executes character interaction
        :param: room object that character can unlock
        :return: characters message (str) and item in possession
        """
        # note room not used - means that Game class can call interact consistently regardless of character
        self.msg = f'*She comes back with a frilly silk dress and tiny crown*\nYou: It looks a bit small.. I don\'t \
        know if I really wa-\nCountess: You\'ll look great. I\'ll leave it here for you.'
        self.canInteract = False
        return self.msg, self.item


class Doorward(Character):

    def __init__(self, name, description, conversation, canInteract, item):
        """
            Constructor method (Inherits from Character super class)
        :param name: name for this character
        :param description: text description for this character
        :param conversation: first line of conversation when you talk to this character
        :param canInteract: boolean value indicating whether player can interact with character or not
        :param item: item in characters possession
        """
        super().__init__(name, description, conversation, canInteract, item)

    def interact(self, room):
        """
            Executes character interaction: different response depending on whether door locked or not
        :param: room object that character can unlock
        :return: characters response (str)
        """
        if room.unlocked:
            self.msg = f'Oh its you m\'lady. What a lovely dress! The door is open.'
            return self.msg, self.item
        else:
            self.msg = f'Bah! You are no lady! And certainly no queen. You are not allowed in this room. Go away.'
            return self.msg, self.item

