from Game import *
import unittest

"""
    Automated system level testing for entire game functioning
"""


class Test(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        del self.game

    def test_full_game(self):
        # going north should lead to gatehouse
        self.assertEqual(self.game.doGoCommand('north'),  f'\n{self.game.gatehouse.description}\n Exits: {self.game.gatehouse.getExits()}')
        # you can talk to and interact with the sentry in the gatehouse
        self.assertEqual(self.game.doTalkCommand('Sentry'), (self.game.msg, self.game.sentry.canInteract))
        self.game.doInteractionCommand(self.game.sentry)
        # however, interaction does not allow you to go north to courtyard
        self.assertEqual(self.game.doGoCommand('north'), f'Mmmm...looks like you can\'t enter this next room \n{self.game.courtyard.requirements}\n' + f'{self.game.gatehouse.getLongDescription()}')
        # go south then west leads to chapel
        self.game.doGoCommand('south')
        self.game.doGoCommand('west')
        self.assertEqual(self.game.currentRoom, self.game.chapel)
        # you can talk with the priest
        self.assertEqual(self.game.doTalkCommand('Priest'), (self.game.msg, self.game.priest.canInteract))
        # you cannot pick up torch before interacting with the priest
        self.assertRaises(ValueError, self.game.doGetItemCommand, 'torch')
        self.assertEqual(self.game.doInteractionCommand(self.game.priest), self.game.msg)
        # priest has left torch in room after interaction
        self.game.doGetItemCommand('torch')
        # torch unlocks cellar door
        self.assertTrue(self.game.cellar.unlocked)
        self.game.doGoCommand('west')
        # picking up rope object leads you to be teleported back to the start (castle grounds)
        self.game.doGetItemCommand('rope')
        self.assertEqual(self.game.currentRoom, self.game.castle_grounds)
        # navigate to armoury
        self.game.doGoCommand('west')
        self.game.doGoCommand('west')
        self.game.doGoCommand('north')
        self.assertEqual(self.game.currentRoom, self.game.armoury)
        # talk to soldier
        self.assertEqual(self.game.doTalkCommand('Soldier'), (self.game.msg, self.game.soldier.canInteract))
        # play dice game with drunk soldier until you have won
        while not self.game.kitchens.unlocked:
            self.game.doInteractionCommand(self.game.soldier)
        # winning unlocks door and allows you to go north to kitchens
        self.game.doGoCommand('north')
        self.game.doGetItemCommand('goblet')
        # picking up goblet also sends you back to the beginning
        self.assertEqual(self.game.currentRoom, self.game.castle_grounds)
        # navigate back to kitchens
        self.game.doGoCommand('west')
        self.game.doGoCommand('west')
        self.game.doGoCommand('north')
        self.game.doGoCommand('north')
        # banquet hall locked
        self.game.doGoCommand('east')
        self.assertNotEqual(self.game.currentRoom, self.game.banquet_hall)
        # picking up platter unlocks door
        self.game.doGetItemCommand('platter')
        self.game.doGoCommand('east')
        self.assertEqual(self.game.currentRoom, self.game.banquet_hall)
        # check that the correct list of characters is there
        self.assertEqual(self.game.currentRoom.getAllRoomCharacters(), ['Musician', 'Nobleman', 'Princess', 'Jester', 'Page'])
        # hidden book case exit takes you to cabinet room
        self.game.doGoCommand('hiddenbookcase')
        self.assertEqual(self.game.currentRoom, self.game.cabinet)
        self.game.doGoCommand('west')
        # kings bedchamber is locked
        self.assertFalse(self.game.bedchamber.unlocked)
        # talk and interact with the countess
        self.game.doGoCommand('west')
        self.game.doTalkCommand('Countess')
        self.game.doInteractionCommand(self.game.countess)
        # pick up dress she leaves in room
        self.game.doGetItemCommand('dress')
        self.game.doGoCommand('east')
        # interact with doorward, who lets you through
        self.game.doTalkCommand('Doorward')
        self.assertEqual(self.game.doInteractionCommand(self.game.doorward), f'Oh its you m\'lady. What a lovely dress! The door is open.')
        # player has made it to bedchamber, end of game
        self.game.doGoCommand('north')
        self.assertEqual(self.game.currentRoom, self.game.bedchamber)


