##############################IMPORTS##############################

import sys, pygame, itertools, random, time
from threading import Thread
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from pygame.locals import *
from PyQt5 import uic, QtCore, Qt
from grid import *
from view import *

##############################GLOBALS##############################

black = (0, 0, 0)
purple = (255, 0, 255)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


enumerateList = []
state1 = []
state2 = []
state3 = []
rule = []
limit = 0
base = 0
interval = 0
##############################INTERFACE##############################


class WindowPQ(QMainWindow):
    def __init__(self):
        #1,1,1,2,1,2,1,0,0,0
        # iniciar pbjeto QMainWindow
        QMainWindow.__init__(self)
        # Cargar archivo
        uic.loadUi("Automata.ui", self)
        # 0,1,1,1,2,1,0,0,0,2
        self.initUI()

    def initUI(self):
        self.addInstruments.clicked.connect(lambda: self.instrument())
        self.addState.clicked.connect(lambda: self.state_list())
        self.start.clicked.connect(
            lambda: self.setup(
                interval,
                base,
                rule,
                state1,
                state2,
                state3,
                enumerateList,
                limit
            )
        )
#0,1,2,1,0,1,2,0,1,2
    def return_list(self, string):
        string_list = string.split(",")
        int_list = []
        for i in string_list:
            int_list.append(int(i))
        return int_list

    def state_list(self):
        global state1
        global state2
        global state3
        global rule
        global limit
        global base
        global interval

        rule = int(self.inputRule.text())
        limit = 10
        base = int(self.inputBase.text())
        interval = int(self.interval.text())
        state1 = self.states(self.state1.text())
        state2 = self.states(self.state2.text())
        state3 = self.states(self.state3.text())


    def states(self, string):
        state_list = []
        state_list = self.return_list(string)
        return state_list

    def instrument(self):
        instruments = []
        if self.Bamboo.isChecked():
            instruments.append("Bamboo")
        if self.Bass.isChecked():
            instruments.append("Bass")
        if self.Bell.isChecked():
            instruments.append("Bell")
        if self.Flute.isChecked():
            if len(instruments) < 4:
                instruments.append("Flute")
        if self.Guitar.isChecked():
            if len(instruments) < 4:
                instruments.append("Guitar")
        if self.MusicBox.isChecked():
            if len(instruments) < 4:
                instruments.append("MusicBox")
        if self.Synthesizer.isChecked():
            if len(instruments) < 4:
                instruments.append("Synthesizer")
        if self.Triangles.isChecked():
            if len(instruments) < 4:
                instruments.append("Triangles")
        if self.Violin.isChecked():
            if len(instruments) < 4:
                instruments.append("Violin")
        if self.Voice.isChecked():
            if len(instruments) < 4:
                instruments.append("Voice")
        global enumerateList
        enumerateList = instruments
        #print(enumerateList)

    def setup(
        self,
        timer,
        base,
        rule,
        state1,
        state2,
        state3,
        sounds,
        limit
    ):
        """
		Instances the pygame window and creates the main loop.
		"""
        window = pygWindow(
            timer,
            base,
            rule,
            state1,
            state2,
            state3,
            sounds,
            limit
        )
        # text, None, [0,1,2,1,1,0,2,0,1,2], [0,1,2,1,1,0,2,0,1,2], [0,1,2,1,1,0,2,0,1,2], None, None, None, 10)
        window.grid.draw_grid(window.surface)
        window.grid2.draw_grid(window.surface)
        window.grid3.draw_grid(window.surface)

        while True:
            window.clock.tick(40)
            # window.draw_stuff()
            window.handle_events()


app = QApplication(sys.argv)
_window = WindowPQ()
_window.show()
app.exec_()

