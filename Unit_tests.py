from Game import *
from Room import *
from Player import *
from Characters import *
from Item import *
import unittest
"""
    Automated unit testing for project classes
"""


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.test_room = Room("test_room", "test_room_description", "test_room requirements")
        self.test_locked_room = Room("test_locked_room", "test_room_description", "test_locked_room requirements", False)
        self.no_exits_room = noExitsRoom("no_exits_room", "test_room_description", "no_exits_room requirements", True)
        self.i1 = Item("test_item", "test_locked_room", False)
        self.i2 = Item("test_item2", None, False)
        self.c1 = Character("character1", "character1 description", "character1 conversation", False, None)
        self.c2 = Character("character2", "character2 description", "character2 conversation", False, None)

    def tearDown(self):
        del self.test_room, self.test_locked_room, self.no_exits_room,  self.i1,  self.i2,  self.c1,  self.c2

    def test_1_lock_related(self):
        # check that new room should automatically be unlocked because of keyword argument
        self.assertEqual(self.test_room.unlocked, True)
        # check test_locked_room is locked
        self.assertEqual(self.test_locked_room.unlocked, False)
        # unlockRoom and check unlock is now True
        self.test_locked_room.unlockRoom()
        self.assertEqual(self.test_locked_room.unlocked, True)
        # set exits to room and check it returns Equal

    def test_2_exit_related(self):
        self.assertTrue(self.test_room.setExit("west", self.no_exits_room))
        # get exits should equal len(number in setExits)
        self.assertEqual(len(self.test_room.getExits()), 1)
        # get exit? check it returns None for an exit that has not been set
        self.assertEqual(self.test_room.getExit("north"), None)
        # get exit returns equal self.exits[direction]
        self.assertEqual(self.test_room.getExit("west"), self.no_exits_room)
        # for noExitsRoom check getExits returns equal to message
        self.assertEqual(self.no_exits_room.getExits(), f'The exits for this room have been hidden.\n Ask around to find out where to go next')

    def test_3_item_related(self):
        # place an item in a room and check it returns True
        self.assertTrue(self.test_room.placeItem(self.i1))
        # add another item and check len(getAllRoomItems()) is 2
        self.test_room.placeItem(self.i2)
        self.assertEqual(len(self.test_room.getAllRoomItems()), 2)
        # getItemByName and check that it returns an item object for which any attribute can be retrieved
        item = self.test_room.getItemByName("test_item2")
        self.assertEqual(item.room_it_unlocks, None)
        # check that the item above was correctly popped (removed) from items in the room - so len of list is now 1
        self.assertEqual(len(self.test_room.getAllRoomItems()), 1)

    def test_4_character_related(self):
        # placeCharacters in room and check it returns True
        self.assertTrue(self.test_room.placeCharacter(self.c1))
        # place another character and check len self.characters = 2
        self.test_room.placeCharacter(self.c2)
        self.assertEqual(len(self.test_room.getAllRoomCharacters()), 2)
        # get correct output for getLongDescription
        self.test_room.placeItem(self.i2)
        self.assertEqual(self.test_room.getLongDescription(), f'\ntest_room_description\n Exits: []')


class TestCharacters(unittest.TestCase):

    def setUp(self):

        self.test_locked_room = Room("test_locked_room", "test_locked_room description", "test_locked_room requirements", False)
        self.i1 = Item("test_item", "test_locked_room", False)
        self.c1 = Character("c1", "c1 description", "c1 conversation.", canInteract=True, item=None)
        self.g1 = Guard("g2", "g2 description", "g2 conversation.", canInteract=True, item=None, drunk=False)
        self.p1 = Priest("p1", "p1 description", "p1 conversation.", canInteract=True, item=self.i1)
        self.l1 = LutePlayer("l1", "l1 description", "l1 conversation.", canInteract=True, item=None)
        self.j1 = Jester("j1", "j1 description", "j1 conversation.", canInteract=True, item=None)
        self.n1 = NoInteraction("m1", "m1 description", "m1 conversation.", canInteract=False, item=None)
        self.m1 = Countess("m1", "m1 description", "m1 conversation.", canInteract=True, item=self.i1)
        self.d1 = Doorward("d1", "d1 description", "d1 conversation.", canInteract=True, item=None)

    def tearDown(self):
        del self.i1, self.test_locked_room, self.c1, self.g1, self.p1, self.l1, self.j1, self.m1, self.d1

    def test_interactions(self):
        # check that make conversation with a normal character returns the stock conversation intros
        self.assertEqual(self.c1.makeConversation(), f'\nYou: I am looking for the king\n{self.c1.name}: {self.c1.conversation}')
        # check that it returns a different response if canInteract is False
        self.c1.canInteract = False
        self.assertEqual(self.c1.makeConversation(), f'\nOh ...it\'s you again! Go away.')
        # check outcome of interacting with priest and countess is a message plus the item in their possession
        self.assertEqual(self.p1.interact(self.i1.room_it_unlocks), (self.p1.msg, self.i1))
        # check once you have already interacted, then canInteract is set to false
        self.p1.interact(self.i1.room_it_unlocks)
        self.assertEqual(self.p1.makeConversation(), f'\nOh ...it\'s you again! Go away.')
        # check lute player returns song with interaction
        self.assertIn(f'*dreadful music ensues*', self.l1.interact(self.test_locked_room)[0])
        # check when noInteraction character has already interacted, they return correct response
        self.n1.hasInteracted = True
        self.assertEqual(self.n1.makeConversation(), f'\nOh ...it\'s you again! Go away.')

    def test_2_guards(self):
        # check that roll dice with sober guard that can interact always returns lost
        self.assertEqual(list(self.g1.roll_dice())[0], "lost")
        # check that dice game with a drunk guard can be won
        self.g1.drunk = True
        while not self.test_locked_room.unlocked:
            result = self.g1.interact(self.test_locked_room)
        self.assertEqual(result, (f'You rolled a {self.g1.your_go}\nThe guard rolled a {self.g1.guards_go}' + '\nYou\'ve won! The guard reluctantly unlocks the door for you.', self.g1.item))

    def test_jester(self):
        # check the response of the jester when you give the right answer
        response = self.j1.answer('a candle')
        self.assertEqual(response, f'Right answer well done. Try the hiddenbookcase...')
        response = self.j1.answer('candle')
        self.assertEqual(response, f'Right answer well done. Try the hiddenbookcase...')
        # check the response of the jester when you give the wrong answer
        response = self.j1.answer('any string')
        self.assertEqual(response, f'Try coming back to me with a better answer')
        # check the response of the jester when you ask for a hint
        response = self.j1.answer('hint')
        self.assertEqual(response, f'I am made of wax')

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.i1 = Item("test_item", "test_locked_room", False)
        self.i2 = Item("test_item2", "test_locked_room", False)

    def tearDown(self):
        del self.player, self.i1, self.i2

    def test_backpack(self):
        # test pick up item returns true
        self.assertTrue(self.player.pickUpItem(self.i1))
        # add another item and check backpack returns 2 items
        self.player.pickUpItem(self.i2)
        self.assertEqual(len(self.player.showBackpackItems()), 2)


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        del self.game

    def test_1_initialisation(self):
        # check (sample of) rooms have been successfully created with exits once game is initialised
        self.assertEqual(self.game.castle_grounds.getExits(), ['north', 'west'])
        self.assertEqual(self.game.chapel.getExits(), ['east', 'west'])
        self.assertEqual(self.game.kitchens.getExits(), ['east', 'south'])
        # check (sample of) items have been successfully created and placed in rooms
        self.assertEqual(self.game.chapel.getAllRoomItems(), ['bible', 'candle'])
        self.assertEqual(self.game.kitchens.getAllRoomItems(), ['goblet', 'platter', 'spoon'])
        # check (sample of) characters have been successfully created and placed in rooms
        self.assertEqual(self.game.gatehouse.getAllRoomCharacters(), ['Sentry'])
        self.assertEqual(self.game.banquet_hall.getAllRoomCharacters(), ['Musician', 'Nobleman', 'Princess', 'Jester', 'Page'])

