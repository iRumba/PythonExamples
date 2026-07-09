from AbstractPrinter import AbstractPrinter

class ConsolePrinter(AbstractPrinter):
    def print(self, string):
        print(string)