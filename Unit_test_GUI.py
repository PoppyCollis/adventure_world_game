import unittest
from GUI import *
import tkinter as tk
from pynput.keyboard import Key, Controller


""""
    Automated unit test for the GUI class to test instantiation.
Requirements: pynput
"""


class Test(unittest.TestCase):

    def setUp(self):
        self.win = tk.Tk()  # Create a window
        self.win.configure(bg='BLACK')
        self.win.title("Adventure World with GUI")  # Set window title
        self.win.geometry("800x600")  # Set window size
        self.win.resizable(True, True)  # Both x and y dimensions ...

    def tearDown(self):
        self.win.destroy()

    def test_instantiation(self):
        self.keyboard = Controller()
        self.keyboard.press(Key.enter)
        result = App(self.win)
        self.keyboard.release(Key.enter)
        self.assertTrue(result)

