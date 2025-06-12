# CastleStorm
Adventure game written in Python in order to practice good <strong>OOP principles</strong> as well as <strong>debugging</strong>, <strong>unit testing</strong> and implementing a customised <strong>graphical user interface</strong> using Tkinter.

To play, run <strong>GUI.py</strong>

![class_diagram](https://user-images.githubusercontent.com/44060045/215266879-5c8919da-61e7-49b8-8bcb-24bdc4a175a4.png)

See <strong>Unit_test_GUI.py</strong> and <strong>Unit_tests.py</strong> for automated unit testing.
See <strong>logs.log</strong> - the game imports a logging module in order to write to a log file documenting the users inputs throughout a game.

In this game, you play the character of a blacksmith who suspects the king of stealing something important of yours on his recent trip
to your forge. The objective of the game is to break into the castle and find the king in order to confront him and take back what is rightfully yours.
The game begins in the castle grounds. You are able to move to different locations (rooms) in the game by typing an input into the command prompt before pressing 'GO'.

Your full set of commands are
‘north’, ‘south’, ‘east’, ‘west’

Through the GUI, you can view the items in your inventory by pressing the ‘inventory’ menu button. You can press the ‘help’ button which will display a useful message telling you how to play the game and you can also quit the game either via the quit button on the menu bar or using the ‘x’ button on the window based on the operating system.

Characters can be spoken to and interacted with by clicking on them. Likewise, you can click on items in the room and this will pick them up and store them in your inventory.

The end goal is to find the King (who is in the bedchamber) so the game ends once you
have reached this room.

NOTE: This program was designed based around the starter code provided by
Kingsley Sage, which involves moving through different locations and interacting with
objects.
