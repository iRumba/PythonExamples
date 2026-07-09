from User import User
from ConsolePrinter import ConsolePrinter
from AbstractPrinter import AbstractPrinter

content: str

with open('username.txt', 'r', encoding='utf-8') as f:
    content = f.read()

user = User(content)

print(user.name)

printer: AbstractPrinter = ConsolePrinter()

printer.print("Hello!")